import os
import sys


import colored
from colored import stylize


def usage():
    print("Usage: 'python3 MyTree.py' or 'pyhton 3 Mytree.py' \"folder\"")


def tree(root, nbindent=1):
    """ Create a tree
    nbindent should not be manually set
    """
    nbfichiers = 0
    nbdossiers = 0
    indent = "\t|" * nbindent
    for item in os.listdir(root):
        # Si c'est un fichier, on affiche son nom
        if os.path.isfile(os.path.join(root, item)):
            print(stylize(f"|{indent[:-2]}---{item}", colored.fg("green")))
            nbfichiers += 1

        # Si c'est un dossier, on affiche son nom...
        if os.path.isdir(os.path.join(root, item)):
            print(stylize(f"|{indent[:-2]}---{item}", colored.fg("blue")))

            # ... On augmente l'indetation ...
            nbindent += 1
            indent = "\t|" * nbindent

            # ... On appelle tree récursivement tree sur le dossier ...
            nbdossiers += 1
            ret = tree(os.path.join(root, item), nbindent)

            # On incrémente le nb de fichiers et de dossiers contenus dans le sous-dossier
            nbfichiers += ret[0]
            nbdossiers += ret[1]

            # ... Et on diminue l'indentation ...
            nbindent -= 1
            indent = "\t|" * nbindent

    # Retourne le nombre de fichiers et de dossiers trouvés
    return (nbfichiers, nbdossiers)


def main(*args):
    if len(args) == 0:
        root = os.getcwd()
    elif len(args) == 1:
        if os.path.exists(args[0]):
            root = args[0]
        else:
            usage()
            sys.exit("Wrong parameters")
    else:
        usage()
        sys.exit("Wrong number of parameters")

    print(stylize('.', colored.fg("blue")))
    ret = tree(root)
    print(f"{ret[0]} fichiers, {ret[1]} dossiers")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        main(*sys.argv[1:])