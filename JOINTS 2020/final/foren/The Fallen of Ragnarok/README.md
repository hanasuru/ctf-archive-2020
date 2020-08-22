## The Fallen of Ragnarok

### Description

>In order to stop Dr. Weil ultimate weapon, Zero sacrificed his life to take down the Ragnarok. He knew that he had no chance to return safely. Thus, he left his final message to Ciel before the Ragnarok final explosion.

### Proof-of-concept
  1. Static analysis on:
  -  `zero.pcap`, found a bunch of `ICMP.stream`
  - `request.exe`, found a broken linkage of python dependencies

  2. We assumed that, the user run the `request.exe`, to generate ICMP traffic of `zero.pcap`. So that, we need to decompile the `python executable` with `pyinstxtractor` in order to see the `source code`

  3. From the `decompiled source code`, found:
  - AES key, `CTF_JOINTS_2020!`
  - File transmission of `flag.png`. Foreach 256 bytes, there'll be a `truncation` contained `icmp.data` of `crypt- + iv + encrypted-byte`
  - Additionally, we found out that the bytes're saved in `tree-alike` structure

  4. Based on 3rd step, extract `icmp.data` with corresponding `AES key` and its `iv`. Then, remap based on rule (odd occurence : FIFO, even occurence : LIFO)

  5. Got decrypted `flag.png`, contained flag