import re
import time


class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if telefone in self.contatos.values():
            print(
                f"Número de telefone '{telefone}' já está em uso. Por favor, escolha um número diferente.")
            return
        if not re.match(r'^\d{2}-\d{5}-\d{4}$', telefone):
            print("Número de telefone inválido. Por favor, use o formato 'XX-XXXX-XXXX'.")
            return
        self.contatos[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
        else:
            print(f"Contato '{nome}' não encontrado.")

    def pesquisar_contato(self, nome):
        contato = self.contatos.get(nome)
        if contato:
            return f"Nome: {nome}, Telefone: {contato}"
        else:
            return "Contato não encontrado."

    def listar_contatos(self):
        if not self.contatos:
            return "Não há contatos na agenda."
        for nome, telefone in self.contatos.items():
            print(f"{nome}: {telefone}")


def menu(agenda):
    while True:
        print("\nOpções do Menu:")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Pesquisar contato")
        print("4 - Listar contatos")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        time.sleep(1.5)

        match escolha:
            case '1':
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o número de telefone: ")
                agenda.adicionar_contato(nome, telefone)
                time.sleep(1.5)
            case '2':
                nome = input("Digite o nome do contato para remover: ")
                agenda.remover_contato(nome)
                time.sleep(1.5)
            case '3':
                nome = input("Digite o nome do contato para pesquisar: ")
                resultado = agenda.pesquisar_contato(nome)
                print(resultado)
                time.sleep(1.5)
            case '4':
                if not agenda.contatos:
                    print(
                        "Não há contatos na agenda. Escolha a opção 1 para adicionar um contato.")
                for nome, telefone in agenda.contatos.items():
                    print(f"{nome}: {telefone}")
                time.sleep(1.5)
            case '5':
                print("Saindo do programa.")
                time.sleep(1.5)
                break
            case _:
                time.sleep(1.5)
                print("Opção inválida. Por favor, tente novamente.")


agenda = AgendaTelefonica()
menu(agenda)
