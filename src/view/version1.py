def process_matrix(raw_matrix):
    destinations = raw_matrix[0]
    matrix = raw_matrix[1:]
    connection_map = {}

    for i, origin in enumerate(destinations):
        connection_map[origin] = {}
        for j, destination in enumerate(destinations):
            if matrix[i][j] != 0:
                connection_map[origin][destination] = matrix[i][j]

    return connection_map

def calculate_total_profit(connection_map, delivery_list):
    accumulated_profit = 0
    current_time = 0
    current_location = 'A'

    for delivery in delivery_list:
        origin, destination, time, bonus = delivery
        departure_time = 0 

        travel_time = connection_map.get(current_location, {}).get(destination, float('inf'))

        if current_time <= departure_time:
            current_time += travel_time
            accumulated_profit += bonus
            current_time += travel_time
            current_location = 'A'

    return accumulated_profit

def version1(connection, scheduling):
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

    raw_matrix = connection.connections[conn_key]
    delivery_list = scheduling.schedules[sched_key]

    destinations = list(connection.connections.keys())

    connection_map = process_matrix([destinations] + raw_matrix)

    total_profit = calculate_total_profit(connection_map, delivery_list)

    print(f"\tLucro Total: {total_profit}")
