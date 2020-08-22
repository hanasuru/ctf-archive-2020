<?php require __DIR__ . '/session.php'; ?>

<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Twitter Collection</title>
    <meta name="description" content="LOL"/>
    <link href="https://fonts.googleapis.com/css?family=Arimo:400,600,700" rel="stylesheet">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link rel="shortcut icon" type="image/png" href="images/favicon.png">
    <link href="styles/main.css" rel="stylesheet">
  </head>
  <body id="top">
    <div class="page">
      <header>
        <div class="pp-header">
          <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container"><a class="navbar-brand" href="/">Twitter Collection</a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
              <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <ul class="navbar-nav ml-auto">
                  <li class="nav-item active"><a class="nav-link" href="/">Home</a>
                  </li>
                  <li class="nav-item"><a class="nav-link" href="https://cacadosman.com">About</a>
                  </li>
                  <li class="nav-item"><a class="nav-link" href="https://cacadosman.com">Blog</a>
                  </li>
                  <li class="nav-item"><a class="nav-link" href="https://cacadosman.com">Contact</a>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
        </div>
      </header>
      <div class="page-content">
        <div class="container">
<div class="container pp-section">
  <div class="row">
    <div class="col-md-9 col-sm-12 px-0">
      <h1 class="h3"> Bisa koleksi gambar dari Twitter slurr.</h1>
    </div>
    <div class="col-md-12">
      <b><p>Masukkan url gambar:</p></b>
      <p>Contoh: https://pbs.twimg.com/media/EV2FFNpUYAAFSxk?format=jpg</p>
      <input type="text" id="url">
      <button onclick="collect()" id="submit">Koleksi</button>
    </div>
  </div>
</div>
<div class="container px-0 py-4">
  <div class="pp-category-filter">
    <div class="row">
      <div class="col-sm-12"></div>
    </div>
  </div>
</div>
<div class="container px-0">
  <div class="pp-gallery">
    <div class="card-columns" id="image-columns">
    </div>
  </div>
</div>
<div class="pp-section"></div></div>
      </div>
      <footer class="pp-footer">
        <div class="container py-5">
          <div class="row text-center">
            <div class="col-md-12"><a class="pp-facebook btn btn-link" href="#"><i class="fa fa-facebook fa-2x " aria-hidden="true"></i></a><a class="pp-twitter btn btn-link " href="#"><i class="fa fa-twitter fa-2x " aria-hidden="true"></i></a><a class="pp-google-plus btn btn-link" href="#"><i class="fa fa-google-plus fa-2x" aria-hidden="true"></i></a><a class="pp-instagram btn btn-link" href="#"><i class="fa fa-instagram fa-2x " aria-hidden="true"></i></a></div>
            <div class="col-md-12">
              <p class="mt-3">Copyright &copy; Photo Perfect. All rights reserved.<br>Design - <a class="credit" href="https://templateflip.com" target="_blank">TemplateFlip</a></p>
            </div>
          </div>
        </div>
      </footer>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="scripts/main.js"></script>
    <script>

      function generate_image_html(url) {
        return `<div class="card" id="img"><a href="` + url + `">
          <figure class="pp-effect"><img class="img-fluid" src="` + url + `"/>
            <figcaption>
              <div class="h4">waifu</div>
              <p>Waifu</p>
            </figcaption>
          </figure></a>
        </div>`
      }

      function fetchData() {
        fetch('/get.php')
        .then((response) => response.json())
        .then((body) => {
          const data = body.data
          const imagesDom = document.querySelector("#image-columns")

          data.forEach((item, index) => {
            imagesDom.insertAdjacentHTML('beforeend', generate_image_html(item))
          })
        })
      }

      function collect() {
        const url = document.querySelector("#url").value
        document.querySelector("#url").disabled = true
        document.querySelector("#submit").disabled = true
        document.querySelector("#submit").innerHTML = "Mohon tunggu..."
        fetch ('/collect.php', {
          method: 'post',
          body: JSON.stringify({url: url})
        })
        .then((response) => response.json())
        .then((body) => {
          document.querySelector("#url").disabled = false
          document.querySelector("#submit").disabled = false
          document.querySelector("#submit").innerHTML = "Koleksi"
          console.log(body)
          if (body.success) {
            const data = body.data
            document.querySelectorAll("#img").forEach(e => e.parentNode.removeChild(e));
            fetchData()
            alert("sukses slurrr")
          } else {
            alert(body.message)
          }
        })
        .catch((error) => {
          document.querySelector("#url").disabled = false
          document.querySelector("#submit").disabled = false
          document.querySelector("#submit").innerHTML = "Koleksi"
          alert("something went wrong.")
          console.log(error)
        })
      }

      fetchData()
    </script>
  </body>
</html>
