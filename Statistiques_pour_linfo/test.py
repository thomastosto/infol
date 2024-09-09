# l=(1,2,3,4,5)

# for x in range(4):
#     print(x)
# l.append(10)
# l=[1,2,3,4,5]
# l.append(10)
# for x in range(7):
#     print(x)
# x=[3]+[4]
# print(x)
# dir(x)

# def Nom_fonction(param):
#     # desc
#     # corp
#     # retour

# #exemple

# def maxi(x):
#     max_value=max(x)
#     print("le maximum des valeurs est : " {max_value})

# maxi(x)

#--------------------------------------------------------------
#som=0
# def sum(var1, var2):
#     global som #variable global
#     som=var1+var2
#     print(som)
# sum(var1,var2)
# print(max(var1,var2))
#input #retourne une chaine de caractère
#def minmax():

#--------------------------------------------------
#le 09/09 en td de python

# def saisir():
#     # print("rentrez une valeur pour a\n")
#     a=float(input("la valeur de a\n"))
#     b=float(input("la valeur de b\n"))
#     c=float(input("la valeur de c\n"))
#     # a=float(a)
#     # b=float(b)
#     # c=float(c)
# def minmax(a,b,c):
#     min=a
#     max=a
#     # if (a>b)&(a>c):
#     #     print("le maximum est a")
#     if b<min:
#         min=b
#     else (b>max):
#         max=b
#     if c<min:
#         min=c
#     else c>max:
#         max=c
#     print("min: {min}")
#     print("min: {max}")
# saisir()
# minmax(a,b,c)

#la somme de deux entier dans une seule valeur

# a=int(input("rentrez une valeur"))
# a+=int(input("rentrez une deuxieme valeur"))
# print("le resultat est",a)

#--------------------------------------------------

# def operateur():
#     #condition=0
#     o=""
#     while o!="+" and o!="-" and o!="/" and o!="x":
#         #bloc à exécuter
#         o=str(input("rentrez une operotion +,-,/ ou x \n"))
#         # if o=="+"or o=="-" or o=="/" or o=="x":
#         #     condition=1
#         #     #break
#     a=int(input("rentrez la premiere val\n"))
#     b=int(input("rentrez la deuxième val\n"))
#     if o=="+":
#         res=a+b
#     elif o=="-":
#         res=a-b
#     elif o=="/":
#         if b==0:
#             print("erreur division par 0\n")
#         else:
#             res=a/b
#     else:
#         res=a*b       
#     # print("a"+o+"b"+"="+res)
#     # print(a,o,b,res)
# operateur()
#--------------------------------------
# sum=0
# n=0
# i=input("entrez une valeur\n")
# while i !="\n":
#     sum+=float(i)
#     n+=1
#     i=input("entrez une valeur")
# print("la moyenne :", sum/n)
# ---------------------------------------------------------------

#nombre de caractères dans une chaine de caractère

# n=0
# ch=input("Entrez une chaine\n")
# for caracter in ch:
#     n+=1
# print(n)

#------------------------------------------------

#compte le nombre de voyelle et consonnes dans une chaine

# voy="aeiuoyAEIOUY"
# ch=input("donnez une chaine de caractere\n")
# nbv=0
# for car in ch:
#     if car in voy:
#         nbv+=1
# print("le nombre de voyelles est:",nbv)

#--------------------------------------------------------

#une chaine de caractere si plus petite ou egale à 2 afficher les caracteres sinon affficher le 2 premier et dernière caractères

# ch=input("rentrez une chaine de caractere\n")
# res=""
# if len(ch)>=2:
#     res=ch[0:2]+ch[-2:]#chiffre: veut dire va jusqu' a la fin
#     #ch[0]+ch[1]+ch[-2]+ch[-1]
#     res=ch[:2]+ch[-2:]#chiffre: veut dire va jusqu' a la fin
# print(res)

#---------------------------------------------------------------

#
# ch="Nous, somme, le,lundi"
# #on veut avoir le,lundi, nous sommes
# ch=ch.lower()#enlève les majuscules
# l=ch.split()#transforme ch en liste
# l.sort()#range cette liste en ordre alph
# ch=','.join(l)
# print(ch)
# #---------------------------------------------
# #somme des éléments dans une liste
# lst=[1,2,6,5]
# a=0
# for ele in lst:
#     a+=ele
# print("la somme des elements de la listre est egale a",a)
#---------------------------------------------------------------
l=[[2,3],[5,0,-2]]
l_s=[]
    for e in l:
        l_s.append(sum(e))
        p=index(max(l_s))