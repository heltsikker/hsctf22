<?php
if(isset($_POST["username"])){
    if($_POST["username"] == "guest"){
        setCookie('user','guest', time() + 86400, "/");
        header('Location: /cms.php');
        die();
    }
}
?>
<html>
<head>
<title>Girl Scout Cookies</title>
<style>
html,body {
margin: 0;
padding: 0;
}
body {
    background-image: url('cookies.jpg');
    background-repeat: repeat;
}
h1 {
    font-size: 100px;
    text-align: center;
    margin-top: 50px;
    text-shadow: 3px 3px 0px #FFF;
}
#login-form {
    width: 300px;
    height: 300px;
    padding: 30px;
    box-shadow: 0 0 8px #000;
    margin: 100px auto 0 auto;
    font-family: Helvetica, sans-serif;
    background-color: white;
}
#login-form input {
    width: 100%;
    margin-bottom: 20px;
}
#login-form button {
    width: 100%;
    padding: 5px;
    background-color: #333;
    color: #ccc;
}
</style>
</head>
<body>
<h1>Girl Scout CMS</h1>
<h1 style="font-size: 50px">(Cookie Management System)</h1>
<form id="login-form" action="/" method="POST">
<?php
$form = '
    <h3>CMS Login</h3>
    <p>Login as <b>guest</b> with no password if you do not have an account</p>
    <input type="text" name="username" placeholder="Username" />
    <input type="password" name="password" placeholder="Password" />
    <button type="submit">Log in</button>';
if(isset($_POST["username"])){
    if($_POST["username"] == "guest"){
        die("That's not supposed to happen");
    } else {
        echo $form.'<span style="color:red">Wrong username or password</span>';
    }
} else {
    echo $form;
}
?>
</form>
</body>
</html>
