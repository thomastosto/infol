# Prenom : Tata  
# NumTel : 04 45 34 35 34  
# Age: 24  
# Mail : Toto@hotmail.com 
# Adresse : 15 rue Marcel Garnier, 51100 Reims
def main():
    nom=input("Nom : ")
    prenom=input("prenom : ")
    numtel=input("NumTel : ")
    age=input("Age : ")
    mail=input("Mail : ")
    adresse=input("Adresse : ")
    message="""
    nom=%s
    prenom=%s
    numtel=%s
    age=%s
    mail=%s
    adresse=%s
    """%(nom,prenom,numtel,age,mail,adresse)
    print(message)

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
from math import min
form math import max
# max=input("rentrez une valeur ")
# min=input("rentrez une valeur minimale")
valeurs={input("rentrez plusieurs valeurs")}
