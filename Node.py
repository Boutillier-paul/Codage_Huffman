leaves_list = []

# Objet Noeud
class Node:

    # Constructeur
    def __init__(self, data):

        self.data = data
        self.frequency = None
        self.left = None
        self.right = None
        self.parent = None
    
    # Renvoi un chaine de caractère définissant l'objet
    def __str__(self):
        return "Node frequency : " + str(self.frequency)

    # Recupère la fréquence d'une feuille
    def getFrequency(self, leaf):

        if isinstance(leaf, Node):
            return leaf.frequency
        else:
            return leaf[1]

    # Applique une fréquence au noeud
    def setFrequency(self):
        self.frequency = self.getFrequency(self.left)+self.getFrequency(self.right)

    # Applique un parent au noeud
    def createParent(self, Node):
        self.parent = Node

    # Applique une valeur aux feuilles du noeud et une fréquence à l'objet parent
    def createLeaves(self, left, right):
        self.left = left
        self.right = right

        # On applique le parent aux feuilles
        if isinstance(left, Node):
            left.createParent(self)
        if isinstance(right, Node):
            right.createParent(self)

        # On applique la fréquence au Noeud
        self.setFrequency()

        # Si le noeud possède au moins une feuille, on l'ajoute à la liste des feuilles
        if not isinstance(left, Node) or not isinstance(right, Node):
            leaves_list.append(self)

        
        