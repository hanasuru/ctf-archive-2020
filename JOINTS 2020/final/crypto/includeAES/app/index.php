<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <style>
    ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #333;
    }

    li {
      float: left;
    }

    li a {
      display: block;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }

    li a:hover {
      background-color: #111;
    }
  </style>
  <title>Joints 2020</title>
</head>

<body>
  <ul>
    <li><a class="home" href="index.php?page=0f7db51d454b811e8fa431d6dd6ae2c4774939389a02f54e4eac04f9ee86b18d1ca0c9603efc3e3b3a12dbe8b1510d91">Home</a></li>
    <li><a href="index.php?page=5c6b2fc0c643775a36d4db6b438bfbad774939389a02f54e4eac04f9ee86b18d9794bc0abe8705db81d09658ff1e0d86">Contact</a></li>
    <!-- /flag.php -->
  </ul>
  <?php
  define('access', TRUE);

  $ENCRYPTIONKEY = hex2bin("39383439346335376634343935663633");
  $IV            = hex2bin("774939389a02f54e4eac04f9ee86b18d");

  function enc($data, $key, $iv)
  {

    $encrypted = openssl_encrypt($data, 'aes-128-cbc', $key, 0, $iv);
    $encrypted = $iv . base64_decode($encrypted);
    return md5($encrypted) . bin2hex($encrypted);
  }

  function dec($encryptedData, $key, $iv)
  {
    $decrypted = openssl_decrypt(base64_encode($encryptedData), 'aes-128-cbc', $key, 0, $iv);
    return $decrypted;
  }

  function filter($param)
  {
    if (strpos($param, '.') !== false || strpos($param, ':') !== false) {
      die('hekel detected !!');
    }
    if (strpos($param, 'index') !== false) {
      include 'home.php';
    }
  }

  function pad($message)
  {
    if (strlen($message) % 8) {
      $message = str_pad(
        $message,
        strlen($message) + 8 - strlen($message) % 8,
        8 - strlen($message) % 8
      );
      return $message;
    } else {
      return $message;
    }
  }

  function unpad($message)
  {
    if (is_numeric(substr($message, -1))) {
      return str_replace(substr($message, -1), "", $message);
    } else {
      return $message;
    }
  }

  if (!empty($_GET['page'])) {

    $page = hex2bin(substr($_GET['page'], 32));
    $hash = substr($_GET['page'], 0, 32);

    if ($hash !== md5($page)) {
      die("An error occurred while verifying MD5 !!!");
    }

    $iv = substr($page, 0, 16);
    $data = substr($page, 16);

    $decData = dec($data, $ENCRYPTIONKEY, $iv);
    $decData = unpad($decData);
    filter($decData);

    if ((@include "./" . $decData . ".php") === false) {
      echo "An error occurred while including  " . $decData;
    }
  } else {
    include 'home.php';
  }

  ?>
</body>

</html>