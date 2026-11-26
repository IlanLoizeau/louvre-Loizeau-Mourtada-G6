import json
def chemin(nom):
    return f"data/{nom}"

def charger_fichier(nom):
    with open(chemin(nom), 'r', encoding = "utf-8") as f:
        dico = json.load(f)
    return dico

def ecrire_json(donnees, nom):
    with open(chemin(nom), "w", encoding= "utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent = 4)

def noter_au_journal(message):
    with open(chemin("journal_enquete.txt"), "a") as f:
        f.write(message)

def remplacer_rapport(contenu):
    with open("rapport_final.txt", "w") as f:
        f.write(contenu)

def trier(scores):
    new = []
    for i, j in scores.items():
        new.append((i, j))
    for i in range(len(new)):
        for j in range(i+1, len(new)):
            if new[i][1] < new[j][1]:
                new[i], new[j] = new[j], new[i]

