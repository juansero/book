# !pip install openai
from openai import OpenAI

# Nos conectamos usando nuestra llave secreta
# (Recuerda al lector que debe poner su propia clave aquí)
TU_CLAVE_OPENAI = "sk-PEGA_AQUI_TU_CLAVE_SECRETA"
cliente = OpenAI(api_key=TU_CLAVE_OPENAI)

print("Despertando a ChatGPT...")

# La magia de los "Roles": Le damos una personalidad y una pregunta
respuesta = cliente.chat.completions.create(
  model="gpt-3.5-turbo", # Usamos un modelo rápido y económico
  messages=[
    # El "System" es la orden secreta que le da personalidad a la IA
    {"role": "system", "content": "Eres un chef experto. Solo respondes con recetas de cocina, pero siempre hablas como el Maestro Yoda de Star Wars."},
    
    # El "User" es lo que pregunta el usuario real
    {"role": "user", "content": "Tengo medio paquete de espaguetis, un huevo y queso rallado. ¿Qué hago?"}
  ]
)

# Imprimimos el mensaje que nos devuelve el modelo
print("\n--- Respuesta de tu Chef Personal ---")
print(respuesta.choices[0].message.content)
