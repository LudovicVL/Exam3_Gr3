def decrypter_message(message: str, nb_cesar: int) -> str:
    """
    Cette fonction reçoit un mot ainsi que le nombre de rotation pour chiffrer le mot. Elle en fait le chiffrement de césar en utilisant le nombre reçu pour transformer le mot.
    :param message: Le message à décrypté
    :param nb_cesar: Le nombre de rotations à faire pour le chiffrement
    :return: Le message décrypté
    """
    caracteres_remplacement = ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz","01234567890123456789"]
    message_decrypte = ""

    #pour chaque caractères dans le message chiffré
    for i in range(len(messages_gr3["cryptes"])):
        #position = trouver caractère dans caracteres_remplacement
        position = caracteres_remplacement.index(messages_gr3["crypte"][i])
        position += nb_cesar
        message_decrypte += caracteres_remplacement[position]
    return message_decrypte


def accuse_reception(message: str) -> None:
    """
    Fonction qui utilise la fonction decrypter_message() pour decrypter le message complètement, puis en préparant un accusé-réception.
    :param message: les messages dans messages_gr3
    :return: None
    """
    liste_accuse_reception = [
        "Accusé-réception:"




    ]
    nb_cesar = 0
    j = 0
    #quand le nombre cesar est plus petit ou egale à 3:
    while nb_cesar <= 3:
        # pour chaque lettres dans les messages modifiés
        for lettre in messages_gr3["cryptes"][j]:
            decrypter_message(message, nb_cesar)
            if j == 0:
                liste_accuse_reception.append("Le 1er message a été intercepté")
            elif j == 1:
                liste_accuse_reception.append("Le 2em message a été intercepté")
            elif j == 2:
                liste_accuse_reception.append("Le 3em message a été intercepté")
        #compteur pour le nombre cesar et les messages
        nb_cesar += 1
        j += 1



if __name__ == "__main__":

    messages_gr3 = {
        "pseudo": "DebugWoman",
        "messages": ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
        "cryptes": ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
    }




