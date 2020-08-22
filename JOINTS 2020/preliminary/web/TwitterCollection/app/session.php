<?php
        session_start();
        if (!isset($_SESSION['id'])) {
            $id = sha1(rand() . rand());
            $_SESSION['id'] = $id;
        }

        $id = $_SESSION['id'];

        $folder = __DIR__ . '/downloads/' . $id;
        if (!file_exists($folder)) {
            mkdir($folder, 0777, true);
        }
    ?>