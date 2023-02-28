## EX 1: 

### Votre collègue vous donne la signature suivante :
### FONCTION estValide(var annee, var mois, var jour) : booléen
### Proposez un algorithme permettant de coder cette routine

La fonction _'estValide'_ prend en entrée une date sous forme de trois variable _'annee'_, _'mois'_, _'jour'_ et renvoie un booléen indiquant si cette date est valide ou non:

1. Si '_annee_' n'est pas un entier positif, renvoyer _'false'_. 

2. Si '_mois_' n'est pas compris entre 1 et 12 inclus, renvoyer _'false'_.

3. Si '_jour_' n'est pas compris entre 1 et 31 inclus, renvoyer _'false'_.

4. Si _'mois'_ est février(2), vérifier si _'annee'_ est bissextile en utilisant les régles suivantes: 

    - Si _'annee'_ est divisible par 4 et non par 100, ou bien divisible par 400, alors _'annee'_ est bissextile et le nombre de jours en février est de 29

    - Sinon, _'annee'_ n'est pas bissextile et le nombre de jours en février est de 28.

5. Si _'mois'_ est avril (4), juin (6), septembre (9), ou novembre (11), vérifier si _'jour'_ est compris entre 1 et 30 inclus. Si ce n'est pas le cas, renvoyer _'false'_. 

6. Sinon (c'est-à-dire si _'mois'_ est janvier (1), mars (3), mai (5), juillet (7), août (8), octobre (10), ou décembre (12)), vérifier si _'jour'_ est compris entre 1 et 31 inclus. Si ce n'est pas le cas, renvoyer _'false'_.


## CODE EN PYTHON


```
def estValide(annee, mois, jour):
    # Vérifie que l'année est positive
    if annee <= 0:
        return False
    
    # Vérifie que le mois est valide (entre 1 et 12 inclus)
    if mois < 1 or mois > 12:
        return False
    
    # Vérifie que le jour est valide (entre 1 et 31 inclus)
    if jour < 1 or jour > 31:
        return False
    
    # Vérifie les jours pour le mois de février, en fonction de l'année bissextile
    if mois == 2:
        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
            # Si l'année est bissextile, février a 29 jours au maximum
            if jour > 29:
                return False
        else:
            # Sinon, février a 28 jours au maximum
            if jour > 28:
                return False
    
    # Vérifie les jours pour les mois qui ont 30 jours
    elif mois in (4, 6, 9, 11):
        if jour > 30:
            return False
    
    # Vérifie les jours pour les mois qui ont 31 jours
    else:
        # mois == 1, 3, 5, 7, 8, 10, ou 12
        if jour > 31:
            return False
    
    # Si toutes les vérifications ont été passées, la date est valide
    return True
```


