from flask import Flask,render_template, request, jsonify
from flask_mysqldb import MySQL 

app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='restapi'


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method=="POST":
        StudentID = request.form['StudentID']
        StudentName = request.form['StudentName']
        StudentAddress = request.form['StudentAddress']
        Grade = request.form['Grade']


        cur = mysql.connection.cursor()

        cur.execute("Insert Into student (StudentID,StudentName,StudentAddress,Grade) VALUES (%s,%s,%s,%s)",(StudentID,StudentName,StudentAddress,Grade))
        mysql.connection.commit()
        cur.close()

        return 'Successfully update record in database'
    return render_template("index.html")



@app.route('/Students')
def get_users():
    cur = mysql.connection.cursor()
    users = cur.execute('Select * FROM student')
    if users >0:
        userDetails = cur.fetchall()
    cur.close()
    return render_template('Students.html',users=userDetails)


if __name__ == "__main__":
    app.run(debug=True)