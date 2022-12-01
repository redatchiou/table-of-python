#exo_1
"""tab=[]
for i in range(10):
    a = int(input("Entrez un nombre: "))
    tab.append(a)
print(tab)
tab.reverse()
print(tab)

#exo_2
tab=[]
s=0
for i in range(10):
    a = int(input("Entrez un nombre: "))
    tab.append(a)
    s=s+a
cpt = 0
moy = s/10
print("moy est",moy)
for i in tab:
    if i>moy:
        cpt+=1
print("le nombre des notes sepurier a la moy est: ",cpt)

#exo_3
tab=[]
s=0
for i in range(10):
    a = int(input("Entrez un nombre: "))
    tab.append(a)
    s=s+a
cpt = 0
moy = s/10
min=tab[0];max =tab[0]
for i in tab:
    if min>i:
        min=i
    if max<i:
        max=i
print("moyenne est",moy,"La valeur minimale est: ",min,"La valeur maximal est est",max)
#exo_4
tab=[]
s=0
for i in range(10):
    a = int(input("Entrez un nombre: "))
    tab.append(a)
    s=s+a
cpt = 0
moy = s/10
min=tab[0];max =tab[0];imax=0;imin=0
for i in tab:
    if min>i:
        min=i
        imin =i
    if max<i:
        max=i
        imax=i
print("moyenne est",moy,"La valeur minimale est: ",min,"sa positionest",imin,"La valeur maximal est est",max,"sa positionest",imax)

#exo_5
tab=[]
cpt = 0
n = int(input("Entrez un valeur: "))
for i in range(10):
    a = int(input("Entrez un nombre: "))
    tab.append(a)
    if n==a:
        cpt+=1

print(n,"a repete ",cpt,"fois")

#exo_6 deja fait

#exo_7
T=[]
TPOS =[]
TNEG=[]
n = int(input("Entrez un VAL: "))
for i in range(n):
    a = int(input("Entrez un nombre: "))
    T.append(a)
    if a>0:
        TPOS.append(a)
    else:
        TNEG.append(a)

print(T)
print(TNEG)
print(TPOS)"""

#exo_8
V=[]
U=[]
s=0
n = int(input("Entrez la dimention: "))
for i in range(n):
    v = int(input("Entrez un v: "))
    u = int(input("Entrez un u: "))
    V.append(v)
    U.append(u)
    s=s+(u*v)
print("La produit scalaire est: ",s)

#Correction du classroom

#exo1
"""
t=[]
for i in range(10):
    a=int(input("Entrez un entier : "))
    t.append(a)
print(t)

for i in range(9,-1,-1):
    print(t[i],end="\t")

#exo2-3

s=0
t=[]
cpt=0
for i in range(10):
    a=float(input("Entrez une note : "))
    t.append(a)
    s+=a
print(t)
moy=s/10
print("La moyenne des notes est:",moy)
print("le max est :",max(t))
print("le min est :",min(t))
for elt in t:
    if elt>=moy:
        cpt+=1
print("Le nombre des notes sup à la moyenne est :",cpt)

#exo4

t=[]
for i in range(10):
    a=float(input("Entrez une valeur : "))
    t.append(a)
min=t[0]
max=t[0]
imin=0
imax=0
for i in range(10):
    if max<t[i]:
        max=t[i]
        imax=i
    if min>t[i]:
        min=t[i]
        imin=i
print("Le max est :",max, "son indice est : ", imax,"Le min est :",min,"son indice:",imin)


#exo 5

val=float(input("Entrez une valeur : "))
cpt=0
t=[]
for i in range(10):
    a=float(input("Entrez une v : "))
    t.append(a)

for i in range(10):
    if val==t[i]:
        cpt+=1
print(val,"se répète ",cpt,"fois")

# exo 6
t=[]
for i in range(10):
    a=float(input("Entrez une v : "))
    t.append(a)
print(t)
t.reverse()
print(t)

for i in range((len(t)-1)//2):
    temp=t[i]
    t[i]=t[len(t)-1-i]
    t[len(t)-1-i]=temp

print(t)

# exo7
tpos=[]
tneg=[]
t=[]
for i in range(10):
    a=float(input("Entrez une v : "))
    t.append(a)

for elt in t:
    if elt>0:
        tpos.append(elt)
    elif elt<0:
        tneg.append(elt)
print(tpos)
print(tneg)
"""
# exo 8
u=[]
v=[]
ps=0
n=int(input("Entrez n : "))
for i in range(n):
    a=float(input("Entrez pour u : "))
    u.append(a)
    b=float(input("Entrez pour v : "))
    v.append(b)

for i in range(n):
    ps+=u[i]*v[i]
print("le produit scalaire est :",ps)


