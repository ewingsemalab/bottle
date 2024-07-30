import sqlite3
import csv

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

def load_csv_to_db(cursor, csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO users (id, name, age) 
                VALUES (:id, :name, :age)
            ''', row)

def main():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create table
    create_table(cursor)

    # Load CSV data into database
    csv_file_path = 'data.csv'
    load_csv_to_db(cursor, csv_file_path)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
