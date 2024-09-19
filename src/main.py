import os
from models.connection import Connection
from models.scheduling import Scheduling
from models.optimize import Optimize

def main_menu():
    connection = Connection()
    scheduling = Scheduling()
    
    while True:
        os.system('cls')
        print('''
   _____   ___  _ _____  __    ___  ___ _    _____   _____ _____   __          ___ 
  / __\ \ / / \| | __\ \/ /   |   \| __| |  |_ _\ \ / / __| _ \ \ / /     __ _|_  )
 | (__ \ V /| .` | _| >  <    | |) | _|| |__ | | \ V /| _||   /\ V /   _  \ V // / 
  \___| |_| |_|\_|___/_/\_\   |___/|___|____|___| \_/ |___|_|_\ |_|   (_)  \_//___|                                                                                                                                                                              

        [1] - Setar Conexões
        [2] - Visualizar Conexões
        [3] - Setar Agendamentos
        [4] - Visualizar Agendamentos
        [5] - Otimizar Rotas
        [0] - Sair
            ''')
        option = int(input("\tOpção: "))

        match option:
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
                if not connection.connections or not scheduling.schedules:
                    print("\tPrimeiro defina as conexões e o agendamento.")
                    input("\n\tPressione Enter para continuar...")
                    continue

                print("\n\tConjuntos de Conexões Disponíveis:")
                for key in connection.connections.keys():
                    print(f"\t- {key}")
                conn_key = input("\n\tDigite o nome ou identificação do conjunto de conexões que deseja usar: ")

                if conn_key not in connection.connections:
                    print("\tConjunto de conexões não encontrado.")
                    input("\n\tPressione Enter para continuar...")
                    continue

                print("\n\tAgendamentos Disponíveis:")
                for key in scheduling.schedules.keys():
                    print(f"\t- {key}")
                sched_key = input("\n\tDigite o nome ou identificação do agendamento que deseja usar: ")

                if sched_key not in scheduling.schedules:
                    print("\tAgendamento não encontrado.")
                    input("\n\tPressione Enter para continuar...")
                    continue

                optimizer = Optimize(connection.connections[conn_key], scheduling.schedules[sched_key])
                optimizer.optimize_routes()
                
            case _:
                print("\tOpção inválida. Tente novamente.")
                input("\n\tPressione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
