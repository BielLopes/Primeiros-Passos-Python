# encoding: utf-8
from usuario import Usuario
from datetime import datetime

'''
total_user = 0
nome = "Você"
idade = 20
data = "18/11/2018"
user2 = Usuario(nome, idade, data, total_user)
user2.set_idade(16)
user2.exibe_all()
Deu Certo Carai
'''
conta_id = 0
TodosUser = {}


def senha_curta(senha):
    if len(senha) < 4:
        return True
    else:
        return False


def cadastrar_usuario():
    name = str(input("Seu Nome: "))
    idade = input("Sua Idade: ")
    senha = input("Defina Uma Senha: ")
    data_hora = datetime.now()
    data_hora = data_hora.strftime('%d/%m/%Y %H:%M')
    while senha_curta(senha):
        senha = input("Senha muito pequene, digite outra: ")

    global conta_id
    novo = Usuario(name, idade, data_hora, senha, conta_id)
    conta_id = conta_id + 1

    global TodosUser
    TodosUser[conta_id] = novo

    print("Usuário Cadastrado Com Sucesso")
    menu()


def listaUsuarios():

    print ("Todos os Usuários-----------------------------------------\n")
    global  TodosUser

    if len(TodosUser) >= 1:
        for id in TodosUser:
            TodosUser[id].exibe_dados()
            print("\n\n")
    else:
        print ("Nenhum Usuário Cadastrado!!-------------------------------------------\n")

    print ("| Enter : Voltar                                            |\n")
    opc = input(': ')

    menu()


def alteraSenha():
    global TodosUser
    if len(TodosUser) >= 1:
        print ("| 1 : Alterar Senha por ID                               |\n")
        print ("| 2 : Listar Usuários                                    |\n")
        print ("| 0 : Voltar                                             |\n")
        opc = -1
        while opc < 0 or opc > 2:
            opc = int(input('Opção: '))
            if opc <0 or opc > 2:
                print ("Opcção invalida, Tente Novamente----------------------------------------------------\n")

        if opc == 0:
            menu()

        elif opc == 1:
            opc = int(input('ID do Usuario: '))
            if opc in TodosUser:
                print('Alterando A Senha de '+TodosUser[opc].get_name())
                novaSenha = input('Digite a nova Senha: ')
                while senha_curta(novaSenha):
                    novaSenha = input("Senha muito pequene, digite outra: ")
                TodosUser[opc].set_senha(novaSenha)
                print("Senha Alterada com sucesso!!!------------------------------------------\n")
            else:
                print("O Usuario Selecionado não Existe!!---------------------------------------\n")

            print("\n\n")
            print("\n\n")
            alteraSenha()

        elif opc == 2:
            print ("\n\n")
            listaUsuarios()
    else:
        print("Nenhum Usuário Cadastrado! ------------------------------------")
        print("| Enter : Voltar                                            |\n")
        opc = input(': ')

        menu()


def excluiUsuario():
    global TodosUser
    if len(TodosUser) >= 1:
        print ("| 1 : Excluir Usuário por ID                             |\n")
        print ("| 2 : Listar Usuários                                    |\n")
        print ("| 0 : Voltar                                             |\n")
        opc = -1
        while opc < 0 or opc > 2:
            opc = int(input('Opção: '))
            if opc < 0 or opc > 2:
                print ("Opcção invalida, Tente Novamente\n")

        if opc == 0:
            print ("\n\n")
            menu()

        elif opc == 1:
            opc = int(input('ID do Usuario: '))
            if opc in TodosUser:
                del(TodosUser[opc])
                print("Usuário deletado com sucesso!!!")
            else:
                print("O Usuario Selecionado não Existe!!\n")

            print("\n\n")
            excluiUsuario()

        elif opc == 2:
            print ("\n\n")
            listaUsuarios()
    else:
        print("Nenhum Usuário Cadastrado! ------------------------------------")
        print("| Enter : Voltar                                            |\n")
        opc = input(': ')

        menu()


def menu():
    print ("Bem Visndo ao Sistema de GERENCIAMENTO DE USUÀRIOS \n")
    print ("Escolha uma das opções abaixo: \n")
    print ("----------------------------------------------------------\n")
    print ("| 1 : Cadastrar um Usuário                               |\n")
    print ("| 2 : Listar Usuários                                    |\n")
    print ("| 3 : Alterar Senha de Um Usuário                        |\n")
    print ("| 4 : Excluir um Usuário                                 |\n")
    print ("| 0 : Sair                                               |\n")
    print ("----------------------------------------------------------\n")
    opc = -1

    while opc < 0 or opc > 4:
        opc = int(input('Opção: '))
        if opc <0 or opc > 4:
            print("Opcção invalida, Tente Novamente\n")

    if opc == 0:
        exit()

    elif opc == 1:
        cadastrar_usuario()

    elif opc == 2:
        listaUsuarios()

    elif opc == 3:
        alteraSenha()

    elif opc == 4:
        excluiUsuario()


if __name__  == "__main__":
    menu()
