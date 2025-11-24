# A basic script for extracting branch length values from tree files
# Tested and working on Python 3.6 

import ete3
from ete3 import Tree
import sys
import pandas as pd

tree = ete3.Tree(sys.argv[1])
filename = sys.argv[1]
filename = filename.split(".")[0]
subtree_out = filename + "_subtree.tre"
lengths = {}
lengths_out = filename + "_lengths.txt"

haptos = []
nonhaptos = []
for leaf in tree:
	i = leaf.name
	if i.startswith("Taka") or i.startswith("Karl") or i.startswith("Geph") or i.startswith("Diac") or i.startswith("NIES") or i.startswith("Pavl") or i.startswith("Emil") or i.startswith("Chry") or i.startswith("Isoc") or i.startswith("Phae") or i.startswith("Tiso"):
		haptos.append(i)
	else:
		nonhaptos.append(i)

## rerooting
outgroup = tree.get_common_ancestor(nonhaptos)
ancestor = tree.get_common_ancestor(haptos)
tree.set_outgroup(outgroup)
check = tree.check_monophyly(haptos, "name")
print(check)

## writing subtree with only taxa of interest
for node in tree.get_monophyletic(haptos, target_attr="name"):
	node.write(outfile = subtree_out)

## extracting branch lengths
subtree = ete3.Tree(subtree_out)
for leaf in subtree.iter_leaves():
	length = subtree.get_distance(leaf)
	lengths[leaf.name] = length
print(lengths)

## writing unsorted output
(pd.DataFrame.from_dict(data=lengths, orient='index')
   .to_csv(lengths_out, header=False))
print("Done! Branch lengths written to",lengths_out)
