def estAvant():
    while True:
        print("Veuillez entrer les dates que vous souhaitez comparer sous forme de AAAA-MM-JJ.")
        date1 = input("Entrez la première date : ")
        date2 = input("Entrez la deuxième date : ")

        try:
            annee1, mois1, jour1 = map(int, date1.split("-"))
            annee2, mois2, jour2 = map(int, date2.split("-"))
            break
        except ValueError:
            print("Les dates entrées sont incorrectes. Veuillez les entrer à nouveau.")

    if (annee1 < annee2) or (annee1 == annee2 and mois1 < mois2) or (annee1 == annee2 and mois1 == mois2 and jour1 < jour2):
        return -1
    elif annee1 == annee2 and mois1 == mois2 and jour1 == jour2:
        return 0
    else:
        return 1