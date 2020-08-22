## A pleasant new game

### Description

>Sebuah agensi menerima **S-Rank Quest** dari client bernama Regigigas. Dalam permintaannya, Regigigas menyebutkan bahwa ia membutuhkan seseorang yang mampu memecahkan kode pada monolit dengan beberapa bekas kerusakan

### Proof-of-concept
  1. Static analysis on `QUEST.png`, found:
  
   - Objective to `decipher braille`
   - Another `PNG file` at the trailer of file. For now, we called this `braille.png`

  2. Hierarchical analysis on `braille.png`, found:
  
   - 1st frame of braille code
   - APNG file structure, identified by `acTL`, `fcTL`, and `fdAT` chunk. But there're discrepancy on `sequence number`

  3. Based on the circumstances, do file recovery by re-mapping the `fcTL` and `fdAT` block, so that the `sequence number` are properly sorted.

  4. Dump each PNG frame from `repaired APNG file` using either `Apngdis` or your own script 

  5. Foreach png frame contained `braille code`, do braille decipher

  6. Found a deciphered message:

  ```
Dear challenger,

If you see this message, it means the code has been succesfully deciphered.
As a token of my gratitude, hence I will grant you a honorable reward for your greatest accomplishment 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
** JOINTS20{1_w0nd3r_1f_th3r3_1s_4_tr3asure_b3h1nd_th3_r4inbow} **
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Master of Legendary Titans

Regigigas

```