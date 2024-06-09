from flask import Flask, render_template, request
import mysql.connector

app=Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def library():
    connection= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='library'
    )

    cursor=connection.cursor()

    books_data=''

    if request.method == 'POST':
        bookdata=request.form.get('bookname')
        descdata=request.form.get('description')
        datedata=request.form.get('releasedate')
        authordata=request.form.get('authorname')

        cursor.execute('INSERT INTO authors (Name) VALUES (%s)', (authordata,))
        lastAuthorId=cursor.lastrowid

        cursor.execute('INSERT INTO books (Name, Description, Release_Date, Author_ID) VALUES (%s, %s, %s, %s)', (bookdata, descdata, datedata, lastAuthorId))
        connection.commit()

        cursor.execute("SELECT books.ID, books.Name, books.Description, books.Release_Date, books.created_at, books.updated_at, books.Author_ID, authors.Name AS author_name FROM books LEFT JOIN authors ON books.Author_ID=authors.ID;")
        books_data = cursor.fetchall()

        cursor.close()
        connection.close()
    return render_template('index.html', books_data=books_data)

app.run()