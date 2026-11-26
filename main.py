import time
def txt_im(x):
    y = x.split(" ")
    for i in range(len(y)):
        if y[i] == ".":
            print(y[i], end=" ")
            time.sleep(1.2)
        else:
            print(y[i], end=" ")
            time.sleep(0.3)


def titre():
    texte = "Votre objectif est de découvrir la vérité derrière la disparition des trésors du louvre . Interroger les visiteurs et les employés afin de découvrir un potentiel coupable derrière cette disparition ."
    texteIm = texte.split(" ")
    for i in range(len(texteIm)):
        if texteIm[i] == ".":
            print(texteIm[i])
            time.sleep(1.2)
        else:
            print(texteIm[i], end=" ")
            time.sleep(0.3)

def main():
    nom_saisi=""
    while nom_saisi=="":
        nom_saisi = input("Saisir le nom du detective : ")
    detective = {
        "nom": nom_saisi,
        "chapitre": 1,
        "score": 0,
        "suspects_identifies": [],
        "indices_trouves": []
    }
    titre()
    txt = "Lancement de l'enquête . . ."
    print("")
    txt_im(txt)

if __name__=='__main__':
    main()

