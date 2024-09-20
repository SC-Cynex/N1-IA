from models.optimize import Optimize

def version2(connection, scheduling):
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

    optimizer = Optimize(connection.connections[conn_key], scheduling.schedules[sched_key])
    optimizer.optimize_routes()
