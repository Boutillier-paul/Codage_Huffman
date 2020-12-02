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


# Fonction permettant d'ajouter un noeud à une liste (de noeud ou d'autre liste) par ordre croissant de fréquences
def sortedAdd(node, tree):

    for nodes in tree:

        # Si l'élément est un noeud
        if type(nodes) is nd.Node:
            if node.frequency <= nodes.frequency:
                tree.insert(tree.index(nodes),node)
                break
            # Si l'élément à une fréquence inférieure au noeud et que cet élément est dernier alors on ajoute simplement le noeud à la fin de la liste
            if node.frequency > nodes.frequency and tree.index(nodes) == len(tree)-1:
                tree.append(node)
                break

        # Si l'élément n'est pas un noeud
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

    # On boucle tant que l'arbre ne contient pas qu'un seul élément, qui sera le noeud racine
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


# Permettant d'avoir en un appel, le code correspondant à un caracètre
def get_Dict_Huffman(tree, char_code):

    leaves_list = nd.leaves_list
    code = ""

    # On récupère les données dans la liste des feuilles
    isLeftOrRight, leaf = getFromLeavesList(leaves_list, char_code)
    code += str(isLeftOrRight)

    while leaf.frequency != tree[0].frequency:

        parentLeaf = leaf.parent

        if parentLeaf.left == leaf:
            code += str(0)
        else:
            code += str(1)

        leaf = parentLeaf

    # On renvoie la chaine de caractère inversée car on est parti de la feuille pour remonter à la racine
    return code[len(code)::-1]


# Permet de trouver un caractère dans la liste des feuilles, retourne la feuille concernée et s'il est a gauche (0) ou à droite (1) de celle-ci
def getFromLeavesList(leaves_list, char_code):

    for leaf in leaves_list:
        if not type(leaf.left) is nd.Node:

            if leaf.left[0] == char_code:
                return 0, leaf

        if not type(leaf.right) is nd.Node:

            if leaf.right[0] == char_code:
                return 1, leaf


# Permet d'afficher l'arbre d'Huffman
def print_Huffman(tree, frequency_table):

    tree_to_print = ""

    for elements in frequency_table:
        tree_to_print += "("+chr(elements[0])+","+str(elements[1])+") : "+get_Dict_Huffman(tree, elements[0])+"\n"

    print(tree_to_print)


# Code la chaine de caractère passé en paramètre
def encode_Text(text, tree):

    encodeText = ""

    for char in text:
        encodeText += get_Dict_Huffman(tree, ord(char))

    return encodeText


# Permet d'obtenir la table de hachage (un caractère et son code)
def getHachageTable(tree, frequency_table):

    table = []

    for elements in frequency_table:
        table.append([chr(elements[0]),get_Dict_Huffman(tree, elements[0])])

    return table