# Fonction permettant de créer la table de fréquence
def build_Frequency_Table(text):

    frequency_table = []
    str_help = ""   #Créer un chaine de caractere constituée des caractères rencontrés 

    for char in text:

        if char not in str_help:    #Si le charactère n'est pas dans la 'str_help' alors on crée une liste répertoriant son code ASCII et son occurence que l'on ajoute ensuite à la table de fréquences
            str_help += char
            frequency = [ord(char), text.count(char)]
            frequency_table.append(frequency)

    return frequency_table


# Fonction permettant de trier la table de fréquence par ordre croisssant de fréquences
def build_Huffman_Tree_List(frequency_table):
    return sorted(frequency_table, key=lambda couple: couple[1])

# Fonction retournant un caractère quelconque
def getCaractQuelconque():
    return ";"


