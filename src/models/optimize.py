from models.pso import PSO

class Optimize:
    def __init__(self, connections, deliveries):
        self.connections = connections
        self.deliveries = deliveries

    def optimize_routes(self):
        if not self.connections or not self.deliveries:
            print("\tDefina primeiro as conexões e os agendamentos de entregas.")
            input("\n\tPressione Enter para continuar...")
            return 0

        pso = PSO(self.connections, self.deliveries)
        best_route, best_profit = pso.optimize()

        print("\n\tMelhor Rota Encontrada:")
        total_bonuses = 0
        for index in best_route:
            delivery = self.deliveries[index]
            print(f"\tDestino: {delivery[1]}, Bônus: {delivery[3]}")
            total_bonuses += delivery[3]
        
        print(f"\n\tBônus Total: {total_bonuses}")

        return total_bonuses

