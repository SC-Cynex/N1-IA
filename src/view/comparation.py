import time
import matplotlib.pyplot as plt
from models.optimize import Optimize
from view.version1 import calculate_total_profit, process_matrix

def comparation(connection, scheduling):
    if not connection.connections or not scheduling.schedules:
        print("\tPrimeiro defina as conexões e o agendamento.")
        input("\n\tPressione Enter para continuar...")
        return
    
    print("\n\tConjuntos de Conexões Disponíveis:")
    for key in connection.connections.keys():
        print(f"\t- {key}")
    conn_key = input("\n\tDigite o nome ou identificação do conjunto de conexões que deseja usar: ")

    if conn_key not in connection.connections:
        print("\tConjunto de conexões não encontrado.")
        input("\n\tPressione Enter para continuar...")
        return

    print("\n\tAgendamentos Disponíveis:")
    for key in scheduling.schedules.keys():
        print(f"\t- {key}")
    sched_key = input("\n\tDigite o nome ou identificação do agendamento que deseja usar: ")

    if sched_key not in scheduling.schedules:
        print("\tAgendamento não encontrado.")
        input("\n\tPressione Enter para continuar...")
        return

    print("\n\tExecutando Version 1...")
    start_time_v1 = time.time()
    raw_matrix = connection.connections[conn_key]
    delivery_list = scheduling.schedules[sched_key]
    destinations = list(connection.connections.keys())
    connection_map = process_matrix([destinations] + raw_matrix)
    total_profit_v1 = calculate_total_profit(connection_map, delivery_list)
    end_time_v1 = time.time()
    execution_time_v1 = end_time_v1 - start_time_v1
    print(f"\tVersion 1 - Lucro: {total_profit_v1}, Tempo de Execução: {execution_time_v1:.6f} segundos")

    print("\n\tExecutando Version 2...")
    start_time_v2 = time.time()
    optimizer = Optimize(connection.connections[conn_key], scheduling.schedules[sched_key])
    total_profit_v2 = optimizer.optimize_routes() or 0
    end_time_v2 = time.time()
    execution_time_v2 = end_time_v2 - start_time_v2
    print(f"\tVersion 2 - Lucro: {total_profit_v2}, Tempo de Execução: {execution_time_v2:.6f} segundos")

    versions = ['Version 1', 'Version 2']
    profits = [total_profit_v1, total_profit_v2]
    execution_times = [execution_time_v1, execution_time_v2]

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.bar(versions, profits, color=['orange', 'yellow'])
    plt.title('Comparação de Lucro')
    plt.xlabel('Versões')
    plt.ylabel('Lucro (Bônus)')

    plt.subplot(1, 2, 2)
    plt.bar(versions, execution_times, color=['purple', 'black'])
    plt.title('Comparação de Tempo de Execução')
    plt.xlabel('Versões')
    plt.ylabel('Tempo de Execução (segundos)')

    plt.tight_layout()
    plt.show()
