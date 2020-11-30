# Fonction permettant de créer la table de fréquence
def build_Frequency_Table(text):

    frequency_table = []
    str_help = ""   #Créer un 'liste' de caractères rencontrés 

    for char in text:

        if char not in str_help:    #Si le charactère n'est pas dans la 'liste' alors on crée une liste répertoriant son code ASCII et son occurence que l'on ajoute ensuite à la table de fréquences
            str_help += char
            frequency = [ord(char), text.count(char)]
            frequency_table.append(frequency)

    return frequency_table


# Fonction permettant de créer l'arbre d'huffman
def build_Huffman_Tree_List(frequency_table):
    pass