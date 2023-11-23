import random
import matplotlib.pyplot as plt

# Número de puntos a generar
num_puntos = 1000

# Contadores para puntos dentro y fuera del círculo
dentro_del_circulo = 0
fuera_del_circulo = 0

# Listas para almacenar coordenadas de puntos
x_dentro = []
y_dentro = []
x_fuera = []
y_fuera = []

# Generar puntos aleatorios y determinar si están dentro o fuera del círculo
for _ in range(num_puntos):
    x = random.uniform(-1, 1)  # Generar coordenada x en [-1, 1]
    y = random.uniform(-1, 1)  # Generar coordenada y en [-1, 1]
    distancia_al_origen = x**2 + y**2  # Calcular distancia al origen (radio 1)
    
    if distancia_al_origen <= 1:  # El punto está dentro del círculo
        dentro_del_circulo += 1
        x_dentro.append(x)
        y_dentro.append(y)
    else:
        fuera_del_circulo += 1
        x_fuera.append(x)
        y_fuera.append(y)

# Calcular la estimación de π
pi_estimado = 4 * (dentro_del_circulo / num_puntos)

# Graficar los puntos y el círculo inscrito
plt.figure(figsize=(6, 6))
plt.scatter(x_dentro, y_dentro, color='blue', marker='.')
plt.scatter(x_fuera, y_fuera, color='red', marker='.')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Estimación de Pi usando Monte Carlo')
plt.axis('equal')  # Configurar el aspecto igual para una mejor visualización
plt.gca().add_patch(plt.Circle((0, 0), 1, color='green', fill=False, linestyle='dashed'))
plt.legend(['Dentro del círculo', 'Fuera del círculo'])
plt.show()

print(f'Estimación de Pi: {pi_estimado}')
