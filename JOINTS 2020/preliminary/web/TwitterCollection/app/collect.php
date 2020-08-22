<?php

require __DIR__ . '/session.php';
header('application/json');

$response = [
    'success' => false
];

try {
    $json = json_decode(file_get_contents('php://input'), true);
} catch (Exception $e) {
    $response['message'] = "failed to parse body";
    echo json_encode($response);
    return;
}

if (isset($json['url'])) {
    $url = $json['url'];
    $urlFilter = "pbs.twimg.com";

    $blacklist =    "/[\`'\+$\&\*)(#{}\|;\[\]><\\\\]|". 
                    "php|phps|html|file:\/\/|data:\/\/|\.\.|".
                    "zip:\/\/|expect:\/\/|input:\/\/|phar:\/\//";

    if (preg_match($blacklist, strtolower($url))) {
        $response['message'] = 'Hekerrrrr';
        echo json_encode($response);
        return;
    }

    $parseUrl = parse_url($url);
    if ($parseUrl['scheme'] !== 'https') {
        $response['message'] = 'Hanya boleh https biar aman slurrr';
        echo json_encode($response);
        return;
    }
    
    if ($parseUrl['host'] !== $urlFilter) {
        $response['message'] = 'Hanya boleh url gambar dari pixiv >:(';
        echo json_encode($response);
        return;
    }

    $desc = array(
        0 => array('pipe', 'r'),
        1 => array('pipe', 'w'),
        2 => array('pipe', 'w')
    );

    $name = sha1(rand() . rand()) . '.jpg';
    $cmd = 'cd ' . $folder . ';curl --fail --silent --show-error --max-filesize 10000000 ' . ' -o ' . "\"$name\" " . "\"$url\"";

    $proc = proc_open($cmd, $desc, $pipes);

    $msg = stream_get_contents($pipes[2]);
    $msg = str_replace(" ", "", $msg);

    if ($msg !== "") {
        http_response_code(500);
        echo $msg;
        return;
    }

    $response['success'] = true;
    echo json_encode($response);
    return;
} else {
    echo json_encode($response);
    return;
}

