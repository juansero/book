# !pip install transformers
from transformers import pipeline

print("Descargando el cerebro del modelo BETO (Español)...")

# Cargamos un modelo experto en ESPAÑOL
# Usamos 'sentiment-analysis' para que la IA nos diga la emoción del texto
analista = pipeline("sentiment-analysis", model="finiteautomata/beto-sentiment-analysis")

# Probamos una frase con contexto
frase = "¡Este nivel del castillo es increíble, me encantan los gráficos!"

print(f"\nAnalizando la frase: '{frase}'")

# ¡La magia de la Atención ocurre aquí!
resultado = analista(frase)

print(f"\nResultado de la IA: {resultado}")
