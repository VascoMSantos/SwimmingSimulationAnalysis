import random

def simulate_race(event, athletes):
    results = []
    for athlete in athletes:
        variation = random.uniform(-0.03, 0.03)
        race_time = round(athlete["base_time_100m"] * (1 + variation), 2)
        results.append({"athlete": athlete, "time": race_time})

    # Ordenar por tempo e atribuir posição
    results.sort(key=lambda x: x["time"])
    for i, result in enumerate(results):
        result["position"] = i + 1

    return results