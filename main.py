def titre():
    nom = detective["nom"]
    print("Vous êtes",nom,"votre objectif est de découvrir la vérité derrière la disparition des trésors du louvre.")



def main():
    nom_saisi = input("Saisir le nom du detective : ")
    return nom_saisi

nom_saisi = main()
detective = {
    "nom": nom_saisi,
    "chapitre": 1,
    "score": 0,
    "suspects_identifies": [],
    "indices_trouves": []
}

titre()

