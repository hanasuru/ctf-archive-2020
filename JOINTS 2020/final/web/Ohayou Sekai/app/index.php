<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ohayou Sekai</title>
</head>
<body>
    <h1>Ohayou Sekai</h1>
    <p>Say whatever you want using bash command :)</p>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" name="upload" value="upload sh file">
    </form>
    <br>
    <p><a href="/example">Download example file</a></p>
</body>
</html>