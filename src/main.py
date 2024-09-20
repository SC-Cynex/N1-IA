import os
from models.connection import Connection
from models.scheduling import Scheduling
from view.version1 import version1
from view.version2 import version2
from view.comparation import comparation

def main_menu():
    connection = Connection()
    scheduling = Scheduling()

    while True:
        os.system('cls')
        print('''
   _____   ___  _ _____  __    ___  ___ _    _____   _____ _____   __ 
  / __\ \ / / \| | __\ \/ /   |   \| __| |  |_ _\ \ / / __| _ \ \ / / 
 | (__ \ V /| .` | _| >  <    | |) | _|| |__ | | \ V /| _||   /\ V /  
  \___| |_| |_|\_|___/_/\_\   |___/|___|____|___| \_/ |___|_|_\ |_|    

        [1] - Setar Conexões
        [2] - Visualizar Conexões
        [3] - Setar Agendamentos
        [4] - Visualizar Agendamentos
        [5] - Versão 1 - Algoritmo Básico
        [6] - Versão 2 - Algoritmo com PSO
        [7] - Comparar as duas versões
        [0] - Sair
              ''')
        optionVersion = int(input("\tOpção: "))

        match optionVersion:
            case 0:
                break
            case 1:
                connection.set_connections()
            case 2:
                connection.get_connections()
            case 3:
                scheduling.set_scheduling()
            case 4:
                scheduling.get_scheduling()
            case 5:
                version1(connection, scheduling)
                input("\n\tPressione Enter para continuar...")
                continue
            case 6:
                version2(connection, scheduling)
                input("\n\tPressione Enter para continuar...")
                continue
            case 7:
                comparation(connection, scheduling)
                input("\n\tPressione Enter para continuar...")
                continue
            case _:
                print("\tOpção inválida. Tente novamente.")
                input("\n\tPressione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
