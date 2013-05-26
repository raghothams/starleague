<!DOCTYPE html>
<html>
	<head>
		<title>Star League</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<!-- Bootstrap -->
		<link href='http://fonts.googleapis.com/css?family=Noto+Sans|Noto+Serif' rel='stylesheet' type='text/css'>
    	<link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    	<link href="/static/css/bootstrap-responsive.min.css" rel="stylesheet">
    	<link href="/static/css/style.css" rel="stylesheet" media="screen">
    	
	</head>

	<body>
		<div class="index-header">
			<h1>Star League</h1>
		</div>
		<div id="index-base">
			<form class="form-signin" action="/login" method="post">
				<h2> Sign in</h2>
				<input type="text" name="username" class="input-block-level" id ="form-username" placeholder="Username">
				<input type="password" name="password" class="input-block-level" id ="form-password" placeholder="Password">
				<button class="btn btn-primary" type="submit">Sign in</button>
			</form>
			
			%if batch_list != None and len(batch_list) > 0:
			<div class="hero-unit" id="signup-base">
				<h1>Sign Up</h1>
				 <p>Rate your stars now!</p>

				 %if signup_errors != None and len(signup_errors) > 0:
				 	%for item in signup_errors:
				 	<div class="alert alert-error">
  						{{item}}
					</div>
					%end
				 %end
				
				<form class="form-signup" action="/signup" method="post">
					<input type="text" name="username" class="input-block-level" id ="signup-username" placeholder="Username">
					<input type="email" name="email" class="input-block-level" id ="signup-email" placeholder="Email">
						<select name="batch" id="batch">
							%for item in batch_list:
								<option value={{item["id"]}}>{{item["id"]}}</option>
							%end
						</select>
					<input type="password" name="password" class="input-block-level" id ="signup-password" placeholder="Password">
					<input type="password" name="verify" class="input-block-level" id ="signup-verify" placeholder="Password">
					<button class="btn btn-primary" type="submit">Sign up</button>
				</form>
			</div>
			%end
		</div>

		

		<script src = "/static/js/jquery.js"></script>
		<script src = "/static/js/bootstrap.min.js"></script>

	</body>

</html>