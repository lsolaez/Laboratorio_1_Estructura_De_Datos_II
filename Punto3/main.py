from Order import *
tree = BPlusTree(Order)

# Insertamos algunas órdenes en el árbol
order1 = Order(1, 'Camisa', 'Ropa', '2023-03-05')
tree.insert(order1.delivery_date, order1)

order2 = Order(2, 'Pantalón', 'Ropa', '2023-03-06')
tree.insert(order2.delivery_date, order2)

order3 = Order(3, 'Zapatos', 'Calzado', '2023-03-07')
tree.insert(order3.delivery_date, order3)

order4 = Order(4, 'Botella de agua', 'Bebidas', '2023-03-07')
tree.insert(order4.delivery_date, order4)

# Buscamos un pedido por su fecha de entrega.
result = tree.search('2023-03-07')

# mostramos el resultado de la busquedad
print(result.product_name)
# Output: 'Zapatos'