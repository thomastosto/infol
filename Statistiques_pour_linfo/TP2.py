# Une enquête a été menée auprès de 100 étudiants concernant leur moyen de transport 
# principal pour se rendre à l’université. Les réponses sont les suivantes : 
# a. Voiture 
# b. Transport en commun  
# c. Vélo  
# d. Moto 
# e. Trottinette 
# f. 
# À pied  
# 1. Créer un tuple nommé « modalites » pour stocker ces modalités. 
import random


modalites=("Voiture","Moto","Velo","transport en commun","trottinette","A pied")
# mod=list(modalites)
# liste[100]
# for i in liste:
#     liste[i]=weigth.random.choices(liste)
N=100
echantillon=random.choices(modalites,weights=[1,4,5,6,1,3])