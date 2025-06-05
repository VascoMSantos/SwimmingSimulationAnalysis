import random

DISTANCES = [50, 100, 200, 400]  # distâncias em metros
STYLES = ["freestyle", "backstroke", "breaststroke", "butterfly"]

def create_event():
    ID = random.randint(1, 9999)  # ID aleatório entre 1 e 9999
    distance = random.choice(DISTANCES)
    style = random.choice(STYLES)
    genero = random.choice(["masculino", "feminino"])
    # round = random.choice(["eliminatórias", "semifinais", "finais"])
    return {
        "ID": ID,
        "distance": distance,
        "style": style,
        "genero": genero,
        # "round": round
    }