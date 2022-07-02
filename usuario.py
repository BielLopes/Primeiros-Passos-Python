class Usuario:
    #Define uma variavel global para colocar os ID

    def __init__(self, nome, idade, data_cadastro, senha, id):
        self.nome = nome
        self.idade = idade
        self.data_cadastro = data_cadastro
        self.senha = senha
        self.id = id

    #Retorna todos os daods do objeto
    def __repr__(self) -> str:
        return f"Nome: {self.nome}\nSenha: {self.senha}\nIdade: {self.idade}znData de cadastro: {self.data_cadastro}\nID: {self.id}"
