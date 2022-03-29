<?php
if(!isset($_COOKIE['user'])){
    header('Location: /index.php');
    die();
}
echo 'Welcome, '.$_COOKIE['user'].'. The CMS is still under construction.<br>';
if($_COOKIE['user'] == 'admin'){
    echo 'HSCTF{a1ways_v3rify_c00kie_v@lues___}';
}
?>
