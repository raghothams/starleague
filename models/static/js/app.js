$( function(){
	app = {
		init: function(){
			var that = this;
			var userinfoXHR = $.ajax({
				url: '/app/welcome',
				success: function(res){
					app.userinfo = res.data;
					that.requestLeaderBoard();
				},
				error: function(req,statusText,error){
					console.log(statusText);
				}
			});

			// userinfoXHR.then(function(){
			// 	var batchinfoXHR = $.ajax({
			// 		url: 'http://localhost:8082/app/batch/'+app.userinfo.batch,
			// 		success: function(res){
			// 			app.batchInfo = res.data;
			// 			dataRenderer.rateNow();
			// 		},
			// 		error: function(req,statusText,error){
			// 			console.log(statusText);
			// 		}
			// 	});
			// });

			var lbXHR = $.ajax({
				url:'/app/leaderboard',
				success: function(res){
					dataRenderer.leaderboardInit(res.data);
				}
			}).error(function(req,statusText,error){console.log(statusText);});
		},

		requestLeaderBoard : function(){
			var batchinfoXHR = $.ajax({
					url: '/app/batch/'+app.userinfo.batch,
					success: function(res){
						app.batchInfo = res.data;
						dataRenderer.rateNow();
					},
					error: function(req,statusText,error){
						console.log(statusText);
					}
				});
		},

		validate_rating_info: function(evt){
			var boolSubj =false;
			var boolDate =false;
			var boolStar =false;

			var txtSubj = $('#subject-name-lbl').text();
			if(txtSubj && txtSubj!=0){
				boolSubj=true;
			} else{
				var error_msg = '<div class="alert alert-error">Please check subject name</div>'
				  				$('#msg-container').html(error_msg);
			}

			var txtDate = $('#form-date').val();
			if(txtDate && txtDate!=0){
				var dates = txtDate.split('/');
				var d = new Date(dates[2],parseInt(dates[1])-1,dates[0]);
				if(d.getDay() == 6){
					boolDate=true;	
				} else{
						var error_msg = '<div class="alert alert-error">Please check the date for a Saturday</div>'
				  		$('#msg-container').html(error_msg);
				}
			} else{
					var error_msg = '<div class="alert alert-error">Please check the date for a Saturday </div>'
				  	$('#msg-container').html(error_msg);
			}

			var txtStar = $('#form-star').find(":selected").text();
			if(0<parseInt(txtStar)<5){
				boolStar = true;
			} else{
				var error_msg = '<div class="alert alert-error">Please check the rating</div>'
				  				$('#msg-container').html(error_msg);
			}

			if(boolSubj && boolDate && boolStar){
				data = {};
				data.date = txtDate.replace('/','_').replace('/','_'); // bad hack
				data.subject = txtSubj;
				data.sem = app.userinfo.current_sem;
				data.star = parseInt(txtStar);
				data.user = app.userinfo.username;
				data.batch = app.userinfo.batch;
				
				$.ajax({
				  type: "POST",
				  url: "/app/rating",
				  data: data,
				  success: function(response){
				  				console.log(response);
				  				responseObj = JSON.parse(response);
				  				var msg;
				  				if(responseObj.error){
				  					var msg = '<div class="alert alert-error">'+responseObj.data+'</div>'
				  				} else{
				  					var msg = '<div class="alert alert-success">'+responseObj.data+'</div>'
				  				}
				  				
				  				$('#msg-container').html(msg);
				  			},
				  error: function(error, status){
				  				var error_msg = '<div class="alert alert-error">An error occurred</div>'
				  				$('#msg-container').html(error_msg);
				  			}
				});
			}
		}
	}

	dataRenderer = {

		leaderboardInit: function(dataList){
			var that = this;
			var resultList = [] 
			
			$.each(dataList, function(index, value){
				resultList.push(that.flattenLBData(value));
			});

			app.leaderboard = resultList;

			$.each(resultList, function(index, value){
				
				var stars = that.generateStar(parseInt(value.avg));
				var html = '<div class = "span4"><div class="well cards"><h2>'+value.subject+'</h2><div class="rows">'+value.faculty+'</div><div class="rows" id="stars-div">'+stars+'</div><div class="rows"><span>'+value.batch+'</span> <span>'+value.sem+' - sem</span></div></div></div>';
				$('#leader-board-base').append(html);

			});

			$('#btn-rate').click(function(evt){app.validate_rating_info(evt);});
			
			$('#tab-leader-board').click(function(evt){
				$('#leader-board-base').show();
				$('#rate-now').hide();
				$('#tab-leader-board').parent().addClass('active');
				$('#tab-rate-now').parent().removeClass('active');
			});

			$('#tab-rate-now').click(function(evt){
				$('#leader-board-base').hide();
				$('#rate-now').show();
				$('#tab-leader-board').parent().removeClass('active');
				$('#tab-rate-now').parent().addClass('active');
			});

			// $('#tab-logout').click(function(evt){
			// 	$.ajax({
			// 		url: 'http://localhost:8082/app/logout',
			// 		dataType: "html"
			// 		// success: function(res){
			// 		// 	app.userinfo = res.data;
			// 		// },
			// 		error: function(req,statusText,error){
			// 			console.log(statusText);
			// 		}
			// 	});			
			// });

		},

		flattenLBData: function(item){
			var obj = {};
			var innerObj = item.result[0];
			
			obj.subject = innerObj._id.subject;
			obj.sem = innerObj._id.sem;
			obj.batch = innerObj._id.batch;
			obj.faculty = item.faculty;
			obj.avg = innerObj.avg
			
			return obj;
		},

		generateStar: function(starNum){
			var star = '<img class = "star-img" src ="/static/img/star.png">';
			var html = "";
			for(i=0; i<starNum; i++){
				html+=star;
			}
			return html;
		},

		rateNow: function(){
			var subjects = app.batchInfo[0].subject_master;
			$.each(subjects, function(index, value){
				var html = '<li><a href="#" class="subject-row">'+value.name+'</a></li>'
				$('#subject-list').append(html)
			});
			$('.subject-row').click(function(evt){
				$('.subject-row').removeClass('active');
				
				$('#subject-name-lbl').text(evt.target.text);

				$.each(subjects, function(index, value){
					if(value.name == evt.target.text){
						$('#faculty-lbl').text(value.faculty);
					}
				});
				$(evt.target).addClass('active');
			});
		}
	}



	app.init();







});