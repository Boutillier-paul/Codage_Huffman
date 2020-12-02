import Node as nd


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


# Fonction permettant d'ajouter un noeud à une liste par ordre croissant de fréquences
def sortedAdd(node, tree):

    for nodes in tree:

        if type(nodes) is nd.Node:
            if node.frequency <= nodes.frequency:
                tree.insert(tree.index(nodes),node)
                break
            if node.frequency > nodes.frequency and tree.index(nodes) == len(tree)-1:
                tree.append(node)
                break

        else:
            if node.frequency <= nodes[1]:
                tree.insert(tree.index(nodes),node)
                break
            if node.frequency > nodes[1] and tree.index(nodes) == len(tree)-1:
                tree.append(node)
                break


# Fonction permettant de créer l'arbre d'Huffman
def build_Huffman_Tree(frequency_table):
    # Copie de la table de fréquences
    tree = frequency_table

    # On boucle tant que l'arbre ne contient pas qu'un seul élément, qui sera un noeud
    while len(tree)>1:

        # Création des noeuds et de leurs feuilles
        n = nd.Node(getCaractQuelconque())
        n.createLeaves(tree[0], tree[1])

        # Ajout par ordre croissant de fréquence des noeuds dans l'arbre
        sortedAdd(n, tree)

        # Suppresion des élélements insérés dans les feuilles du noeud
        tree.pop(0)
        tree.pop(0)

    return tree


# Table de hachage permettant d'avoir en un appel, le code correspondant à un caracètre
def get_Dict_Huffman(tree, char_code):

    pass



