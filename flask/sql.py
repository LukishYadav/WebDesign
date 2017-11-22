import sqlite3


#with sqlite3.connect("sample.db") as connection:
#	c=connection.cursor()
#	#c.execute("""DROP TABLE posts""")
#	c.execute("""CREATE TABLE posts(title TEXT,description TEXT)""")
#	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
#	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')


conn=sqlite3.connect('tutorial.db')
c=conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')


def data_entry():
		c.execute("INSERT INTO stuffToPlot VALUES(145123542, '2016-01-01', 'Python', 5)")
		conn.commit()
		c.close()
		conn.close()

create_table()
data_entry()