import numpy as np

class PSO:
    def __init__(self, connections, deliveries, num_particles=5, max_iterations=100):
        self.connections = connections
        self.deliveries = deliveries
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.particles = self.initialize_particles()

    def initialize_particles(self):
        particles = []
        num_deliveries = len(self.deliveries)
        for _ in range(self.num_particles):
            sequence = np.random.permutation(num_deliveries)
            particles.append(sequence)
        return particles

    def optimize(self):
        best_global_sequence = None
        best_global_profit = float('-inf')

        for _ in range(self.max_iterations):
            for particle in self.particles:
                profit = self.calculate_profit(particle)
                if profit > best_global_profit:
                    best_global_profit = profit
                    best_global_sequence = particle

            self.particles = [np.random.permutation(len(self.deliveries)) for _ in range(self.num_particles)]
        
        return best_global_sequence, best_global_profit

    def calculate_profit(self, sequence):
        total_time = 0
        total_bonus = 0
        start_location = self.deliveries[sequence[0]][0]
        
        for i in range(len(sequence)):
            delivery = self.deliveries[sequence[i]]
            origin = delivery[0]
            destination = delivery[1]

            if i > 0:
                prev_delivery = self.deliveries[sequence[i - 1]]
                prev_destination = prev_delivery[1]

                # Map delivery points to indices
                start_idx = self.delivery_point_to_index(prev_destination)
                end_idx = self.delivery_point_to_index(origin)

                if start_idx is not None and end_idx is not None:
                    total_time += self.connections[start_idx][end_idx]

            total_bonus += delivery[3]

            start_location = destination

        end_idx = self.delivery_point_to_index(start_location)
        start_idx = self.delivery_point_to_index(self.deliveries[sequence[0]][0])
        if start_idx is not None and end_idx is not None:
            total_time += self.connections[start_idx][end_idx]

        profit = total_bonus - total_time
        return profit

    def delivery_point_to_index(self, point):
        try:
            return next(index for index, delivery in enumerate(self.deliveries) if delivery[1] == point)
        except StopIteration:
            return None
