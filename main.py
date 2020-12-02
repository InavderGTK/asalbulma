s = float(input("Sayı girin: "))  
f = 0
i = 2
while i <= s / 2:
    if s == 1:
      print("error")
      quit()
    
    if s % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("Asal Sayıdır")
else:
    print("Asal Sayı Değildir")
