# A script for identifying monophyletic clades containing taxa of interest in phylogenetic trees.
# Tested and working on Python 3.6.
# Positive hits are saved as filename_HIT.tre; the identified clade is extracted from the input tree and saved as filename_HIT_zoom.tre.
# IMPORTANT! The script detects specific strings at the start of the headers of the sequences of interest. To search for different taxonomic names than Gertia, Kareniaceae and Haptista, change the corresponding strings in Lines 22, 24 and 26.

#!/usr/bin/python3.6
import ete3
from ete3 import Tree
import sys
import itertools

tree = ete3.Tree(sys.argv[1])
filename = sys.argv[1]
filename = filename.split(".")[0]
print(filename)

outname = filename + "_HIT" +'.tre'
zoom = filename + "_HIT_zoom" + '.tre'

for leaf in tree:
        i = leaf.name
        if i.startswith("Gertia"):
                leaf.add_features(color="red")
        elif i.startswith("Kareniaceae"):
                leaf.add_features(color="green")
        elif i.startswith("Haptista"):
                leaf.add_features(color="blue")

for node in tree.get_monophyletic(values=["red","blue","green"], target_attr="color"):
        print(node.get_ascii(attributes=["color", "name"], show_internal=False))
        node.write(outfile = zoom)
        tree.write(outfile = outname)
