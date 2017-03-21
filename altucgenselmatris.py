#!/usr/bin/python3
# -*- coding: utf-8 -*-

dosya=open("katsayilar.txt")
matris = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    matris.append(line)
dosya.close()
boyut = len(matris)
for n in range(boyut):
        kat = int(matris[n][n])
        for m in range(boyut+1):
           if kat!=0:
                matris[n][m]=int(matris[n][m])/kat
        for p in range(1,boyut-n):
            kat = float(matris[n+p][n])
            for q in range(boyut+1):
                if matris[n][n]!=0:
                      matris[n+p][q]=float(matris[n+p][q])-float(matris[n][q])*(kat/float(matris[n][n]))
        for t in range(1,boyut-n):
            kat=float(matris[n+t][t])
            for b in range(1,boyut+1):
                if matris[n][n]!=0:
                    matris[n][b]=float(matris[n][b])-float(matris[n][b])*(kat/float(matris[n][n]))
            for k in range(1,boyut-1):
                if matris[n][n]!=0:
                    matris[k][2]=float(matris[k][2])-float(matris[k][2])*(kat/float(matris[n][n]))
        
print(matris)

