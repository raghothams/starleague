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
				url:'http://localhost:8082/app/leaderboard',
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
		}
	}



	app.init();





});