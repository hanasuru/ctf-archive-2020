## Love Discrepancy

### Description

>Ada orang berkata bahwa cinta itu adalah tanda dari sejauh apakah usaha kita untuk menemukan dua hati yang memiliki kecocokan

### Proof-of-concept
  1. Static analysis on `koi.png`, found improper PNG chunks due to discrepancy between `chunk_size` and `chunk` data. Also there's `flag` delimiter between 2 chunk

  2. Thus, we can reconstruct the given image by re-mapping the `chunk_data` based on `chunk_size`

  3. Got recovered `flag.png` contained flag
