import lectureJson as lj
import codage as cod
import decodage as dec
import Node as nd


if __name__ == "__main__":

    cheminTEXT = "text.json"
    cheminTEXTOUT = "out-text.json"

    # Lecture du text à encoder dans le fichier json text.json
    x = lj.read(cheminTEXT, "text")
    print("Texte à encoder :", x, "\n")

    table = cod.build_Frequency_Table(x)    # Création de la table de fréquence
    lj.write(cheminTEXTOUT, "table", table) # Ecriture de la table de fréquence dans le fichier json out-text.json

    tree = cod.build_Huffman_Tree(cod.build_Huffman_Tree_List(table)) # Création de l'arbre d'Huffman (à partir de la table de fréquence triée)
    #cod.print_Huffman(tree, cod.build_Huffman_Tree_List(table)) # Affiche l'arbre d'Huffman

    encodeText = cod.encode_Text(x, tree)
    print("Texte encodé :", encodeText, "\n") # Affiche le texte encodé
    lj.write(cheminTEXTOUT, "encodeText", encodeText) # Insère le texte encodé dans le fichier json

    decodeText = dec.decode(encodeText, table) # Decode le texte
    print("Texte décodé :", decodeText, "\n") # Affiche le texte décodé
    lj.write(cheminTEXTOUT, "decodeText", decodeText) # Insère le texte décodé dans le fichier json