from db.connection import get_connection

def insert_athlete(athlete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO athletes (name, nationality, age, preferred_style, base_time_100m)
        VALUES (?, ?, ?, ?, ?)
    ''', (athlete["name"], athlete["nationality"], athlete["age"], athlete["preferred_style"], athlete["base_time_100m"]))
    athlete_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return athlete_id

def insert_event(event):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (distance, style, round)
        VALUES (?, ?, ?)
    ''', (event["distance"], event["style"], event["round"]))
    event_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return event_id

def insert_result(event_id, athlete_id, time, position):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (event_id, athlete_id, time, position)
        VALUES (?, ?, ?, ?)
    ''', (event_id, athlete_id, time, position))
    conn.commit()
    conn.close()