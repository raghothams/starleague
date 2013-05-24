$( function(){
	app = {
		init: function(){
			var that = this;
			$.ajax({
				url:'http://localhost:8082/app/welcome',
				success: function(res){
					that.welcome = res;
				}
			}).error(function(req,statusText,error){console.log(statusText);})

			$.ajax({
				url:'http://192.168.43.57:8082/app/leaderboard',
				success: function(res){
					dataRenderer.leaderboardInit(res.data);

				}
			}).error(function(req,statusText,error){console.log(statusText);})
		}
	}

	dataRenderer = {

		leaderboardInit: function(dataList){
			var that = this;
			var resultList = [] 
			
			$.each(dataList, function(index, value){
				resultList.push(that.flattenLBData(value));
			});

			that.leaderboard = resultList;

			$.each(resultList, function(index, value){
				
				var stars = that.generateStar(parseInt(value.avg));
				var html = '<div class = "span4"><div class="well cards"><h2>'+value.subject+'</h2><div class="rows">'+value.faculty+'</div><div class="rows" id="stars-div">'+stars+'</div><div class="rows"><span>'+value.batch+'</span> <span>'+value.sem+' - sem</span></div></div></div>';
				$('#leader-board-base').append(html);

			});


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
		}
	}



	app.init();





});