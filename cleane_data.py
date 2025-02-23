import csv
import psycopg2

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        idx = self.hash_function(key)
        if not self.exists(key):
            self.table[idx].append(key)

    def exists(self, key):
        idx = self.hash_function(key)
        return key in self.table[idx]

try:
    with open('file.csv', 'r') as file:
        reader = csv.reader(file)
        head, *body = list(reader)
except FileNotFoundError:
    print("Error: 'file.csv' not found")
    exit()

hash_table = HashTable()
cleaned_file = [head]

for row in body:
    if len(row) < 3:
        continue


    row = [col.strip() for col in row]
    name = ' '.join(row[1].title().split())
    email = row[2].lower()
    city = row[3].title()
    purchase_amount = row[4] if row[4] else "NULL"

    unique_key = f"{name}-{email}-{city}"
    if not hash_table.exists(unique_key) and all(row[:4]):
        hash_table.insert(unique_key)
        cleaned_file.append([row[0], name, email, city, purchase_amount, row[5]])


with open('cleaned_file.csv', 'w', newline='') as file:
    csv.writer(file).writerows(cleaned_file)

print('Data cleaned successfully!')


try:
    with psycopg2.connect(dbname='postgres', user='postgres', password='123', host="localhost", port="5432") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                city VARCHAR(50),
                purchase_amount DECIMAL(10,2)
            )
        """)

        for row in cleaned_file[1:]:
            try:
                purchase_amount = float(row[4]) if row[4] != "NULL" else None
            except ValueError:
                purchase_amount = None

            cursor.execute("""
                INSERT INTO data (name, email, city, purchase_amount)
                VALUES (%s, %s, %s, %s) ON CONFLICT (email) DO NOTHING
            """, (row[1], row[2], row[3], purchase_amount))

        print("Successfully inserted into the database!")

except psycopg2.Error as e:
    print("Database connection failed:", e)
