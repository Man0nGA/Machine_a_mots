from random import choices

def occurrences(txt):
    occurrences = {}
    for caractere in txt:
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1
    return occurrences

def occurrences_2(txt):
    occurrences = {}
    for c1, c2 in zip(txt[:-1], txt[1:]):
        if c1 in occurrences:
            if c2 in occurrences[c1]:
                occurrences[c1][c2] += 1
            else:
                occurrences[c1][c2] = 1
        else:
            occurrences[c1] = {}
    return occurrences

def occurrences_3(txt):
    occurrences = {}
    for c1, c2, c3 in zip(txt[:-2], txt[1:-1], txt[2:]):
        if c1 in occurrences:
            if c2 in occurrences[c1]:
                if c3 in occurrences[c1][c2]:
                    occurrences[c1][c2][c3] += 1
                else:
                    occurrences[c1][c2][c3] = 1
            else:
                occurrences[c1][c2] = {}
        else:
            occurrences[c1] = {}
    return occurrences

def frequences_2(txt):
    occurrences = occurrences_2(txt)
    nombre_paires = len(txt) - 1
    for c1 in occurrences:
        for c2 in occurrences[c1]:
            occurrences[c1][c2] /= nombre_paires
    return occurrences

def frequences_3(txt):
    occurrences = occurrences_3(txt)
    nombre_triplets = len(txt) - 2
    for c1 in occurrences:
        for c2 in occurrences[c1]:
            for c3 in occurrences[c1][c2]:
                occurrences[c1][c2][c3] /= nombre_triplets
    return occurrences

def generer_mot_2(freq):
    mot = ""
    lettres_possibles = list(freq[" "].keys())
    proba = list(freq[" "].values())
    l = choices(lettres_possibles, weights=proba)[0]
    while l != " ":
        mot = mot + l
        lettres_possibles = list(freq[l].keys())
        proba = list(freq[l].values())
        l = choices(lettres_possibles, weights=proba)[0]
    return mot

def generer_mot_3(freq2, freq3):
    mot = ""
    lettres_possibles = list(freq2[" "].keys())
    proba = list(freq2[" "].values())
    l = choices(lettres_possibles, weights=proba)[0]
    while l != " ":
        mot = mot + l
        if len(mot) > 2:
            lettres_possibles = list(freq3[mot[-2]][mot[-1]].keys())
            proba = list(freq3[mot[-2]][mot[-1]].values())
            l = choices(lettres_possibles, weights=proba)[0]
        else:
            lettres_possibles = list(freq2[l].keys())
            proba = list(freq2[l].values())
            l = choices(lettres_possibles, weights=proba)[0]
    return mot

def generer_mots(txt, n):
    freq2 = frequences_2(txt)
    freq3 = frequences_3(txt)
    mots = []
    for k in range(n):
        mots.append(generer_mot_3(freq2, freq3))
    return mots

def main():
    with open("dico_fr.txt", "r") as f_dico:
        txt = f_dico.read()
        
    print(generer_mots(txt, 10))

        
if __name__ == "__main__":
    main()
        
