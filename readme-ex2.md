# EX 2: Comparaison de dates


#### Votre collègue vous donne la signature suivante :
#### FONCTION estAvant(var annee1, var mois1, var jour1, var
#### annee2, var mois2, var jour2) : entier
#### Cette routine doit renvoyer -1 si la date1 est avant la date 2,
#### 0 si ce sont les mêmes dates, et 1 si date1 est après date2.
#### Proposez un algorithme permettant de coder cette routine.

Si annee1 < annee2 
OU (annee1 = annee2 ET mois1 < mois2) 
OU (annee1 = annee2 ET mois1 = mois2 
ET jour1 < jour2) 
alors
renvoyer -1

Si annee1 = annee2 
ET mois1 = mois2 
ET jour1 = jour2 alors
renvoyer 0
Sinon, renvoyer 1


```
def estAvant(annee1, mois1, jour1, annee2, mois2, jour2):
    if (annee1 < annee2) or (annee1 == annee2 and mois1 < mois2) or (annee1 == annee2 and mois1 == mois2 and jour1 < jour2):
        return -1
    elif annee1 == annee2 and mois1 == mois2 and jour1 == jour2:
        return 0
    else:
        return 1
```
