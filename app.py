from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app=Flask(__name__)
app.secret_key = 'rakybakyshin9595'


mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='library'
)

@app.route("/", methods=['GET', 'POST'])
def books():
    if request.method == 'POST' and 'bookname' in request.form:
        bookdata=request.form.get('bookname')
        sql='INSERT INTO books (NameOfBook) VALUES (%s)'
        val=(bookdata,)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        flash('Your book has been inserted successfully!', 'success')
        return redirect(url_for('books'))
    return render_template('index.html')

app.run()