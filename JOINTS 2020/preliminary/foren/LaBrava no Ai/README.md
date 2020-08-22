# La Brava no Ai
## Deskripsi
Setelah Jentoru Kriminaru menyerahkan dirinya bersama LaBrava ke pihak pahlawan setelah melawan Naruto Hijau(Deku), mereka berdua diserahkan ke pihak kepolisian. Pihak kepolisian kesulitan untuk mengetahui apa yang dibuat oleh LaBrava sebelum penangkapan, karena laptop LaBrava terjatuh dan crash. Bantulah Kepolisian kota Musutafu mencari kebenaran.
<br/>
--file integrity check--
<br/>
md5sum : b922c2507e59ffbf93a6575ae6a73833
<br/>
crc32 : 8bb47c55
## Hint
Need a little recon
## Note to panita
Gambar yang dimasukin ke deskripsi: 1.GentleLaBrava_menyerah.png 2.LaptopLabravaJatuh.png
<br/>
File soal: LaBravaLaptop.7z 
<br/>
link: https://drive.google.com/open?id=1i0MRe_xF5VPA-9YY7df4yyEh-wOdZuKT
new link: https://drive.google.com/file/d/1czdWILeXTJ8Ou8WWfSvpZe03hzVjeY6W/view?usp=sharing
<br/>
Tolong filenya ditaruh di gdrive/mega JOINTS sendiri ya, biar bulan depan bisa saia hapus. Trus peserta kalo bisa dikasih link download gdrive/mega/dropbox biar cepet, jangan pake server ctfd.
<br/>
src/ jangan dikasih
<br/>
FLAG : JOINTS20{4NaT4a_7o_n0_Om01D3} 

## How to solve
1. File extension .dmp (memdump) pakai volatility
2. untuk melihat memdump dari apa command : `vol.py -f LaBravaLaptop.dmp imageinfo`
3. untuk melihat proses yang jalan command : `vol.py -f LaBravaLaptop.dmp --profile=Win7SP1x86 pslist` \**param --profile dilihat dari image info*
4. ada notepad.exe(PID:2256) sama mspaint.exe(PID:2296 & PID:2376)
5. Dump notepad dan mspaint(\**note: mspaint boleh salah satu*) command:`vol.py -f LaBravaLaptop.dmp --profile=Win7SP1x86 memdump -p <--PID-->`
6. dari notepad atau filebesar dump bisa dilihat flagpart2 dengan `strings <filename> | grep` atau bisa nguli cari sendiri dapetnya `we_have_a_little_recon_for_you_flag_part2:_n0_Om01D3}`
7. dari mspaint dump diubah jadiin .data(rawdata: memory sampah ngikut), trus pake gimp untuk buka. Dari sini nguli nyari parameter image yang pas.
<br/><br/>
=-=Salah satu parameter GIMP yang paling enak dilihat:  =-=
<br/>
PID:`2296` imageType: `RGB`, offset: `5672395`, width: `576`, height: `323`
<br/>
PID:`2376` imageType: `RGBA`, offset:`6186972`, width: `261`, height: `66`
