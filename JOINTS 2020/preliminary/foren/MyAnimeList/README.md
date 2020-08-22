## MyAnimeList

### Description

>Di tengah-tengah kesenjangan waktunya, seorang sysadmin menemukan sebuah log trace pada server miliknya. Di sana, ia mengetahui bahwa terdapat upaya pengaksesan dan eksploitasi sebuah web **AnimeList** pada sebuah private tunnel antara 2 buah region yang berbeda.

### Proof-of-concept
  1. Static analysis on `remote.pcapng`, found:

  -  VNC traffic
  -  Http traffic, contained `log.pcap` 

  2. For vnc traffic, run `chaosreader` to replay the `VNC session`. Based on replayed session, found out that the server used `strongswan` to setup a ipsec tunnel between 2 different server. 

  3. Based on 2nd case, we know that `log.pcap` was a captured traffic on 1st server, so that it must be contained `ESP encrypted packet`.

  4. To decrypt the packet, collect information of `spi`, `encryption key`, and `authentication key` from VNC session. Then edit the `ESP SAs` preferences

  5. After decrypted the `ESP packet`, now we can see the `Http traffic`. Here we found an `Anime search` requests, we assumed that the flag was embedded here

  6. After several inspection, found out that there're `boolean-based nosql injection`, identified by `$regex` params.

  7. Here, we assumed that the flag is `unique`, so firstly we need to find an `anime title` that has minimum `1 match` result. Found out that `Itai no wa iya nanode bougyo ryoku ni kyokufuri shitai to omoimasu` is the correct title

  8. Extract `$regex rule` that has title of `itai no wa iya nanode bougyo ryoku ni kyokufuri shitai to omoimasu`

  9. Remap `$regex rule` based on `forward` and `backward` order to get the flag