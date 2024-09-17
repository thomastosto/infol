import argparse

# Configurer l'analyseur d'arguments
parser = argparse.ArgumentParser(description='Remplacer ````bash par # et ```` par # dans un fichier.')
parser.add_argument('filename', type=str, help='Le nom du fichier à modifier')

# Analyser les arguments
args = parser.parse_args()

# Ouvrir le fichier en mode lecture
with open(args.filename, 'r') as file:
    content = file.read()

# Remplacer les occurrences de ````bash par # et ```` par #
content = content.replace('````bash', '#').replace('````', '#')

# Ouvrir le fichier en mode écriture
with open(args.filename, 'w') as file:
    file.write(content)