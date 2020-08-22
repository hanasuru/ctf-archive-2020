<?php

header('application/json');
require __DIR__ . '/session.php';

$images = scandir($folder);

$response = [
    "success" => true,
    "data" => []
];

foreach($images as $image)
{
    if (!($image === "." || $image === ".."))
    {
        $response["data"][] = "/downloads/$id/" . $image;
    }
}

echo json_encode($response);