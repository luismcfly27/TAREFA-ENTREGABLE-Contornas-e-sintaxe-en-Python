# Importamos a librería Faker para xerar datos falsos
from faker import Faker
import random

# Inicializamos Faker en español
fake = Faker("es_ES")

# Creamos un dicionario baleiro para gardar os usuarios
usuarios = {}

print("--- CREANDO 15 USUARIOS ---")

# Facemos un bucle que se repita 15 veces (do 1 ao 15)
for codigo in range(1, 16):
    # Para cada número, gardamos os datos do usuario nun dicionario
    usuarios[codigo] = {
        "nome": fake.name(),
        "direccion": fake.address().replace("\n", ", "),
        "correo": fake.email(),
        "telefono": fake.phone_number(),
    }

print("\n--- LISTAXE DE USUARIOS ---")

# Percorrémos o dicionario para mostrar os datos un a un
for codigo in usuarios:
    print("Código:", codigo)
    print("Nome:", usuarios[codigo]["nome"])
    print("Dirección:", usuarios[codigo]["direccion"])
    print("Correo:", usuarios[codigo]["correo"])
    print("Teléfono:", usuarios[codigo]["telefono"])
    print("-" * 30)

# Seleccionamos un número aleatorio entre o 1 e o 15
codigo_afortunado = random.randint(1, 15)

# Buscamos o nome dese usuario afortunado
nome_afortunado = usuarios[codigo_afortunado]["nome"]

print("\n" + "=" * 50)
print("O usuario chamado", nome_afortunado, "foi o afortunado!")
print("=" * 50)
