import json

#Fonction qui lit un fichier json
def read(name, key):
    f = open(name, 'r')
    x = json.load(f)

    return x[key]
    
#Fonction qui ecrit dans un fichier json
def write(name, key, value):
    f = open(name, 'r')
    x = json.load(f)
    
    x[key] = str(value)

    f = open(name, 'w')
    json.dump(x, f)
    f.close()