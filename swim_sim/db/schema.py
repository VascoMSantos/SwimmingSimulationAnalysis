from db.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS athletes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nationality TEXT,
            age INTEGER,
            preferred_style TEXT,
            base_time_100m REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distance INTEGER NOT NULL,
            style TEXT NOT NULL,
            round TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            athlete_id INTEGER NOT NULL,
            time REAL NOT NULL,
            position INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (athlete_id) REFERENCES athletes(id)
        )
    ''')

    conn.commit()
    conn.close()