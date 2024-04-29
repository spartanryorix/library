from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector
import sys

app=Flask(__name__)
app.secret_key = 'rakybakyshine9595'


#mydb= mysql.connector.connect(
    #host='localhost',
    #user='root',
    #password='',
    #database='library'
#)

@app.route("/", methods=['GET', 'POST'])
def data():
    mydb= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='library'
    )
    books_data=''
    authors_data=''
    if request.method == 'POST':
        bookdata=request.form.get('bookname')
        descdata=request.form.get('description')
        datedata=request.form.get('releasedate')

        authordata=request.form.get('authorname')
        query2='INSERT INTO authors (Name) VALUES (%s)'
        val2=(authordata,)
        mycursor = mydb.cursor()
        mycursor.execute(query2, val2)
        lastAuthorId=mycursor.lastrowid
        authordata=mycursor.fetchall()
        mydb.commit()

        query='INSERT INTO books (Name, Description, Release_Date, Author_ID) VALUES (%s, %s, %s, %s)'
        val=(bookdata, descdata, datedata, lastAuthorId)
        mycursor = mydb.cursor()
        mycursor.execute(query, val)
        #query5="SELECT * FROM authors WHERE ID='ID'"
        #mycursor.execute(query5)
        #print(authordata)


        mycursor = mydb.cursor(dictionary=True)
        query3='SELECT books.ID, books.Name, books.Description, books.Release_Date, books.created_at, books.updated_at, books.Author_ID, authors.Name AS author_name FROM books LEFT JOIN authors ON books.Author_ID=authors.ID'
        mycursor.execute(query3)
        books_data = mycursor.fetchall()
        print(books_data)
        print("/////////")


        query4='SELECT * FROM authors'
        mycursor.execute(query4)
        authors_data = mycursor.fetchall()
        print(authors_data)
        

        mycursor.close()
        mydb.close()
        flash('Data added successfully!', 'success')
    return render_template('index.html', books_data=books_data, authors_data=authors_data)

if __name__ == "__main__":
    app.run()