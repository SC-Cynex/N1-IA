import matplotlib.pyplot as plt
import numpy as np

def visualize_results(best_route, best_cost, deliveries):
    num_deliveries = len(deliveries)
    x = np.arange(num_deliveries)
    y = [deliveries[i][2] for i in best_route]

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='blue')
    plt.xlabel('Delivery Index')
    plt.ylabel('Time (minutes)')
    plt.title('Delivery Times 1 for Optimized Route')
    plt.xticks(x, [f"{deliveries[i][0]} -> {deliveries[i][1]}" for i in best_route], rotation=45)
    plt.tight_layout()             
    plt.show()