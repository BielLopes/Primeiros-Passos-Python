class Usuario():
    #Define uma variavel global para colocar os ID

    def __init__(self, nome: str, idade: int, data_cadastro: str, senha: str, id: int) -> None:
        self.name = nome
        self.idade = idade
        self.data_cadastro = data_cadastro
        self.senha = senha
        self.id = id

    def get_id(self) -> int:
        return self.id

    def get_idade(self) -> int:
        return self.idade

    def get_name(self) -> str:
        return self.name

    def get_data_cadastro(self) -> str:
        return self.data_cadastro

    def get_senha(self) -> str:
        return self.senha

    def set_idade(self, idade: int) -> None:
        self.idade = idade

    def set_name(self, nome: str) -> None:
        self.name = nome

    def set_data_cadastro(self, data_cadastro: str) -> None:
        self.data_cadastro = data_cadastro


    def set_senha(self, senha: str) -> None:
        self.senha = senha

    #Retorna todos os daods do objeto
    def exibe_dados(self) -> None:
        print ("Nome: "+self.get_name())
        print ("Senha: " + self.get_senha())
        print ("Idade: "+self.get_idade())
        print ("Data de Cadastro: "+self.get_data_cadastro())
        print ("ID: "+str(self.get_id()+1))
