import psycopg2

import environ
env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5445,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id SERIAL PRIMARY KEY,
             task TEXT NOT NULL,
             completed BOOLEAN,
             due_date DATE,
             completion_date DATE,
             priority INTEGER)''')

# Insert sample tasks into the tasks table
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task1', True, '2023-06-28', '2023-07-01', 1))
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task2', True, '2023-06-29', '2023-07-02', 2))
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task3', False, '2023-07-05', None, 3))
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task4', False, '2023-07-08', None, 4))
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task5', False, '2023-07-10', None, 5))
cursor.execute("INSERT INTO tasks (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Task6', False, '2023-07-10', None, 6))

# Commit the changes and close the connection
conn.commit()
conn.close()