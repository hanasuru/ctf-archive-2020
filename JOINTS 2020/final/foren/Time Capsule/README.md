## Time Capsule

### Description

> Dalam perjalanan mencari wejangan hidup, seorang *Hikki-NEET*, sebut saja Kazuma, menemukan **Time capsule** yang dicache menggunakan CDN. Di sana, ia menemukan potongan pesan yang kabarnya merupakan peninggalan dari seorang **Damegami** sehingga wajar saja apabila pesan yang ditinggalkannya dalam keadaan yang acak-acakan.

### Proof-of-concept
  1. Static analysis  on `time-capsule.pcap`, found:

  - TCP stream, contained Sslkeylogfile
  - SSL stream, contained encrypted http traffic
  - Note that, the `relation of each packet.frame` seems like broken `as stated in challenge description`

  2. Based on the circumstances, found out that the order of each `packet.frame` aren't correct. So that, we need to find a way to reorder `packet file` chronologically by using either `reordercap` or `editcap`

  3. Decrypt SSL traffic using sslkeylogfile as an input, found

  - Http stream, contained image CDN source code
  - Http stream, contained requests of  cropping operation

  4. Based on `cropping requests`, construct a newly image based on given `offset` and `dimension`

  5. Got qr code, contained message of `JOINTS20{4r4_4r4__sUch_4_n4sty_im4g3_cdn_servic3}`