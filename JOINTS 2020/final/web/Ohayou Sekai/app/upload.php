<?php

if ($_POST['upload'])
{
    $file_tmp = $_FILES['file']['tmp_name'];
    $name = sha1(rand() . rand());
    if (move_uploaded_file($file_tmp, __DIR__ . '/files/' . $name))
    {
        $allowedPattern = '/#!\/bin\/sh\necho \"(\w| )+\"\nexit 0$/';
        $raw = shell_exec('cat ./files/' . $name);
        preg_match_all($allowedPattern, $raw, $matches);
        if (!count($matches)) {
            echo "HEKEL PERGI WOI";
            return;
        }

        $output = shell_exec("./files/" . $name);
        echo $output;
    }
    else
    {
        echo "GAGAL SLURRRR";
        return;
    }
}