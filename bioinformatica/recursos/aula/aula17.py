class Pessoa:

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def obterNome(self):
		return self.nome

	def obterIdade(self):
		return self.idade

	def alterarIdade(self, nova_idade):
		self.idade = nova_idade

	def mostrarPessoa(self):
		print('Nome: %s' % self.nome)
		print('Idade: %d\n' % self.idade)


p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Joao', 20)

pessoas = [p1, p2]

for pessoa in pessoas:
	pessoa.mostrarPessoa()