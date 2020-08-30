#!/usr/bin/python
import random, sys
import gmpy2

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

AVAILABLE_VOUCHER = [50, 100, 200]
PRIME = 2**89 - 1

class RedeemToday:
  def __init__(self):
    self.poly = [random.randint(2, PRIME - 2) for _ in range(6)]

  def eval_at(self, x):
    y = 0
    for coef in reversed(self.poly):
      y *= x
      y += coef
      y %= PRIME
    return y

class Player:
  def __init__(self):
    self.balance = 313337
    self.hackcoin = 0
    self.codeused = []
    self.x = random.getrandbits(64)

  def buy(self, num, rt):
    if self.balance >= num * 1000:
      x = self.x
      y = rt.eval_at(x)
      code = '%s-%s-%s' % (gmpy2.digits(num, 10), gmpy2.digits(x, 62), gmpy2.digits(y, 62))
      self.balance -= num * 1000
      print '[+] Terima kasih telah membeli %d Hackcoin!' % (num)
      print '[+] Redeem Code untuk %d Hackcoin anda:' % (num)
      print '[+] %s' % (code)
      self.x = pow(self.x, 31337, PRIME)
    else:
      print '[-] Saldo anda tidak mencukupi!'

  def check(self):
    print '[+] Saldo: %d' % (self.balance)
    print '[+] Hackcoin: %d' % (self.hackcoin)

  def flaggy(self):
    if self.hackcoin >= 1337:
      self.hackcoin -= 1337
      print '[+] %s' % (open('flag.txt').read())
    else:
      print '[-] Hackcoin anda tidak mencukupi!'

  def redeem(self, code, rts):
    try:
      num, x, y = code.split('-')
      num, x, y = gmpy2.mpz(num, 10), gmpy2.mpz(x, 62), gmpy2.mpz(y, 62)
      rt = rts[AVAILABLE_VOUCHER.index(num)]
      if rt.eval_at(x) == y:
        if not x in self.codeused:
          self.codeused.append(x)
          self.hackcoin += num
          print '[+] Redeem %d Hackcoin berhasil!' % (num)
        else:
          print '[-] Redeem Code telah digunakan!'
          return
      else:
        print '[-] Redeem Code anda salah!'
    except:
      print '[!] Redeem Code anda tidak sesuai format!'

def banner():
  return '''
+--------> Welcome to RedeemToday <--------+
| $$$                                      |
|         1 hackcoin = 1000 rupiah         |
|                                      $$$ |
+------------------------------------------+

[1] buy (50, 100, 200)
[2] redeem
[3] check
[4] flag
[5] exit'''

def main():
  rts = [RedeemToday() for _ in range(3)]
  pl = Player()
  print banner()

  while True:
    opt = raw_input('\n> ').strip()
    if opt == '1' or opt == 'buy':
      num = raw_input('Nominal: ').strip()
      if num == '50':
        pl.buy(50, rts[0])
      elif num == '100':
        pl.buy(100, rts[1])
      elif num == '200':
        pl.buy(200, rts[2])
      else:
        print '[!] Nominal %s tidak tersedia' % (num)
    elif opt == '2' or opt == 'redeem':
      code = raw_input('Masukkan Redeem Code: ').strip()
      pl.redeem(code, rts)
    elif opt == '3' or opt == 'check':
      pl.check()
    elif opt == '4' or opt == 'flag':
      pl.flaggy()
    elif opt == '5' or opt == 'exit':
      exit()
    else:
      print '[!] Perintah %s tidak tersedia' % (opt)

if __name__ == '__main__':
  main()
