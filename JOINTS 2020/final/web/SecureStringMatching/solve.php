<?php
$string1 = hash_hmac('sha256',array(1),'asdas');
$sign=md5($string1);
$nonce=substr($sign,0,24);
$key=substr($sign,0,32);
$string1=sodium_crypto_secretbox($string1, $nonce,$key );
echo "string1 => array representation \n";
echo "string2 => ".md5($string1)."\n";
?>