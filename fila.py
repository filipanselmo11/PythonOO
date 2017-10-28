import heapq

class FilaDePrioridade:

	def __init__(self):
		self.fila = []
		self.indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self.fila, (-prioridade, self.indice, item))
		self.indice += 1

	def remover(self):
		return heapq.heappop(self.fila)[-1]


class Item:

	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

#class Numero:
	#def __init__(self, num):
		#self.num = num
	
	#def __repr__(self):
		#return self.num


fila = FilaDePrioridade()
fila.inserir(Item('marcos'), 28)
fila.inserir(Item('joao'), 30)
fila.inserir(Item('maria'), 18)
fila.inserir(Item('fílip'), 20)

print(fila.remover())
print(fila.remover())
print(fila.remover())


#fila.inserir(Numero(1), 1)
#fila.inserir(Numero(2), 2)
#fila.inserir(Numero(3), 3)

#print(fila.remover())
#print(fila.remover())