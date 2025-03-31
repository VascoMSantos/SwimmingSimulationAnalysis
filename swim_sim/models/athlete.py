import random
import names

STYLES = ["freestyle", "backstroke", "breaststroke", "butterfly"]
NATIONALITIES = ["Portugal", "Spain", "USA", "Brazil", "France"]

def generate_athlete():
    name = names.get_full_name()
    nationality = random.choice(NATIONALITIES)
    age = random.randint(16, 30)
    preferred_style = random.choice(STYLES)
    base_time_100m = round(random.uniform(50.0, 60.0), 2)  # tempo base em segundos

    return {
        "name": name,
        "nationality": nationality,
        "age": age,
        "preferred_style": preferred_style,
        "base_time_100m": base_time_100m
    }