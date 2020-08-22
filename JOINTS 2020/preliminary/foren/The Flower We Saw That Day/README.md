## The Flower We Saw That Day

### Description

>It's Hide & Seek, isn't?
>If so, can you find me?

### Proof-of-concept
  1. Static analysis on:
  - `bthci.pcap`, found a file pairing between 2 hosts
  - `bthid.pcap`, found a keylogger of paired bluetooth keyboard. Here we know that the user typed `bash command` & `vim command`

  2. For `bthci.pcap`, we know that it was utilized Windows OS (identified by `RFCOMM`). Based on this, extract `bthci_acl`. Remember that foreach packet truncation, there were additional 6 bytes, so make sure to clean-up these byte. Finally, we got an encrypted `flag.zip`

  3. For `bthid.pcap`, we can directly see the `pressed-key` of `bluetooth keyboard` (thanks to bluetooth dissector). Beware that, the `vim behaviour` was a bit tricky  due to the `command mode`. Finally, we got an message of `The passphrase is bTFubmFfbTB1XzFjaDFkMF93NHN1cjNuYTFkZV9rdWQ0c2ExbmU=`

  4. Extract `flag.zip` using the password from 3rd step. Got `flag.png` contained a flag