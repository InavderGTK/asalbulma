s = int(input("Başlangıç sayısı: "))
f = 0
i = 2

while i <= s / 2:
  if s % i == 0:
    f = 1
    add = False

  i = i + 1
  if f == 0:
    print(str(s) + " asal sayıdır")
    add = True
  else:
    add = True

  while add:
    s + 1
    add = False
