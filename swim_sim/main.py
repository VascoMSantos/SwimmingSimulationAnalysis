from db.schema import create_tables
from models.athlete import generate_athlete
from models.event import create_event
from simulation.simulate_race import simulate_race
from storage.insert import insert_athlete, insert_event, insert_result


def main():
    create_tables()

    # Gerar atletas
    athletes = [generate_athlete() for _ in range(8)]
    athlete_ids = [insert_athlete(a) for a in athletes]

    # Criar evento
    event = create_event()
    event_id = insert_event(event)

    # Simular corrida
    results = simulate_race(event, athletes)

    # Guardar resultados
    for i, result in enumerate(results):
        athlete_index = athletes.index(result["athlete"])
        insert_result(event_id, athlete_ids[athlete_index], result["time"], result["position"])

if __name__ == "__main__":
    main()