class playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id < 0:
            raise ValueError("o id deve ser positivo")
        self.__id = id
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("tem que escrever algo")
        self.__nome = nome
    
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("tem que escrever algo")
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return f"id: {self.__id} - nome: {self.__nome} - descrição: {self.__descricao}"


class musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    def set_id(self, id):
        if id < 0:
            raise ValueError("tem que ser positivo")
        self.__id = id

    def set_titulo(self, titulo):
        if titulo == "":
            raise ValueError("põe o titulo da music caramba")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError("não cale o artista")
        self.__artista = artista

    def set_album(self, album):
        if album == "":
            raise ValueError("cadê o album")
        self.__album = album

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_artista(self):
        return self.__artista
    
    def get_album(self):
        return self.__album
    
    def __str__(self):
        return f"id = {self.__id} - titulo = {self.__titulo} - artista = {self.__artista} - album = {self.__album}"


class playlistitem:
    def __init__(self, id, idplaylist, idmusica, sequencia):
        self.set_id(id)
        self.set_idplaylist(idplaylist)
        self.set_idmusica(idmusica)
        self.set_sequencia(sequencia)

    def set_id(self, id):
        if id < 0:
            raise ValueError("id deve ser positivo")
        self.__id = id

    def set_idplaylist(self, idplaylist):
        if idplaylist < 0:
            raise ValueError("o id deve ser positivo")
        self.__idplaylist = idplaylist

    def set_idmusica(self, idmusica):
        if idmusica < 0:
            raise ValueError("o id deve ser positivo")
        self.__idmusica = idmusica

    def set_sequencia(self, sequencia):
        if sequencia < 0:
            raise ValueError("a sequência deve ser positiva")
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id
    
    def get_idplaylist(self):
        return self.__idplaylist
    
    def get_idmusica(self):
        return self.__idmusica
    
    def get_sequencia(self):
        return self.__sequencia
    
    def __str__(self):
        return f"id = {self.__id} - id da playlist = {self.__idplaylist} - id da música = {self.__idmusica} - sequência = {self.__sequencia}"



class UI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()

            if op == 1: UI.inserir_playlist()
            elif op == 2: UI.listar_playlist()
            elif op == 3: UI.atualizar_playlist()
            elif op == 4: UI.excluir_playlist()
            elif op == 5: UI.inserir_musica()
            elif op == 6: UI.listar_musica()
            elif op == 7: UI.inserir_item()
            elif op == 8: UI.listar_item()
            elif op == 9: UI.listar_musica_playlist()
            elif op == 10: UI.excluir_musica()
            elif op == 11: print("Encerrando o programa")
            else: print("Opção inválida!")

    @staticmethod
    def menu():
       
        print("      SISTEMA DE MÚSICA")
        print("1- Inserir Playlist      2- Listar Playlist")
        print("3- Atualizar Playlist    4- Excluir Playlist")
        print("5- Inserir Música        6- Listar Música")
        print("10- Excluir Música")
        print("7- Inserir Item (Add Música na Playlist)")
        print("8- Listar Itens Geral")
        print("9- Ver Músicas de uma Playlist")
        print("11- Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_playlist(cls):
        print("Inserir Nova Playlist")
        id = int(input("Informe o ID: "))
        nome = input("Informe o Nome: ")
        descricao = input("Informe a Descrição: ")
        x = playlist(id, nome, descricao)
        cls.playlists.append(x)
        print("Playlist inserida com sucesso!")

    @classmethod
    def listar_playlist(cls):
        print("Listagem de Playlists")
        if len(cls.playlists) == 0:
            print("Nenhuma playlist cadastrada.")
        else:
            for x in cls.playlists:
                print(x)

    @classmethod
    def listar_id_playlist(cls, id):
        for x in cls.playlists:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_playlist(cls):
        UI.listar_playlist()
        if len(cls.playlists) > 0:
            id = int(input("Informe o ID da playlist que deseja atualizar: "))
            x = UI.listar_id_playlist(id)
            if x != None:
                cls.playlists.remove(x)
                nome = input("Informe o novo Nome: ")
                descricao = input("Informe a nova Descrição: ")
                novo = playlist(id, nome, descricao)
                cls.playlists.append(novo)
                print("Playlist atualizada!")
            else:
                print("ID não encontrado.")

    @classmethod
    def excluir_playlist(cls):
        UI.listar_playlist()
        if len(cls.playlists) > 0:
            id = int(input("Informe o ID da playlist para excluir: "))
            x = UI.listar_id_playlist(id)
            if x != None:
                cls.playlists.remove(x)
                print("Playlist removida")
            else:
                print("ID não encontrado")

    @classmethod
    def inserir_musica(cls):
        print("Inserir Nova Música")
        id = int(input("Informe o ID: "))
        titulo = input("Informe o Título: ")
        artista = input("Informe o Artista: ")
        album = input("Informe o Álbum: ")
        x = musica(id, titulo, artista, album)
        cls.musicas.append(x)
        print("Música inserida com sucesso")

    @classmethod
    def listar_musica(cls):
        print("Listagem de Músicas")
        if len(cls.musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            for x in cls.musicas:
                print(x)

    @classmethod
    def listar_id_musica(cls, id):
        for x in cls.musicas:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def excluir_musica(cls):
        UI.listar_musica()
        if len(cls.musicas) > 0:
            id = int(input("Informe o ID da música para excluir: "))
            x = UI.listar_id_musica(id)
            if x != None:
                cls.musicas.remove(x)
                print("Música removida.")
            else:
                print("ID não encontrado.")

    @classmethod
    def inserir_item(cls):
        print("Adicionar Música à Playlist")
        id = int(input("ID do Item: "))
        idplaylist = int(input("ID da Playlist: "))
        idmusica = int(input("ID da Música: "))
        sequencia = int(input("Sequência na Playlist: "))
        x = playlistitem(id, idplaylist, idmusica, sequencia)
        cls.itens.append(x)
        print("Item vinculado com sucesso!")

    @classmethod
    def listar_item(cls):
        print("Itens de Playlists musicais")
        if len(cls.itens) == 0:
            print("Nenhum item cadastrado.")
        else:
            for x in cls.itens:
                print(x)

    @classmethod
    def listar_musica_playlist(cls):
        print("\n--- Ver Músicas de uma Playlist ---")
        idplaylist = int(input("Informe o ID da playlist: "))
        encontrou = False
        print(f"\nMúsicas da Playlist ID {idplaylist}:")
        for item in cls.itens:
            if item.get_idplaylist() == idplaylist:
                for m in cls.musicas:
                    if m.get_id() == item.get_idmusica():
                        print(f"- {m.get_titulo()} (Artista: {m.get_artista()}, Álbum: {m.get_album()}) - Sequência: {item.get_sequencia()}")
                        encontrou = True
        if not encontrou:
            print("Nenhuma música encontrada para essa playlist.") 
UI.main()