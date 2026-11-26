from utils import *
import json
def lire_personnage(x):
    with open(chemin(x), "r" ,encoding= "utf-8") as f1:
        t1 = ()
        t2 = []
        l=json.load(f1)
        f1.close()
        for i in range(len(l)):
            t1 =(l[i]["code"], l[i]['nom'],l[i]['role'])
            t2.append(t1)
        return tuple(t2)

visiteurs = lire_personnage("visiteurs.json")
employes = lire_personnage("employes.json")

print(visiteurs)
print(employes)
l = []
h = []
for i in range(len(visiteurs)):
    l.append(visiteurs[i][1])
    h.append(visiteurs[i][0])
print(l)
print(h)

g = []
m = []
for j in range(len(employes)):
    g.append(employes[j][0])
    m.append(employes[j][1])
print(g)
print(m)


