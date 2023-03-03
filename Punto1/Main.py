from Punto import *
import csv


tree = AVLTree()
"""
with open('User_track_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        tree.insert(format(row[1]))
"""

tree.insert("jimenezzuletajhonjanner")
tree.insert("mivallesola")
tree.insert("31wmparzjhqbvsn6bcijxbj245cy")
tree.insert("nm7adjhazf7n85vkf6zxequ7p")
tree.insert("nm7adjhazf7n85vkf6zxequ7p")
tree.insert("21nkonqixyujyyuxcgner5p2i")
tree.insert("12179172375")
tree.insert("0cxaozs3a5z8m26vwzzc80wb9")
tree.insert("31wuuvwl5ak5254tirgzgux5hycy")
tree.insert("31oj4ddmhj72gh65gjgkrfbqx4ia")
tree.insert("316aov5an7ol5ldr64mksxnfrwvu")
tree.insert("usmmuh3bnsqmv3q8d4227ndyt")
tree.insert("09n35jjitgmqw8xcqmkp9nsri")
tree.insert("marianact10-7")
if tree.search("316aov5an7ol5ldr64mksxnfrwvu"):
    print("User ID found!")
else:
    print("User ID not found.")
# Obtiene la altura del nodo correspondiente al user_id "user_id_3"
height = tree.get_node_height("316aov5an7ol5ldr64mksxnfrwvu")
print("Altura del nodo correspondiente al user_id:", height)


# Imprime los nodos en orden por nivel
print(tree.level_order_traversal())

