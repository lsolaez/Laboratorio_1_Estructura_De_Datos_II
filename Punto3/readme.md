# Tienda Virutal usando arboles B+
***
Tenemos una tienda en línea que vende productos de diferentes categorías, como ropa, electrónica, hogar y jardín, etc. Para manejar los pedidos de manera eficiente, decidimos utilizar una estructura de árbol B+ para organizar los pedidos según su fecha de entrega.

Cada nodo del árbol B+ representa una fecha de entrega y contiene una lista de pedidos que se entregarán en esa fecha. Cada pedido se identifica por su número de pedido único.

## Correr el codigo

Ejecutar el archivo `main.py`

## Modo de empleo de codigo

Para insertar una orden se hace de la siguiente manera:
```
order1 = Order(1, 'Camisa', 'Ropa', '2023-03-05')
tree.insert(order1.delivery_date, order1)
```

Order() es una clase la cual solicita como parametros de entrada el numero de orden, el producto, el tipo de producto y la fecha de delivery.

Para hacer una busqueda se hace de la siguiente manera:
```
result = tree.search('2023-03-07')
print(result.product_name)
```


## Reference
Este codigo es de autoria del grupo de trabajo y amigos externos al grupo.
