{% extends "base.html" %}
{% block content %}
<?php
session_start();
if (isset($_SESSION['username'])) {
    header("location:../index.php");
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Staff Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="../css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="../css/main.css" rel="stylesheet" media="screen">
  </head>

  <body>
  	<fieldset>
  		<legend>Clinician Login</legend>
	  	<div class="container">

	      <form class="form-signin" name="form1" method="post" action="home.php">
	        <!-- <h2 class="form-signin-heading">Clinician Login</h2><br> -->
	        <input name="myusername" id="myusername" type="text" class="form-control" placeholder="Username" autofocus>
	        <br><br>
	        <input name="mypassword" id="mypassword" type="password" class="form-control" placeholder="Password"><br>
	        <!-- The checkbox remember me is not implemented yet...
	        <label class="checkbox">
	          <input type="checkbox" value="remember-me"> Remember me
	        </label>
	        -->
	        <button><a href="dashboard/managePatient" name="Submit" id="submit" class="btn btn-lg btn-primary btn-block" type="submit">Login</a></button>
		    <!-- <a href="signup.php" name="Sign Up" id="signup" class="btn btn-lg btn-primary btn-block" type="submit">Create new account</a><br><br> -->

	        <div id="message"></div>
	      </form>

	    </div> <!-- /container -->
    </fieldset>
    

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-2.2.4.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script type="text/javascript" src="js/bootstrap.js"></script>
    <!-- The AJAX login script -->
    <script src="js/login.js"></script>

  </body>
</html>
<!-- <body>
	<h1>Welcome {{user}}</h1>
		<form method="POST" action="" style="">
			{% csrf_token %}
			{{ login.as_p }}
			<input type="Submit" name="Login" value="Submit">
		</form>
</body>	 -->
{% endblock %}	