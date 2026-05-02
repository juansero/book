import numpy as np
import matplotlib.pyplot as plt

# 1. Creamos una "imagen" básica (un cuadrado blanco sobre fondo negro)
imagen_real = np.zeros((64, 64))
imagen_real[20:44, 20:44] = 1.0  # Dibujamos el cuadrado

# 2. La estropeamos por completo añadiendo mucho ruido (estática)
ruido_total = np.random.normal(0, 0.6, (64, 64))
imagen_ruidosa = imagen_real + ruido_total

# 3. Simulamos el trabajo de la IA: Limpiar el ruido en varios "pasos"
pasos_de_limpieza = 4

plt.figure(figsize=(15, 4))

for i in range(pasos_de_limpieza):
    # En la vida real, una Red Neuronal adivinaría el ruido en cada paso.
    # Aquí simulamos cómo se va restando poco a poco:
    fraccion_limpieza = i / (pasos_de_limpieza - 1) 
    imagen_limpiando = imagen_ruidosa - (ruido_total * fraccion_limpieza)
    
    # ¡Dibujamos cada paso para ver la magia!
    plt.subplot(1, pasos_de_limpieza, i+1)
    plt.imshow(imagen_limpiando, cmap='gray')
    plt.title(f"Paso {i+1}")
    plt.axis('off')

plt.show()
