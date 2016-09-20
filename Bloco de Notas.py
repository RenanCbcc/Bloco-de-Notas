# -*- coding: utf-8 -*-
import sys


class Nota:
	def __init__(self,ID = None,txt = ""):
		self.ID = ID
		self.texto = txt
        #print("Construtor chamado com sucesso")
		
	def nota(id,string):
		self.ID = id
		self.texto = string
		
	def get_Id(self):
		return self.ID
	def __str__(self):
		return(" ID  : %i \n Texto: %s "%(self.ID,self.texto))	
		
class Bloco():
		
	def __init__(self):
		self.notas = []
			
	def Novo(self):
		id = int(input("Digite o ID da nota 0-10: "))
		string = input(str("Digite o texto da nota: "))
		self.notas.append(Nota(id, string))			
	
	def Imprimir(self):
		for i in self.notas:
			print(i) 

	def Buscar(self,id):
		for i in self.notas:
			if id == i.get_Id():
				print(i)
				break
			else:
				print("Não encontrado")
			
	def Remover(self,id):
		for i in self.notas:
			if id == i.get_Id():
				print("Nota removida:")
				print(i)
				self.notas.remove(i)
				
	def Modificar(self,id):
		for i in self.notas:
			if id == i.get_Id():
				id = int(input("Digite o ID da nota 0-10: "))
				string = input(str("Digite o texto da nota: "))
				i.nota(id,string)
				break
			else:
				print("Não encontrado")
				
	
class Menu:
    def __init__(self):
        self.blocodenotas = Bloco()
        self.escolhas = {
        "1": self.imprimir_notas,
        "2": self.buscar_notas,
        "3": self.adicionar_notas,
        "4": self.modificar_notas,
		"5": self.remover_notas,
        "6": self.sair
        }

    def apresentar_menu(self):
        print("""
        Menu
        1. Imprimir Notas
        2. Buscar Notas
        3. Adicionar Notas
        4. Modificar Notas
		5. Remover Notas
        6. Sair        
        """)

    def executar(self):
        while True:
            self.apresentar_menu()
            escolha = input("Escolha uma opção:")
            acao = self.escolhas.get(str(escolha))
            if acao:
                acao()
            else:
                print ("{0} não foi uma escolha válida.".format(escolha))
        
    def imprimir_notas(self):
        self.blocodenotas.Imprimir()
        
    def buscar_notas(self):
	    id = int(input("Digite o ID da nota 0-10: "))
	    self.blocodenotas.Buscar(id)
    
    def adicionar_notas(self):
        self.blocodenotas.Novo()
		
    def modificar_notas(self):
		id = int(input("Digite o ID da nota 0-10: "))
        self.blocodenotas.Modificar(id)
	
    def remover_notas(self):
	    id = int(input("Digite o ID da nota 0-10: "))
	    self.blocodenotas.Remover(id)
		
    def sair(self):
        print ("Saindo...")
        sys.exit(0) 		
		
    if __name__ == "__main__":
	    m = Menu()
	    m.executar()
