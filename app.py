import psycopg2

# "postgresql://(username):(password)@(servername/url):(port)/(dbname)"
url = "postgresql://postgres:pw@127.0.0.1:5432/python-postgresql-course"
connection = psycopg2.connect(url)

# need a cursor in psycopg2
cursor = connection.cursor()

cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
