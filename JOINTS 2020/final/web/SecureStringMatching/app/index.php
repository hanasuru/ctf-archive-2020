<?
include "secret.php";

header("Debug: ?debug=v");

if (isset($_GET["debug"])) {
    show_source(__FILE__);
}else{
    
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>String Matching</title>
</head>

<body>
    <center>
        <h1>Secure String Matching</h1>
        <form action="" method="POST">
            String1: <input type="text" name="string1"> <br> <br>
            String2: <input type="text" name="string2"> <br>
            <br>
            <button type="submit" name="submit"> Submit</button>
        </form>
    </center>
    <?

    if (!empty($_POST["string1"]) || !empty($_POST["string2"])) {

        $xxx = $_POST["string1"];
        $yyy = $_POST["string2"];

        if ($xxx === $yyy) {
            echo "<center> <p>Match bosqquee!!</p> </center>";
        } else {
            $key=$xxx;
            $key = hash_hmac('sha256',$key,$secret);
            $sign=md5($key);
            $nonce=substr($sign,0,24);
            $key=substr($sign,0,32);
            $string1=sodium_crypto_secretbox($string1, $nonce,$key );
            if (md5($string1) === $yyy) {
                echo "<center> $flag </center>";
            } else {
                echo "<center> Nope </center>";;
            }
        }
    }

    ?>
</body>

</html>