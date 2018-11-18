class Usuario:
    #Define uma variavel global para colocar os ID

    def __init__(self, nome, idade, data_cadastro, senha, id):
        self.name = nome
        self.idade = idade
        self.data_cadastro = data_cadastro
        self.senha = senha
        self.id = id

    def get_id(self):
        return self.id

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_name(self):
        return self.name

    def set_name(self, nome):
        self.name = nome

    def get_data_cadastro(self):
        return self.data_cadastro

    def set_data_cadastro(self, data_cadastro):
        self.data_cadastro = data_cadastro

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    #Retorna todos os daods do objeto
    def exibe_dados(self):
        print ("Nome: "+self.get_name())
        print ("Senha: " + self.get_senha())
        print ("Idade: "+self.get_idade())
        print ("Data de Cadastro: "+self.get_data_cadastro())
        print ("ID: "+str(self.get_id()+1))
