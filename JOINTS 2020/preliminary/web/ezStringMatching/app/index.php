<?
include "flag.php";

header("Debug: ?debug=v");

if (isset($_GET["debug"])) {
    show_source(__FILE__);
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
    <h1>String Matching</h1>
        <form action="" method="POST">
        String1:    <input type="text" name="string1"> <br> <br>
        String2:    <input type="text" name="string2"> <br>
        <br>
        <button type="submit" name="submit"> Submit</button>
        </form>
    </center>
    <?
            if (!empty($_POST["string1"]) || !empty($_POST["string2"])){
                
                $xxx=$_POST["string1"];
                $yyy=$_POST["string2"];

                if ($xxx===$yyy){
                    echo "<center> <p>Match bosqquee!!</p> </center>";
                }else{
                    if (md5($xxx) == md5($yyy)) {
                        echo "<center> $flag </center>" ;
                      }else{
                        echo "<center> <p>Not Match bosqquee!!</p> </center>";
                      }
                }            
            }    

    ?>
</body>
</html>
