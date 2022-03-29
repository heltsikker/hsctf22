<?php
function search(){
    $db_location = '/vaccine.sqlite';
    $handle = new SQLite3($db_location); 

    $resstr = "<table><thead><td>ID number</td><td>Name</td><td>Number of vaccine shots</td><td>Comment</td></thead>";
    if($result = $handle->query("SELECT * FROM vaccine WHERE idnumber = '".$_POST['idnumber']."'")){
        while($row = $result->fetchArray()){
            $resstr = $resstr."<tr><td>".$row['idnumber']."</td><td>".$row["name"]."</td><td>".$row["num"]."</td><td>".$row["comment"]."</td></tr>";
        }
    }
    $resstr = $resstr."</table>";
    return $resstr;
}

?>
<html>
<head>
<title>Vaccination record system</title>
<style>
html,body {
margin: 0;
padding: 0;
}
body {
    background-color: white;
}
#login-form {
    width: 600px;
    height: 600px;
    padding: 30px;
    box-shadow: 0 0 8px #000;
    margin: 100px auto 0 auto;
    font-family: Helvetica, sans-serif;
    background-color: #cccccc;
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
thead {
    font-weight: bold;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
</head>
<body>
<form id="login-form" action="/" method="POST">
<?php
$form = '
    <h3>Search our vaccination records</h3>
    <input type="text" name="idnumber" placeholder="Personal identification number" />
    <button type="submit">Search</button>';
if(isset($_POST["idnumber"])){
    echo search();
} else {
    echo $form;
}
?>
</form>
</body>
</html>
