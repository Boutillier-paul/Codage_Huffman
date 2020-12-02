import codage as cod


def decode(encodeText, frequency_table):

    decodeText = ""
    code = ""

    #Recupération de l'arbre à partir de la table de fréquence triée
    tree = cod.build_Huffman_Tree(cod.build_Huffman_Tree_List(frequency_table))

    #Récupération de la table de hachage
    hachageTable = cod.getHachageTable(tree, cod.build_Huffman_Tree_List(frequency_table))

    for i in encodeText:
        code += i

        for elements in hachageTable:
            if code == elements[1]:
                decodeText+=elements[0]
                code = ""

    return decodeText