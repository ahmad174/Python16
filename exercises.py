# Sixteenth Day Exercise
from flask import *
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/enternew')
def newStudent():
	return render_template('student.html')
	
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			name = request.form['name']
			address = request.form['address']
			city = request.form['city']
			pin = request.form['pin']
			
			with sql.connect('database.db') as con:
				cur = con.cursor()
			
				cur.execute('insert into students values (?, ?, ?, ?)', (name, address, city, pin))
	
				con.commit()
				msg = 'Record successfully added'
		
		except:
			con.callback()
			msg = 'error in insert operation'
			
		finally:
			return render_template('result.html', msg = msg)
			con.close()
			
@app.route('/list')
def data():
	con = sql.connect('database.db')
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute('select * from students')
	
	rows = cur.fetchall()
	return render_template('list.html', data = rows)
	
	
if __name__ == '__main__':
	app.run()
