import psycopg2

# PostgreSQL Connection Details
DB_NAME = "algeval"
DB_USER = "postgres"
DB_PASSWORD = "ashascugpt4o"
DB_HOST = "localhost"
DB_PORT = "5432"

def engine():
    """Reusable function to establish a PostgreSQL database connection."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None

def setup_Instructor():
    """Ensure Instructor table exists before storing data."""
    conn = engine()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Instructor (
                    instructor_name VARCHAR(255) PRIMARY KEY,
                    email TEXT,
                    department TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database Setup Error (Instructor): {e}")

def setup_Sessions():
    """Ensure Sessions table exists before storing data."""
    conn = engine()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Sessions (
                    session_id VARCHAR(255) PRIMARY KEY,
                    instructor_name VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (instructor_name) REFERENCES Instructor(instructor_name) ON DELETE CASCADE
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database Setup Error (Sessions): {e}")

def setup_AnswerKey():
    """Ensure AnswerKey table exists before storing data."""
    conn = engine()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS AnswerKey (
                    id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) NOT NULL,
                    sol_weight FLOAT NOT NULL,
                    fa_weight FLOAT NOT NULL,
                    ak_latex TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (session_id) REFERENCES Sessions(session_id) ON DELETE CASCADE
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database Setup Error (AnswerKey): {e}")

def setup_StudentHAS():
    """Ensure StudentHAS table exists before storing data."""
    conn = engine()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS StudentHAS (
                    id SERIAL PRIMARY KEY,
                    answer_key_id INT NOT NULL,
                    has_latex TEXT NOT NULL,
                    result TEXT NOT NULL,
                    sol_grade FLOAT NOT NULL,
                    fa_grade FLOAT NOT NULL,
                    overall_grade FLOAT NOT NULL,
                    used_asm BOOLEAN NOT NULL DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (answer_key_id) REFERENCES AnswerKey(id) ON DELETE CASCADE
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database Setup Error (StudentHAS): {e}")
