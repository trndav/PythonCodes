import matplotlib.pyplot as plt
import numpy as np

# Definiranje podataka o točkama i udaljenostima
point_names = ['LA', 'London', 'Dubai', 'Sydney', 'Johannesburg', 'Tokyo']
distances = [('LA', 'London', 5.5), ('LA', 'Dubai', 8.3), ('LA', 'Sydney', 12),
             ('Sydney', 'London', 17), ('LA', 'Johannesburg', 13),
             ('LA', 'Tokyo', 8.8), ('London', 'Johannesburg', 8),
             ('London', 'Tokyo', 9.6), ('Johannesburg', 'Dubai', 6.4),
             ('London', 'Dubai', 5.4), ('Johannesburg', 'Tokyo', 13.5),
             ('Tokyo', 'Sydney', 8), ('Dubai', 'Sydney', 12)]

# Inicijalizacija točaka
points = {}

# Postavljanje početne točke
points[point_names[0]] = (0, 0)


# Funkcija za računanje pozicija točaka
def calculate_positions():
    # First pass: Place points relative to LA
    for (point1, point2, distance) in distances:
        if point1 == 'LA' and point2 not in points:
            angle = len(points) * (2 * np.pi / 3
                                   )  # More natural angular distribution
            x_new = points[point1][0] + distance * np.cos(angle)
            y_new = points[point1][1] + distance * np.sin(angle)
            points[point2] = (x_new, y_new)

    # Second pass: Adjust positions based on other distances
    for _ in range(20):  # More iterations for better convergence
        for (point1, point2, distance) in distances:
            if point1 in points and point2 in points:
                x1, y1 = points[point1]
                x2, y2 = points[point2]
                current_dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if abs(current_dist - distance) > 0.1:
                    dx = x2 - x1
                    dy = y2 - y1
                    factor = (distance / current_dist - 1) * 0.3
                    if point2 != 'LA':  # Keep LA fixed
                        points[point2] = (x2 + dx * factor, y2 + dy * factor)


# Funkcija za crtanje grafa
def plot_points():
    plt.figure(figsize=(8, 8))
    for point, (x, y) in points.items():
        plt.scatter(x, y)
        plt.text(x, y, f' {point}', fontsize=12, ha='right')

    plt.xlabel('X osa')
    plt.ylabel('Y osa')
    plt.title('Crtanje točaka na koordinatnom sustavu')
    plt.grid(True)
    plt.show()


# Pozivanje funkcija
calculate_positions()
plot_points()
