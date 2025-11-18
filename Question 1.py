



#Liste qui définit le la message chiffrée (vide au départ)    message_chiffree = ""

#Pour chaque lettre dans le message (en minuscule)       for lettre in message.lower():
    #verifier pour chaque liste dans cle_gr3,               for i in range(len(cle_gr3)
        #Si lettre est dans l'une des listes,                   if lettre in cle_gr3[i]
            #trouve la liste spécifique qui contient la lettre, puis l'indice exacte de la lettre dans cette liste-ci.
            #ajoute +1 pour laquelle des listes contient cette lettre à l'intérieur.
            #trouve la lettre qui a cette même indice, mais avec la nouvelle liste.
            #ajouter cette lettre-ci dans la liste vide (message_chiffree)
        #Si non, ajouter cette lettre-ci dans la liste vide (message_chiffree) --> (ajoute les espaces et le point d'exclamation)

#afficher le message chiffrée           print(message_chiffree) --> le message chiffrée