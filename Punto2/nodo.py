class Nodo:
	"""
	Clase Nodo:

	Nos permite crear un nodo para el arbol

	Parametros de entrada:
	-nombre
	-padre
	-arista

	Atributos:
	-nombre
	-padre
	-arista
	-hijos=list[]
	"""
	def __init__(self, nombre, padre, arista=None):
		self.nombre = nombre
		self.padre  = padre
		self.hijos  = []
		self.arista = arista

	def agregar_hijo(self, hijo):
		self.hijos.append(hijo)

	def regresar_hijo(self, arista):
		for hijo in self.hijos:
			if hijo.arista == arista:
				return hijo
		return None