from math import *
katsayilar=[1.0,-7.0,-3.0,79.0,-46.0,-120.0]
print(katsayilar)
yeni=[]
def f(x):
    fonk=0
    for i in range(len(katsayilar)):
        fonk=fonk+katsayilar[i]*pow(x,len(katsayilar)-i)
    return(fonk)
def fi(x):
    fonk1=0
    for i in range(len(katsayilar)-1):
        fonk1=fonk1+katsayilar[i]*(len(katsayilar)-i-1)*pow(x,len(katsayilar)-i-1)
    return(fonk1)

def kok(x):
    for i in range(100):
      if fi(x)!=0:
          x=x-f(x)/fi(x)
    return(x)
xi=float(input("bir baslangic degeri girin:"))
while(len(katsayilar)!=2):
            k=kok(xi)
            xi=k
            yeni.append(k)
            for j in range(len(katsayilar)):
                if(j==0):
                        continue
                katsayilar[j]=k*(katsayilar[j-1])+katsayilar[j]
            katsayilar=katsayilar[:len(katsayilar)-1]
            if(len(katsayilar)==2):
                t=-katsayilar[1]/katsayilar[0]
                yeni.append(t)
            print(yeni)            

for i in range(5):
    print("%d. kok="%(i+1),yeni[i])

