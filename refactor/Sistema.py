from datetime import datetime
from Usuario import Usuario

class Sistema():

    def __init__(self) -> None:
        self.contador_ids: int = 0
        self.todos_usuarios: dict = {}


    def senha_curta(self, senha: str) -> bool:
        if len(senha) < 4:
            return True
        else:
            return False


    def cadastrar_usuario(self):
        name = str(input("Seu Nome: "))
        idade = input("Sua Idade: ")
        senha = input("Defina Uma Senha: ")
        data_hora = datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H:%M')
        while self.senha_curta(senha):
            senha = input("Senha muito pequene, digite outra: ")

        novo: Usuario = Usuario(name, idade, data_hora, senha, self.contador_ids)
        self.contador_ids += 1

        self.todos_usuarios[self.contador_ids] = novo

        print("Usuário Cadastrado Com Sucesso")
        print ("\n----------------------------------------------------------\n")
        self.menu()


    def listaUsuarios(self):

        print ("Todos os Usuários-----------------------------------------\n")

        if len(self.todos_usuarios) >= 1:
            for id in self.todos_usuarios:
                self.todos_usuarios[id].exibe_dados()
                print("\n\n")
        else:
            print ("Nenhum Usuário Cadastrado!!-------------------------------------------\n")

        print ("| Enter : Voltar                                            |\n")
        input(': ')
        print ("\n----------------------------------------------------------\n")
        self.menu()


    def alteraSenha(self):

        if len(self.todos_usuarios) >= 1:
            print ("| 1 : Alterar Senha por ID                               |\n")
            print ("| 2 : Listar Usuários                                    |\n")
            print ("| 0 : Voltar                                             |\n")
            opc: int = -1
            while opc < 0 or opc > 2:
                opc = int(input('Opção: '))
                if opc <0 or opc > 2:
                    print ("Opcção invalida, Tente Novamente----------------------------------------------------\n")

            if opc == 0:
                self.menu()

            elif opc == 1:
                opc = int(input('ID do Usuario: '))
                if opc in self.todos_usuarios:
                    print('Alterando A Senha de '+self.todos_usuarios[opc].get_name())
                    novaSenha = input('Digite a nova Senha: ')
                    while self.senha_curta(novaSenha):
                        novaSenha = input("Senha muito pequene, digite outra: ")
                    self.todos_usuarios[opc].set_senha(novaSenha)
                    print("Senha Alterada com sucesso!!!------------------------------------------\n")
                else:
                    print("O Usuario Selecionado não Existe!!---------------------------------------\n")

                print("\n\n")
                print("\n\n")
                self.alteraSenha()

            elif opc == 2:
                print ("\n\n")
                self.listaUsuarios()
        else:
            print("Nenhum Usuário Cadastrado! ------------------------------------")
            print("| Enter : Voltar                                            |\n")
            opc: int = input(': ')
            print ("\n----------------------------------------------------------\n")
            self.menu()


    def excluiUsuario(self):
        if len(self.todos_usuarios) >= 1:
            print ("| 1 : Excluir Usuário por ID                             |\n")
            print ("| 2 : Listar Usuários                                    |\n")
            print ("| 0 : Voltar                                             |\n")
            opc: int = -1
            while opc < 0 or opc > 2:
                opc = int(input('Opção: '))
                if opc < 0 or opc > 2:
                    print ("Opcção invalida, Tente Novamente\n")

            if opc == 0:
                print ("\n\n")
                self.menu()

            elif opc == 1:
                opc = int(input('ID do Usuario: '))
                if opc in self.todos_usuarios:
                    del(self.todos_usuarios[opc])
                    print("Usuário deletado com sucesso!!!")
                else:
                    print("O Usuario Selecionado não Existe!!\n")

                print("\n\n")
                self.excluiUsuario()

            elif opc == 2:
                print ("\n\n")
                self.listaUsuarios()
        else:
            print("Nenhum Usuário Cadastrado! ------------------------------------")
            print("| Enter : Voltar                                            |\n")
            input(': ')
            print ("\n----------------------------------------------------------\n")

            self.menu()

    def menu(self) -> None:
        print ("Bem Visndo ao Sistema de GERENCIAMENTO DE USUÀRIOS \n")
        print ("Escolha uma das opções abaixo: \n")
        print ("----------------------------------------------------------\n")
        print ("| 1 : Cadastrar um Usuário                               |\n")
        print ("| 2 : Listar Usuários                                    |\n")
        print ("| 3 : Alterar Senha de Um Usuário                        |\n")
        print ("| 4 : Excluir um Usuário                                 |\n")
        print ("| 0 : Sair                                               |\n")
        print ("----------------------------------------------------------\n")
        opc: int = -1

        while opc < 0 or opc > 4:
            opc = int(input('Opção: '))
            if opc <0 or opc > 4:
                print("Opcção invalida, Tente Novamente\n")

        if opc == 0:
            exit()

        elif opc == 1:
            self.cadastrar_usuario()

        elif opc == 2:
            self.listaUsuarios()

        elif opc == 3:
            self.alteraSenha()

        elif opc == 4:
            self.excluiUsuario()
