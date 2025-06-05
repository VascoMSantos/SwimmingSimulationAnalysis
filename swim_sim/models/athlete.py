import random
import names

STYLES = ["freestyle", "backstroke", "breaststroke", "butterfly"]
NATIONALITIES = ["Portugal", "Spain", "USA", "Brazil", "France"]

def generate_athlete():
    ID = random.randint(1, 9999)  # ID aleatório entre 1 e 9999
    name = names.get_full_name()
    nationality = random.choice(NATIONALITIES)
    age = random.randint(16, 30)
    sex = random.choice(['masculino', 'feminino'])
    preferred_style = random.choice(STYLES)
    # base_time_100m = round(random.uniform(50.0, 60.0), 2)  # tempo base em segundos

    return {
        "ID": ID,
        "name": name,
        "nationality": nationality,
        "age": age,
        "sex": sex,
        "preferred_style": preferred_style,
        # "base_time_100m": base_time_100m
    }