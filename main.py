import os
import pickle

#relizar a votação
class Mesario:
    def __init__(self):
        self.candidatos = {}
        self.eleitores = []
        self.votacoes = {}

#Cria o menu do mesário e dá a opção à ser escolhida
    def menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("1 - Ler arquivo de candidatos")
            print("2 - Ler arquivo de eleitores")
            print("3 - Iniciar votação")
            print("4 - Apurar votos")
            print("5 - Mostrar resultados")
            print("6 - Sair do programa")
            print
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                self.ler_arquivo_candidatos()
            elif opcao == 2:
                self.ler_arquivo_eleitores()
            elif opcao == 3:
                self.registrar_voto()
            elif opcao == 4:
                self.apurar_votos()
            elif opcao == 5:
                self.mostrar_resultados()
            elif opcao == 6:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida")

#Lê o arquivo txt dos candidatos
    def ler_arquivo_candidatos(self):
        arquivo = input("Digite o nome do arquivo de candidatos: ")
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as f: #abre o arquivo no modo leitura
                self.candidatos = {linha.strip(): [] for linha in f.readlines()}
        else:
            print("Arquivo não encontrado")

#Lê o arquivo txt dos eleitores
    def ler_arquivo_eleitores(self):
        arquivo = input("Digite o nome do arquivo de eleitores: ")
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as f: #abre o arquivo no modo leitura
                self.eleitores = [linha.strip() for linha in f.readlines()]
        else:
            print("Arquivo não encontrado")


def pesquisar_eleitor(self, titulo):
    for eleitor in self.eleitores:
        if eleitor.titulo == titulo:
            return eleitor
    return None

#registra a votação dos eleitores(Não consegui fazer por nada)
def registrar_voto(self, eleitor, votos):
    for voto in votos:
        uf = voto.uf
        numero = voto.numero

        if uf not in self.votacoes:
            self.votacoes[uf] = [0] * len(self.candidatos[uf])

        for i, candidato in enumerate(self.candidatos[uf]):
            if candidato.numero == numero:
                self.votacoes[uf][i] += 1
                break
        else:
            print("Candidato não encontrado! Voto Nulo.")


#mesário inicia a votação
def iniciar_votacao(self):
    uf = input("Digite o UF onde está localizada a urna: ")

    if uf not in self.candidatos:
        print("UF não encontrada!")
        return

    while True:
        titulo = input("Informe o Título de Eleitor: ") #informa o titulo de eleitor de quem vai votgar
        eleitor = self.pesquisar_eleitor(titulo)

        if eleitor is None:
            print("Título não encontrado!")
        else:
            votos = []

            for cargo, voto_valido in enumerate([1, 2, 3, 4, 5]):
                print(f"Eleitor: {eleitor.nome}")
                print(f"Estado: {eleitor.uf}")

                voto = votos(cargo, 0)

                while True:
                    if cargo == 4: # Presidência
                        numero = input(f"Informe o voto para {cargo}° Cargo: ") #voto para presidente
                    else:
                        numero = input(f"Informe o voto para {cargo}° Cargo (MG = 1 a 40): ")

                    if not numero.isdigit():
                        if cargo == 4 and numero == "B": # Branco para Presidente
                            voto.numero = -1
                            break
                        else:
                            print("Número inválido!")
                    else:
                        voto.numero = int(numero)
                        break

                if voto.numero != voto_valido:
                    print("Voto Nulo.")
                else:
                    votos.append(voto)

            confirma = input("Confirma (S ou N)? ").upper() #confirma o voto do eleitor

            if confirma == "S":
                self.registrar_voto(eleitor, votos)
                print("Voto registrado com sucesso!")
            else:
                print("Voto não registrado.")

        registrar_novos_votos = input("Registrar novos votos (S ou N)? ").upper()

        if registrar_novos_votos == "N":
            break


#mostra quantos votos cada candidato recebeu
    def mostrar_resultados(self):
        if not self.votacoes:
            print("Por favor, apure os votos antes de mostrar os resultados")
            return

        print("Resultados da votação:")
        for uf, votos in self.votacoes.items():
            print(f"{uf}:")
            for i, voto in enumerate(votos):
                print(f"{self.candidatos[uf][i]}: {voto} votos")

mesario = Mesario()
mesario.menu()