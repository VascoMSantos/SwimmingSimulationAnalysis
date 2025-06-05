def gerar_atletas(num_atletas):
    """
    Gera uma lista de atletas fictícios.
    
    :param num_atletas: Número de atletas a serem gerados.
    :return: Lista de dicionários representando os atletas.
    """
    from models.athlete import generate_athlete
    return [generate_athlete() for _ in range(num_atletas)]

def gerar_eventos(num_eventos):
    """
    Gera uma lista de eventos fictícios.
    
    :param num_eventos: Número de eventos a serem gerados.
    :return: Lista de dicionários representando os eventos.
    """
    from models.event import create_event
    return [create_event() for _ in range(num_eventos)]

def simular_corridas(atletas, eventos, n_competicoes=10):
    """
    Simula corridas para uma lista de eventos e atletas.
    
    :param eventos: Lista de dicionários representando os eventos.
    :param atletas: Lista de dicionários representando os atletas.
    :return: Lista de resultados das corridas.
    """
    # Data aleatória para as competições
    from datetime import datetime, timedelta
    import random
    date = datetime.now()
    resultados = []

    for _ in range(n_competicoes):
        for evento in eventos:
            for atleta in atletas:
                # Ajusta a média e desvio padrão conforme o tipo de prova
                if evento.get("tipo") == "livre":
                    media = 55
                    desvio = 2
                elif evento.get("tipo") == "peito":
                    media = 65
                    desvio = 3
                elif evento.get("tipo") == "costas":
                    media = 60
                    desvio = 2.5
                elif evento.get("tipo") == "borboleta":
                    media = 58
                    desvio = 2
                else:
                    media = 62
                    desvio = 2.5

                tempo = max(0, random.gauss(media, desvio))
                resultados.append({
                    "data": date.strftime("%Y-%m-%d"),
                    "evento": evento.ID,
                    "atleta": atleta.ID,
                    "tempo": tempo
                })
        date += timedelta(days=7)
    return resultados