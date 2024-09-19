# Versão 1 do Leilão de Entregas: Criar um algoritmo básico, sem a necessidade de cálculos otimizados para obter o melhor resultado entregas e bônus.

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
        departure_time, destination, bonus = delivery
        travel_time = connection_map[current_location].get(destination, float('inf'))

        if current_time <= departure_time:
            current_time += travel_time
            accumulated_profit += bonus
            current_time += travel_time
            current_location = 'A'

    return accumulated_profit

raw_matrix = [
    ['A', 'B', 'C', 'D'],
    [0, 5, 0, 2],
    [5, 0, 3, 0],
    [0, 3, 0, 8],
    [2, 0, 8, 0]
]

delivery_list = [
    (0, 'B', 1),
    (5, 'C', 10),
    (10, 'D', 8)
]

connection_map = process_matrix(raw_matrix)
total_profit = calculate_total_profit(connection_map, delivery_list)

print(f"Lucro Total: {total_profit}")
