<!DOCTYPE html>
<html>
	<head>
		<title>Star League</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<!-- Bootstrap -->
		<!-- <link href='http://fonts.googleapis.com/css?family=Noto+Sans|Noto+Serif' rel='stylesheet' type='text/css'> -->
    	<link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    	<link href="/static/css/bootstrap-responsive.min.css" rel="stylesheet">
    	<link href="/static/css/style.css" rel="stylesheet" media="screen">
    	
	</head>

	<body>
		
			<div class="page-header">
				<div class="head-colors"></div>
				<h1>Star League</h1>
				<div class="head-colors"></div>
			</div>
			<div class="container">
				<ul class="nav nav-pills tabs">
					<li class="active">
		    			<a id="tab-leader-board" href="#">Leader Board</a>
		  			</li>
		  			<li >
		    			<a id="tab-rate-now" href="#">Rate Now</a>
		  			</li>
		  			<li class="pull-right">
		    			<a id="tab-logout" href="/logout">Logout</a>
		  			</li>
				</ul>

				<div class="span12 base" >
					<!-- base container -->
					<div class="span1"></div>
					<div class="span10" id="leader-board-base"><!-- <div class = "span4">
								<div class="well cards">
									<h2>SUBJECT NAME</h2>
									<div class="rows">Faculty Name Is Always Big</div>
									<div class="rows"><span class="icon-star"></span><span class="icon-star"></span></div>
									<div class="rows"><span>2010-2014</span><span>6 - sem</span></div>
								</div>
							</div> --></div>

							
					<div class="span10" id="rate-now">
						<ul class="nav nav-tabs nav-stacked" id="subject-list">
							<!-- <li><a href="#">subj1</a></li>
							<li><a href="#">subj1</a></li>
							<li><a href="#">subj1</a></li> -->
						</ul>

						<div class="well">
							<form id="form-rate">
								<h2 id="subject-name-lbl"></h2>
								<p id="faculty-lbl"></p>
								<input type="text" class="input-block-level" id ="form-date" placeholder="Date dd/mm/yyyy">
								<!-- <input type="range" class="input-block-level" id ="form-star" placeholder="Star"> -->
								<select name="ratelist" form="form-rate" id="form-star">
								  <option value=1>1</option>
								  <option value=2>2</option>
								  <option value=3>3</option>
								  <option value=4>4</option>
								  <option value=5>5</option>
								</select>
								<!-- <button class="btn btn-primary" id="btn-rate" type="button">Rate</button> -->
								<input type="button" class="btn btn-primary" value="Rate" id="btn-rate">
							</form>
						</div>
						<div id="msg-container"></div>
					</div>	
				</div>
			</div>
			
		


		<!-- <div id="footer">
			<div class="foot-design"></div>
			<div class="foot-content">lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum</div>
			<div class="foot-design"></div>
		</div> -->


		<script src = "/static/js/jquery.js"></script>
		<script src = "/static/js/bootstrap.min.js"></script>
		<script src = "/static/js/app.js"></script>

	</body>

</html>