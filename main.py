def titre():
    print("Vous êtes",detective["nom"], ", votre objectif est de découvrir la vérité derrière la disparition des trésors du louvre.")



def main():
    nom_saisi = ""
    detective = {
        "nom": nom_saisi,
        "chapitre": 1,
        "score": 0,
        "suspects_identifies": [],
        "indices_trouves": []
    }

    nom_saisi = input("Saisir le nom du detective : ")

main()
titre()