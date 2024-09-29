'''Instruções para Usar o Simulador de Corrida de Fórmula 1
Bem-vindo ao simulador de corrida de Fórmula 1! Este programa permite que você simule corridas entre diferentes pilotos e mantenha um ranking geral com os melhores tempos. Siga as instruções abaixo para começar:


Python 3+ instalado no sistema.
Dependências:

Não há dependências externas. O código utiliza apenas a biblioteca padrão do Python.
Informações Relevantes:

Como Usar
Iniciar o Programa:

Execute o arquivo Python. O programa começará a rodar e você verá um menu.
Menu Principal:

Você verá as seguintes opções:
Iniciar Corrida: Para cadastrar pilotos e simular uma corrida.
Exibir Ranking Geral: Para visualizar os melhores tempos de cada piloto acumulados ao longo das corridas.
Sair: Para encerrar o programa.
Iniciar uma Corrida:

Se você escolher "Iniciar Corrida":
O programa solicitará quantos pilotos você deseja cadastrar. Digite um número e pressione Enter.
Para cada piloto, insira o nome e pressione Enter.
Em seguida, insira o número de voltas que a corrida terá.
O programa simulará a corrida e exibirá os resultados, incluindo o tempo de cada piloto.
Exibir Ranking Geral:

Se você escolher "Exibir Ranking Geral":
O programa mostrará uma lista dos pilotos com seus melhores tempos registrados. O ranking é ordenado pelo melhor tempo, do menor para o maior.
Sair do Programa:

Escolha a opção "Sair" para encerrar o simulador.
Dicas
Você pode realizar quantas corridas quiser, e o ranking geral será atualizado após cada uma.
Experimente diferentes combinações de pilotos e voltas para ver como isso afeta os resultados.
Divirta-se simulando suas corridas e boa sorte para os pilotos!'''

import random

def corrida_formulaE(pilotos, num_voltas):
    resultados = {piloto: float('inf') for piloto in pilotos}  # Inicializa com infinito

    for volta in range(1, num_voltas + 1):
        print(f"\nVolta {volta}:")
        for piloto in pilotos:
            tempo_volta = random.uniform(60, 120)
            print(f"{piloto} completou a volta em {tempo_volta:.2f} segundos.")
            # Atualiza o melhor tempo se o tempo da volta for menor
            if tempo_volta < resultados[piloto]:
                resultados[piloto] = tempo_volta

    classificacao = sorted(resultados.items(), key=lambda x: x[1])
    print("\nResultado da Corrida:")
    print("======================")
    print("Posição\t|\tPiloto\t|\tMelhor Tempo")
    print("======================")
    for i, (piloto, melhor_tempo) in enumerate(classificacao):
        if melhor_tempo == float('inf'):
            melhor_tempo = "N/A"  # Caso o piloto não tenha completado a volta
        print(f"{i + 1}\t|\t{piloto}\t|\t{melhor_tempo:.2f} segundos" if isinstance(melhor_tempo, float) else f"{i + 1}\t|\t{piloto}\t|\t{melhor_tempo}")
    print("======================")

    return classificacao

def atualizar_ranking(ranking_geral, classificacao):
    for piloto, melhor_tempo in classificacao:
        if piloto not in ranking_geral or melhor_tempo < ranking_geral[piloto]:
            ranking_geral[piloto] = melhor_tempo  # Atualiza apenas se o novo tempo for melhor

def exibir_ranking_geral(ranking_geral):
    print("\nRanking Geral:")
    print("======================")
    print("Posição\t|\tPiloto\t|\tMelhor Tempo")
    print("======================")
    classificacao_geral = sorted(ranking_geral.items(), key=lambda x: x[1])
    for i, (piloto, melhor_tempo) in enumerate(classificacao_geral):
        print(f"{i + 1}\t|\t{piloto}\t|\t{melhor_tempo:.2f} segundos")
    print("======================")

def menu():
    ranking_geral = {}
    while True:
        print("\n=== Menu da Corrida ===")
        print("1. Iniciar Corrida")
        print("2. Exibir Ranking Geral")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            num_pilotos = int(input("Quantos pilotos deseja cadastrar? "))
            pilotos = []
            for i in range(num_pilotos):
                piloto = input(f"Insira o nome do piloto {i + 1}: ")
                pilotos.append(piloto)

            num_voltas = int(input("Insira o número de voltas da corrida: "))
            classificacao = corrida_formulaE(pilotos, num_voltas)
            atualizar_ranking(ranking_geral, classificacao)
        elif opcao == '2':
            exibir_ranking_geral(ranking_geral)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
