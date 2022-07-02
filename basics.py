#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Python tutorial basic explanations
"""

# 0 - apresentar a história do python e o fato dela ser uma linguagem interpretada.
####### BÁSICO DE MANIPULAÇÃO DE DADOS #######
# 1 - dar um type em cada um dos tipos primitivos (inteiro - string - float - bool - complex)
type(6)
type(4.2)
type("string")
type('string too')
type(True)
type(2 + 3j)
# 2 - A divisão de dois inteiro é um número inteiro?
type(3/3)
# 3-  variáveis são espaços de memórias que tem um label associado a elas, poem, diferente de C, a tipagem é dinâmica
avant = 23
type(avant)
avant = "drone"
type(avant)
del(avant)
# 4 - O nome das variáveis não pode começar com número e não podem conter caracteres especiais, a exeção é '_', nem serem palavras reservadas (class = 1 da erro)
nome = "correta"
# 1nome = "errado!!"
# n@me = "errado!!"
nome1234 = 34
# 5 - escrita de variáveis camelCase e snake_case
nome_de_variavel = "snake_case"
nomeDeVariavel = "camelCase"
# 6 - operadores aritiméticos (+, -, *, /, **, // (divisão inteira), %, +=, -=, *=, /=, %=):
a = 2
b = 3
a * b
# etcetara
# 7 - operadores lógicos (==, !=, >, >=, <, <= , is, not, and, or, not, in):
a != b
"ab" > "ba"
"ab" == "ba" # voce pode usar is
"ab" < "ba"
not a < b
b >= a and "ab" > "ba"
b >= a or "ab" > "ba"
# 8 - operadores aritiméticos com strings:
texto1 = "Trainee "
texto2 = "AVANT"
texto1 + texto2
texto1 * 3
texto1 * texto2 #ERRO
# 9 - Entrada do usuário
entrada = input()
#digite 1
type(entrada) # string
entrada = int(input("digite um número: "))
# 10 - formatação de tipo em string
print("Numero digitado " + str(entrada))
print("Numero digitado {}".format(entrada))
print(f"Numero digitado {entrada}")

# 0 - apresentar a documentação em python.org

####### ESTRUTURAS COMPOSTAS DE DADOS #######
# 1 - Listas, forma de agrupar informação de forma ordinária (em ordem, formato ordinal)
lista = [1, 2, 3, 4]
lista[0]
lista[3]
lista[4]
lista[1] = "Virou bagunça"
lista[2] =  ["Disney total isso aqui", 3.6]
lista[2][0]
# 2 - Bincando com o indice das listas
lista = [1, 2, 3, 4]
lista[-1]
lista[-2]
lista[0:2]
lista[2:]
lista[:3:2]
lista[2::-1]
# 3 - manipulando listas:
lista = []
lista.append("indice zero")
lista.append("indice um")
lista += [1, 2]
lista * 2
lista *= 2 
lista.extend([True, False])
"indice zero" in lista
lista.pop()
lista.remove("indice um")
lista = [[]] * 3
lista[0].append(3)
lista2 = lista
lista2.append(5) # Mostrar que altera a lista original
lista2 - lista.copy()
# 4 - Tuplas são como listas, porém, são imutaveis
tupla = tuple(lista)
tupla[0] = 1 # ERROR!!!
nova_tupla = (1, 2, 3, ["Coisas", "Aleatórias"])
nova_tupla.append("Value") #ERROR!!!
type(nova_tupla)
# 5 - range é uma sequencia imutável de números inteiros
sequencia = range(0,6)
type(sequencia)
range(-10, 10, 2)
range(10)
# 6 - sets: conjunto de valores imutaveis
letras = {'A', 'V', 'A', 'N', 'T'}
letras # output: {'A', 'N', 'T', 'V'}
mistura = {1, 2, 'tudo', int}
mistura[0] #ERROR!! - um set só faz sentido como conjunto
type(int) # kkkkkkk
# 7 - operações de conjuntos:
a = set('abacate')
b = set('abacaxi')
a
b
a - b # Diferença
b - a # Diferença
a | b # união
a & b # interceção
b = {}
type(b)
b = set()
type(b)
# 8 - Dicionários são listas cujos indices são um conjunto
dicionario = {}
dicionario['key'] = "value"
dicionario[1] = 2.5
dicionario[2.5] = False
dicionario[False] = True
dicionario[(1, 2, 3)] = 10
dicionario.keys()
dicionario.values()
a = dict(um=1, dois=2, três=3)
'chave' in dicionario
dicionario.get('chave', "Chave não encontrada!")
del(dicionario['key'])

####### CONDICIONAIS E LOOPS DE REPETIÇÂO ####### - A partir daqui coloque o código em um editor de texto
# 1 - Condicionais:
a = 10
b = 20
if a > b:
    print("A é maior do que b")
elif a == b:
    print("A é igual a b")
else:
    print("A é menor do que b")
# Condicionais não tem segredo
# 2 - Loop while
i = 0
while i < 10:
    i += 1

i = 0
while True:
    if i >= 10:
        break
    i += 1
# Loop For
for i in range(10):
    print(i)
lista = [1, 5, 6, 9, 0]
for i in lista:
    print(lista)


####### ORIENTAÇÃO A OBJETOS #######
class Estudante():

    def __init__(self, nome: str, matricula: int, curso: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas: list = []

    def pegar_disciplina(self, disciplina: str) -> None:
        self.disciplinas.append(disciplina)

    def verificar_sisciplina(self, disciplina):
        return disciplina in self.disciplinas

    def __repr__(self) -> str:
        return f"Nome: {self.nome}\nMatricula: {self.matricula}"

class A(object):
  variavel = 10

  def __init__(self):
    self.variavel = 15

##### LER E ESXREVER EM ARQUIVO ####
file = open('filename.txt', 'a')
lines = file.readlines()