import lectureJson as lj
import codage as cod
import Node as nd

cheminTEXT = "text.json"
cheminTEXTOUT = "out-text.json"

# Lecture du text à encoder dans le fichier json text.json
x = lj.read(cheminTEXT, "text")
print("Texte à encoder :", x)

table = cod.build_Frequency_Table(x)    # Création de la table de fréquence
lj.write(cheminTEXTOUT, "table", table) # Ecriture de la table de fréquence dans le fichier json out-text.json

table0 = cod.build_Huffman_Tree_List(table)

print(table0)
tree = cod.build_Huffman_Tree(table0)

print(tree[0].left)
print(tree[0].right)

print(tree[0].left.left)
print(tree[0].left.right)

