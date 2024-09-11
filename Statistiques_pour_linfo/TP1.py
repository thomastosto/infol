# Prenom : Tata  
# NumTel : 04 45 34 35 34  
# Age: 24  
# Mail : Toto@hotmail.com 
# Adresse : 15 rue Marcel Garnier, 51100 Reims
# def main():
#     nom=input("Nom : ")
#     prenom=input("prenom : ")
#     numtel=input("NumTel : ")
#     age=input("Age : ")
#     mail=input("Mail : ")
#     adresse=input("Adresse : ")
#     message="""
#     nom=%s
#     prenom=%s
#     numtel=%s
#     age=%s
#     mail=%s
#     adresse=%s
#     """%(nom,prenom,numtel,age,mail,adresse)
#     print(message)
# main()
# ---------------------------------------------------
# for i in range(21):
#     if(i>0 and i<10):
#         print(f"000{i}")
#     elif(i):
#         print(f"00{i}")
# -----------------------------------------
# from math import pi
# nb=int(input("rentez le nombre de décimal de pi  voulu\n"))
#     # pie=str(pi)
#     # for i in range(nb+2):
#     #     print(pie[i])
#     # chiffre=math.pi.nbf
# print(round(pi,nb))
#-----------------------------------------------
# chaine=input("rentrez un chiffre\n")
# liste=[0]
# for i in range(10):
#     # liste[i]=chaine.count(str(i))
#     print("Chiffre\tNombre_Occurences ")
#     print(f"{i}\t {chaine.count(str(i))}")
# #!!!! Sauf qu'il fallait utiliser la methode format()
#----------------------------------------------
# import math

# valeurs=[]
# # valeurs.append(0)
# nb=int(input("rentrez une nombre de valeurs à mettre\n"))
# for i in range(nb):
#     valeurs.append(int(input("rentrez plusieurs valeurs mettez x pour finir la saisie \n")))
# print(f"le maximum de votre liste est {max(valeurs)}\n")
# print(f"le minimum de votre liste est {min(valeurs)}\n")

#----------------------------------------------
# [0-2] : Crèche, [3-5] : Maternelle, [6-10] :
# Élémentaire, [11-14] : Collège, [15-17] : Lycée , [18-25] : Université
# age=-1
# message="rien"
# while age<0 or age>25:
#     age=int(input("saisissez votre age entre 0 et 25\n"))
# if(age>17):
#     message="Université"
#     print(message)

# elif(age>15):
#     message="Lycée"
#     print(message)

# elif(age>11):
#     message="Collège"
#     print(message)
# elif(age>6):
#     message="Elementaire"
#     print(message)
# elif(age>3):
#     message="Maternelle"
#     print(message)
# else:
#     message="Creche"
#     print(message)
#-----------------------------------------------------
#nombre de lettres dans un mot
# alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ch=input("Rentrez un mot\n")
# cmpt=0
# for car in ch:
#     if car in alph:
#         cmpt+=1
# print(f"Le mot que vous avez rentré est {ch} et a {cmpt} lettre(s)")
#-------------------------------------------------------------------------
#inverser une chaine de caractères
ch=input("Rentrez un mot\n")
cmpt=len(ch)
tp=("")
ch2=ch.join(tp)
# print(f"Le mot que vous avez rentré est {ch} et a {cmpt} lettre(s)")
for car in ch[:cmpt]:
    print(f"{ch}")