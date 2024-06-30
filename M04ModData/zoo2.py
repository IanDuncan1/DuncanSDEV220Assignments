import zoo
zoo.hours()
import zoo as menagerie
menagerie.hours()
import sqlite3
import sqlalchemy 
connection = sqlite3.connect('books.db')
engine = sqlalchemy.create_engine('sqlite:///books.db')
cursor=connection.cursor()
command1 = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT, year INTEGER)'
cursor.execute(command1)
cursor.execute("INSERT INTO books VALUES ('The Weirdstone of Brisingamen','Alan Garner',1960)")
cursor.execute("INSERT INTO books VALUES ('Perdido Street Station','China Miéville',2000)")
cursor.execute("INSERT INTO books VALUES ('Thud!','Terry Pratchett',2005)")
cursor.execute("INSERT INTO books VALUES ('The Spellman Files','Lisa Lutz',2007)")
cursor.execute("INSERT INTO books VALUES ('Small Gods','Terry Pratchett',1992)")
result = connection.execute("SELECT title FROM books ORDER BY title ASC ")
print(result.fetchall())