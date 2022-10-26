class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node_one = None
node_two = Node("X", None)
node_three = Node("Y", node_two)
print(node_two)
#aquí le estoy diciendo que me arroje el dato del nodo
print(node_two.data)
#aquí le estoy diciendo que me lleve a otro nodo
print(node_two.next)
#si quiero saber el dato del siguiente nodo lo hago así
print(node_three.next.data)
#Si quiero que el nodo 1 que no tiene ningún valor lo apuntemos a otro lado o queremos saber dónde nos lleva
node1 = Node("Z", node_three)
print(node1.next.data)
#para saber ahora cuál es el valor del nodo uno
print(node1.data)
print()
"""
Creación de una serie de nodos
"""
head = None
for count in range(1,5):
    head = Node(count, head)
while head != None:
    print(head.data)
    head = head.next

"""
Lo que hicimos fue declarar tres variables node_one, node_two, node_three e ibamos asignando valores a cada uno de los nodos
"""