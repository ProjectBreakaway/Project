import sqlite3
from sqlite3 import Error

NULL=None

def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")

    _conn.execute("BEGIN")
    
    try:
        sql ="""CREATE TABLE user(
                u_Username char(20) not null,
                u_Password varchar(30) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE review(
                r_reviewKey decimal(4, 0) not null, 
                r_author varchar(20) not null, 
                r_movieTitle varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE director(
                d_Name varchar(30) not null, 
                d_Year decimal(4, 0) not null,
                d_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE producer(
                p_Name varchar(30) not null, 
                p_Year decimal(4, 0) not null,
                p_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE actor(
                a_Name varchar(30) not null, 
                a_Year decimal(4, 0) not null,
                a_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE composer(
                c_Name varchar(30) not null, 
                c_Year decimal(4, 0) not null,
                c_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE studio(
                s_Name varchar(30) not null, 
                s_Year decimal(4, 0) not null,
                s_President varchar(30) not null,
                s_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE president(
                pre_Name varchar(30) not null,
                pre_Year decimal(4, 0) not null, 
                pre_Studio varchar(30) not null,
                pre_YearsRan decimal(3) not null)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE movie(
                m_Title varchar(40) not null, 
                m_genre char(10) not null, 
                m_Year decimal(4, 0) not null, 
                m_Revenue decimal(12, 2) not null, 
                m_Director varchar(40) not null,
                m_DirectorTwo varchar(40),
                m_Producer varchar(40) not null,
                m_ProducerTwo varchar(40),
                m_ProducerThree varchar(40),
                m_Actor varchar(40) not null,
                m_ActorTwo varchar(40),
                m_ActorThree varchar(40),
                m_Composer varchar(40) not null,
                m_Studio varchar(40) not null,
                m_Review decimal(4, 0)
)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE earliestHere (
                e_Title varchar(40) not null,
                e_Director varchar(40),
                e_DirectorTwo varchar(40),
                e_Producer varchar(40),
                e_ProducerTwo varchar(40),
                e_ProducerThree varchar(40),
                e_Actor varchar(40),
                e_ActorTwo varchar(40),
                e_ActorThree varchar(40),
                e_Composer varchar(40),
                e_Studio varchar(40))
"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE workedWith(
                w_Name varchar(40) not null, 
                w_Director varchar(40),
                w_DirectorTwo varchar(40),
                w_DirectorThree varchar(40),
                w_DirectorFour varchar(40),
                w_DirectorFive varchar(40),
                w_Producer varchar(40),
                w_ProducerTwo varchar(40),
                w_ProducerThree varchar(40),
                w_ProducerFour varchar(40),
                w_ProducerFive varchar(40),
                w_Actor varchar(40),
                w_ActorTwo varchar(40),
                w_ActorThree varchar(40),
                w_ActorFour varchar(40),
                w_ActorFive varchar(40),
                w_Composer varchar(40), 
                w_ComposerTwo varchar(40)
)"""
        _conn.execute(sql)
        
        sql ="""CREATE TABLE year(
                y_year decimal(4, 0) not null, 
                y_Movie varchar(40), 
                y_MovieTwo varchar(40),
                y_MovieThree varchar(40),
                y_MovieFour varchar(40),
                y_MovieFive varchar(40),
                y_Director varchar(40),
                y_DirectorTwo varchar(40),
                y_DirectorThree varchar(40),
                y_DirectorFour varchar(40),
                y_DirectorFive varchar(40),
                y_Producer varchar(40),
                y_ProducerTwo varchar(40),
                y_ProducerThree varchar(40),
                y_ProducerFour varchar(40),
                y_ProducerFive varchar(40),
                y_Actor varchar(40),
                y_ActorTwo varchar(40),
                y_ActorThree varchar(40),
                y_ActorFour varchar(40),
                y_ActorFive varchar(40),
                y_Composer varchar(40),
                y_ComposerTwo varchar(40),
                y_ComposerThree varchar(40),
                y_ComposerFour varchar(40),
                y_ComposerFive varchar(40),
                y_President varchar(40),
                y_Studio varchar(40),
                y_StudioTw varchar(40)
)"""
        _conn.execute(sql)
        
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE user"
        _conn.execute(sql)
        sql = "DROP TABLE review"
        _conn.execute(sql)
        sql = "DROP TABLE director"
        _conn.execute(sql)
        sql = "DROP TABLE producer"
        _conn.execute(sql)
        sql = "DROP TABLE actor"
        _conn.execute(sql)
        sql = "DROP TABLE composer"
        _conn.execute(sql)
        sql = "DROP TABLE studio"
        _conn.execute(sql)
        sql = "DROP TABLE president"
        _conn.execute(sql)
        sql = "DROP TABLE movie"
        _conn.execute(sql)
        sql = "DROP TABLE earliestHere"
        _conn.execute(sql)
        sql = "DROP TABLE workedWith"
        _conn.execute(sql)
        sql = "DROP TABLE year"
        _conn.execute(sql)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)
    
def insertUser(_conn, _username, _password):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert User")
    try: 
        sql = "INSERT INTO user VALUES(?, ?)"
        args = [_username, _password]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")

def populateUser(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate User")
    
    insertUser(_conn,"Michael Moua", "qwertyuip")
    insertUser(_conn,"Paul Kim", "asdfghjkl")
    
    print("++++++++++++++++++++++++++++++++++")

def deleteUserWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete User")
    try:
        sql="delete from user where u_Username =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteUserWPassword(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete User")
    try:
        sql="delete from user where u_Password =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateUserName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update User")
    try:
        sql="update user set u_Password as ? where u_Username=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateUserPassword(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update User")
    try:
        sql="update user set u_Username as ? where u_Username=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
   
def insertReview(_conn, _reviewKey, _author, _movieTitle):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Review")
    try: 
        sql = "INSERT INTO review VALUES(?, ?, ?)"
        args = [_reviewKey, _author, _movieTitle]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateReview(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Review")
    
    insertReview(_conn, 1, "Paul Kim", "The Lion King")
    insertReview(_conn, 2, "Michael Moua", "If")
    insertReview(_conn, 3, "Paul Kim", "Schindler's List")
    insertReview(_conn, 4, "Michael Moua", "Horizons West")
    insertReview(_conn, 5, "Paul Kim", "Sorcerer's Stone")
    insertReview(_conn, 6, "Paul Kim", "Tron")
    insertReview(_conn, 7, "Michael Moua", "Batteries Not Included")
    insertReview(_conn, 8, "Michael Moua", "Duel")
    insertReview(_conn, 9, "Michael Moua", "Fear and Desire")
    insertReview(_conn, 10, "Paul Kim", "Dr Strangelove")
    insertReview(_conn, 11, "Michael Moua", "Max Dugan Returns")
    insertReview(_conn, 12, "Michael Moua", "Ironweed")
    insertReview(_conn, 13, "Michael Moua", "Nijinsky")
    insertReview(_conn, 14, "Michael Moua", "Moonlighting")
    insertReview(_conn, 15, "Michael Moua", "Diamond Head")
    insertReview(_conn, 16, "Paul Kim", "A Clockwork Orange")
    
    print("++++++++++++++++++++++++++++++++++")
 
def deleteReviewWKey(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Review")
    try:
        sql="delete from review where r_reviewKey =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteReviewWAuthor(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Review")
    try:
        sql="delete from review where r_reviewKey =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def deleteReviewWMovieTitle(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Review")
    try:
        sql="delete from review where r_reviewKey =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateReviewAuthor(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Review")
    try:
        sql="update user set r_author as ? where r_reviewKey=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateReviewMovie(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Review")
    try:
        sql="update user set r_movieTitle as ? where r_reviewKey=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def insertProducer(_conn, _name, _year, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Producer")
    try: 
        sql = "INSERT INTO producer VALUES(?, ?, ?)"
        args = [_name, _year, _firstFilm]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
        
def populateProducer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Producer")
    
    insertProducer(_conn, "Gerald Molen", 1935, "Batteries Not Included")
    insertProducer(_conn, "David Hayman", 1948, "Sorcerer's Stone")
    insertProducer(_conn, "Steven Spielberg", 1946, "Schindler's List")
    insertProducer(_conn, "Michael Medwin", 1923, "If")
    insertProducer(_conn, "Stanley Kubrick", 1928, "Fear and Desire")
    insertProducer(_conn, "Donald Kushner", 1945, "Tron")
    insertProducer(_conn, "Neil Simon", 1927, "Max Dugan Returns")
    insertProducer(_conn, "Ronald Schwary", 1944, "Batteries Not Included")
    insertProducer(_conn, "Richard Matheson", 1926, "Duel")
    insertProducer(_conn, "Keith Barish", 1944, "Ironweed")
    insertProducer(_conn, "Marcia Nasatir", 1926, "Ironweed")
    insertProducer(_conn, "Herbert Ross", 1927, "Max Dugan Returns")
    insertProducer(_conn, "Hugh Wheeler", 1912, "Nijinsky")
    insertProducer(_conn, "Romola Nijinsky", 1891, "Nijinsky")
    insertProducer(_conn, "Vaslav Nijinsky", 1890, "Nijinsky")
    insertProducer(_conn, "Mark Shivas", 1938, "Moonlighting")
    insertProducer(_conn, "Jerzy Skolimowski", 1937, "Moonlighting")
    insertProducer(_conn, "Michael White", 1936, "Moonlighting")
    insertProducer(_conn, "Jerry Bresler", 1908, "Diamond Head")
    insertProducer(_conn, "Albert Cohen", 1903, "Horizons West")
    insertProducer(_conn, "Bill Butler", 1921, "A Clockwork Orange")
    insertProducer(_conn, "Lindsay Anderson", 1923, "If")
    
    
    print("++++++++++++++++++++++++++++++++++")

def deleteProducerWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Producer")
    try:
        sql="delete from producer where p_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def deleteProducerWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Producer")
    try:
        sql="delete from producer where p_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteProducerWFirstFilm(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Producer")
    try:
        sql="delete from producer where p_FirstFilm =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateProducerName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Producer")
    try: 
        sql="update producer set p_Name as ? where p_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateProducerYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Producer")
    try: 
        sql="update producer set p_Year as ? where p_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateProducerFirstFilm(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Producer")
    try: 
        sql="update producer set p_FirstFilm as ? where p_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def insertDirector(_conn, _name, _year, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Director")
    try: 
        sql = "INSERT INTO director VALUES(?, ?, ?)"
        args = [_name, _year, _firstFilm]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def populateDirector(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Director")
    
    insertDirector(_conn, "Steven Spielberg", 1946, "Duel")
    insertDirector(_conn, "Roger Allers", 1949, "The Lion King")
    insertDirector(_conn, "Chris Columbus", 1958, "Sorcerer's Stone")
    insertDirector(_conn, "Rob Minkoff", 1962, "The Lion King")
    insertDirector(_conn, "Stanley Kubrick", 1928, "Fear and Desire")
    insertDirector(_conn, "Steven Lisberger", 1951, "Tron")
    insertDirector(_conn, "Herbert Ross", 1927, "Nijinsky")
    insertDirector(_conn, "Hector Babenco", 1946, "Ironweed")
    insertDirector(_conn, "Guy Green", 1913, "Diamond Head")
    insertDirector(_conn, "Budd Boetticher", 1916, "Horizons West")
    insertDirector(_conn, "Jerzy Skilowski", 1933, "Moonlighting")
    insertDirector(_conn, "Lindsay Anderson", 1923, "If")
    insertDirector(_conn, "Matthew Robbins", 1945, "Batteries Not Included")

    
    print("++++++++++++++++++++++++++++++++++")

def deleteDirectorWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Director")
    try:
        sql="delete from director where d_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
  
def deleteDirectorWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Director")
    try:
        sql="delete from director where d_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
  
def deleteDirectorWFirstFilm(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Director")
    try:
        sql="delete from director where d_FirstFilm =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
  
def updateDirectorName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Director")
    try: 
        sql="update director set d_Name as ? where d_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateDirectorYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Director")
    try: 
        sql="update director set d_Year as ? where d_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateDirectorFirstFilm(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Director")
    try: 
        sql="update director set d_FirstFilm as ? where d_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
  
def insertActor(_conn, _name, _year, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Actor")
    try: 
        sql = "INSERT INTO actor VALUES(?, ?, ?)"
        args = [_name, _year, _firstFilm]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def populateActor(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Actor")
    
    insertActor(_conn, "Nathan Lane", 1956, "Ironweed")
    insertActor(_conn, "Jeremy Irons", 1948, "Nijinsky")
    insertActor(_conn, "James Earl Jones", 1931, "Dr Strangelove")
    insertActor(_conn, "Daniel Radcliffe", 1989, "Sorcerer's Stone")
    insertActor(_conn, "Emma Watson", 1990, "Sorcerer's Stone")
    insertActor(_conn, "Matthew Broderick", 1962, "Max Dugan Returns")
    insertActor(_conn, "Alan Rickman", 1946, "Sorcerer's Stone")
    insertActor(_conn, "Ralph Fiennes", 1962, "Schindler's List")
    insertActor(_conn, "Liam Neeson", 1952, "Schindler's List")
    insertActor(_conn, "Dennis Weaver", 1924, "Horizons West")
    insertActor(_conn, "Malcolm McDowell", 1943, "If")
    insertActor(_conn, "Jack Nicholson", 1937, "Ironweed")
    insertActor(_conn, "Dennis Weaver", 1924, "Horizons West")
    insertActor(_conn, "Jeff Bridges", 1943, "Tron")
    
    print("++++++++++++++++++++++++++++++++++")

def deleteActorWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Actor")
    try:
        sql="delete from actor where a_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteActorWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Actor")
    try:
        sql="delete from actor where a_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteActorWFirstFilm(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Actor")
    try:
        sql="delete from actor where a_FirstFilm =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
     
def updateActorName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Actor")
    try: 
        sql="update actor set a_Name as ? where a_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateActorYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Actor")
    try: 
        sql="update actor set a_Year as ? where a_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateActorFirstFilm(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Actor")
    try: 
        sql="update actor set a_FirstFilm as ? where a_Name?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
       
def insertComposer(_conn, _name, _year, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Composer")
    try: 
        sql = "INSERT INTO composer VALUES(?, ?, ?)"
        args = [_name, _year, _firstFilm]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def deleteComposerWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Composer")
    try:
        sql="delete from composer where c_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteComposerWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Composer")
    try:
        sql="delete from composer where c_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteComposerWFirstFilm(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Composer")
    try:
        sql="delete from composer where c_FirstFilm =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
     
def populateComposer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Composer")
    
    insertComposer(_conn, "Hans Zimmer", 1957, "The Lion King")
    insertComposer(_conn, "John Williams", 1932, "Diamond Head")
    insertComposer(_conn, "Billy Goldenberg", 1936, "Duel")
    insertComposer(_conn, "Wendy Carlos", 1939, "A Clockwork Orange")
    insertComposer(_conn, "Laurie Johnson", 1927, "Dr Strangelove")
    insertComposer(_conn, "David Shire", 1937, "Max Dugan Returns")
    insertComposer(_conn, "James Horner", 1953, "Batteries Not Included")
    insertComposer(_conn, "Uncredited", 0, "Horizons West")
    insertComposer(_conn, "Marc Wilkinson", 1929, "If")
    insertComposer(_conn, "Stanley Myers", 1930, "Moonlighting")
    insertComposer(_conn, "John Morris", 1926, "Ironweed")
    
    print("++++++++++++++++++++++++++++++++++")
       
def updateComposerName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Composer")
    try: 
        sql="update composer set c_Name as ? where c_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateComposerYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Composer")
    try: 
        sql="update composer set c_Year as ? where c_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateComposerFirstFilm(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Composer")
    try: 
        sql="update composer set c_FirstFilm as ? where c_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
          
def insertStudio(_conn, _name, _year, _currentPres, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Studio")
    try: 
        sql = "INSERT INTO studio VALUES(?, ?, ?, ?)"
        args = [_name, _year, _currentPres, _firstFilm]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
        
def populateStudio(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Studio")
    
    insertStudio(_conn, "Disney", 1923, "Bob Iger", "The Lion King")
    insertStudio(_conn, "Universal", 1912, "Peter Cramer", "Duel")
    insertStudio(_conn, "Warner Bros", 1923, "Terry Tenser", "A Clockwork Orange")
    insertStudio(_conn, "Miracle Films", 1950, "Tony Semel", "Moonlighting")
    insertStudio(_conn, "Paramount", 1912, "Brian Robbins", "If")
    insertStudio(_conn, "Tri-Star", 1982, "Nicole Brown", "Ironweed")
    insertStudio(_conn, "Columbia", 1918, "Sanford Pantich", "Diamond Head")
    insertStudio(_conn, "Independent", 0, "Not Applicable", "Fear and Desire")
    
    print("++++++++++++++++++++++++++++++++++")

def deleteStudioWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Studio")
    try:
        sql="delete from studio where s_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def deleteStudioWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Studio")
    try:
        sql="delete from studio where s_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteStudioWPresident(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Studio")
    try:
        sql="delete from studio where s_President =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteStudioWFirstFilm(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Studio")
    try:
        sql="delete from studio where s_FirstFilm =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateStudioName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Studio")
    try: 
        sql="update studio set s_Name as ? where s_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateStudioYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Studio")
    try: 
        sql="update studio set s_Year as ? where s_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateStudioFirstFilm(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Studio")
    try: 
        sql="update studio set s_ as ? where s_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateStudioPresident(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Studio")
    try: 
        sql="update studio set s_President as ? where s_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def insertPresident(_conn, _name, _year, _studio, _yearsRan):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert President")
    try: 
        sql = "INSERT INTO president VALUES(?, ?, ?, ?)"
        args = [_name, _year, _studio, _yearsRan]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populatePresident(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate President")
    
    
    
    insertPresident(_conn, "Bob Iger", 1951, "Disney", 12)
    insertPresident(_conn, "Peter Cramer", 1960, "Universal", 17)
    insertPresident(_conn, "Terry Semel", 1943, "Warner Bros", 5)
    insertPresident(_conn, "Tony Tenser", 1920, "Miracle Films", 20)
    insertPresident(_conn, "Brian Robbins", 1963, "Paramount", 3)
    insertPresident(_conn, "Nicole Brown", 1980, "Tristar", 3)
    insertPresident(_conn, "Sanford Pantich", 1967, "Columbia", 4)
    
    
    
    print("++++++++++++++++++++++++++++++++++")

def deletePresidentWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete President")
    try:
        sql="delete from president where pre_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deletePresidentWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete President")
    try:
        sql="delete from president where pre_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deletePresidentWStudio(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete President")
    try:
        sql="delete from president where pre_Studio =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deletePresidentWYearsR(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete President")
    try:
        sql="delete from president where pre_YearsRan =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updatePresidentName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update President")
    try: 
        sql="update president set pre_Name as ? where pre_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updatePresidentYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update President")
    try: 
        sql="update president set pre_Year as ? where pre_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updatePresidentYearsRan(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update President")
    try: 
        sql="update president set pre_YearsRan as ? where pre_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updatePresidentStudio(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update President")
    try: 
        sql="update president set pre_Studio as ? where pre_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def insertMovie(_conn, _name, _genre, _year, _revenue, _directorO, directorTw, 
    _producerO, producerTw, producerTr, _actorO, actorTw, actorTr,
    _composerO, _studioO, _review):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Movie")
    try: 
        sql = "INSERT INTO movie VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_name, _genre, _year, _revenue, _directorO, directorTw, _producerO, producerTw, producerTr, _actorO, 
                actorTw, actorTr, _composerO, 
                _studioO, _review]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        
    print("++++++++++++++++++++++++++++++++++")
    
def populateMovie(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Movie")
    
    insertMovie(_conn, "The Lion King", "Dramedy", 1994, 968400000, "Roger Allers", "Rob Minkoff", "Don Hahn", NULL, NULL, "Nathan Lane", "Matthew Broderick", "James Earl Jones", "Hans Zimmer", "Disney", 1)
    insertMovie(_conn, "If", "Drama", 1968, 2300000, "Lindsay Anderson", NULL, "Lindsay Anderson", "Michael Medwin", NULL, "Malcolm McDowell", NULL, NULL, "Marc Wilkinson", "Paramount", 2)
    insertMovie(_conn, "Schindler's List", "Drama", 1993, 322200000, "Steven Spielberg", NULL, "Steven Spielberg", "Gerald Molen", "Branko Lustig", "Liam Neeson", "Ralph Fiennes", NULL, "John Williams", "Universal", 3)
    insertMovie(_conn, "Horizons West", "Western", 1952, 500000, "Budd Boetticher", NULL, "Albert Cohen", NULL, NULL, "Dennis Weaver", NULL, NULL, "Uncredited", "Universal", 4)
    insertMovie(_conn, "Sorcerer's Stone", "Fantasy", 2001, 1024000000, "Chris Columbus", NULL, "David Heyman", NULL, NULL,"Daniel Radcliffe", "Emma Watson", "Alan Rickman", "John Williams", "Warner Bros", 5)
    insertMovie(_conn, "Tron", "Science Fiction", 1982, 50000000, "Steven Lisberger", NULL, "Donald Kushner", NULL, NULL, "Jeff Bridges", NULL, NULL, "Wendy Carlos", "Disney", 6)
    insertMovie(_conn, "Batteries Not Included", "Horror", 1987, 65100000, "Matthew Robbins", NULL, "Ronald Schwary", NULL, NULL, "Hume Croyn", NULL, NULL, "James Horner", "Universal", 7)
    insertMovie(_conn, "Duel", "Thriller", 1971, 450000, "Steven Speilberg", NULL, "Richard Matheson", NULL, NULL, "Dennis Weaver", NULL, NULL, "Billy Goldenberg", "Universal", 8)
    insertMovie(_conn, "Fear and Desire", "War", 1952, 53000, "Stanley Kubrick", NULL, "Stanley Krubrick", NULL, NULL, "Frank Silvera", NULL, NULL, "Gerald Fried", "Independent", 9)
    insertMovie(_conn, "Dr Strangelove", "Satire", 1964, 9200000, "Stanley Kubrick", NULL, "Stanley Kubrick", NULL, NULL, "James Earl Jones", NULL, NULL, "Laurie Johnson", "Columbia", 10)
    insertMovie(_conn, "Max Dugan Returns", "Drama", 1983, 17613720, "Herbert Ross", NULL, "Herbert Ross", "Neil Simon", NULL, "Matthew Broderick", NULL, NULL, "David Shire", "Miracle Films", 11)
    insertMovie(_conn, "Ironweed", "Drama", 1987, 7300000, "Hector Babenco", NULL, "Keith Barish", "William Kennedy", NULL, "Jack Nicholson", "Nathan Lane", NULL, "John Morris", "Tri-Star", 12)
    insertMovie(_conn, "Nijinsky", "Biographical", 1980, 1047454, "Herbert Ross", NULL, "Hugh Wheeler", "Romola Nijinsky", "Vaslav Nijinsky", "Jeremy Irons", NULL, NULL, "Uncredited", "Paramount", 13)
    insertMovie(_conn, "Moonlighting", "Drama", 1982, 2000000, "Jerzy Skilowski", NULL, "Mark Shivas", "Jerzy Skolimowski", "Michael White", "Jeremy Irons", NULL, NULL, "Stanley Myers", "Miracle Films", 14)
    insertMovie(_conn, "Diamond Head", "Romance", 1962, 4500000, "Guy Green", NULL, "Jerry Bresler", NULL, NULL, "Charlton Heston", NULL, NULL, "John Williams", "Columbia", 15)
    insertMovie(_conn, "A Clockwork Orange", "Crime", 1971, 1440000000, "Stanley Kurbrick", NULL, "Bill Butler", NULL, NULL, "Malcolm McDowell", NULL, NULL, "Wendy Carlos", "Warner Bros", 16)
    
    print("++++++++++++++++++++++++++++++++++")

def deleteMovieWTitle(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Title =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWGenre(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_genre =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWRevenue(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Revenue =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Don't sweat it. :)")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWDirector(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Director =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWDirectorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_DirectorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWProducer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Producer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWProducerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_ProducerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWProducerThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_ProducerThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWActor(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Actor =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWActorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_ActorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWActorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_ActorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        print("Might be in another related slot")
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWComposer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Composer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWStudio(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Studio =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteMovieWReview(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Movie")
    try:
        sql="delete from movie where m_Review =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateMovieTitle(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Title as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieGenre(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_genre as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieYear(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Year as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateMovieRevenue(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Revenue as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieDirector(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Director as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieDirectorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_DirectorTwo as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieActor(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Actor as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieActorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_ActorTwo as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieActorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_ActorThree as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateMovieProducer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Producer as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieProducerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_ProducerTwo as ? where m_Title=?"
        args=[_up1, _up2]

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieProducerThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_ProducerThree as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieComposer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Composer as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateMovieStudio(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Studio as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateMovieReview(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Movie")
    try: 
        sql="update movie set m_Review as ? where m_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def insertEarliestHere(_conn, _movie, _directorO, directorTw, _producerO, producerTw, producerTr, 
    _actorO, actorTw, actorTr, _composerO, _studio):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert earliestHere")
    try: 
        sql = "INSERT INTO earliestHere VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_movie, _directorO, directorTw, _producerO, producerTw, producerTr, 
    _actorO, actorTw, actorTr, _composerO, _studio]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
        
def populateEarliestHere(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Movie")
    
    insertEarliestHere(_conn, "The Lion King", "Roger Allers", "Rob Minkoff", NULL, NULL, NULL, NULL, NULL, NULL, "Hans Zimmer", "Disney")
    insertEarliestHere(_conn, "If", "Lindsay Anderson", NULL, "Michael Medwin", "Lindsay Anderson", NULL, "Marc Wilkinson", NULL, NULL, NULL, "Paramount")
    insertEarliestHere(_conn, "Schindler's List", NULL, NULL, "Steven Spielberg", NULL, NULL, "Malcolm McDowell", NULL, NULL, NULL, NULL)
    insertEarliestHere(_conn, "Horizons West", "Budd Boetticher", NULL, NULL, NULL, NULL, "Dennis Weaver", NULL, NULL, "Uncredited", NULL)
    insertEarliestHere(_conn, "Sorcerer's Stone", "Chris Columbus", NULL, "David Hayman", NULL, NULL, "Daniel Radcliffe", "Emma Watson", "Alan Rickman", NULL, NULL)
    insertEarliestHere(_conn, "Tron", "Steven Lisberger", NULL, "Donald Kushner", NULL, NULL, NULL, NULL, NULL, NULL, "Disney")
    insertEarliestHere(_conn, "Batteries Not Included", "Matthew Robbins", NULL, "Gerald Molen", "Ronald Schwary", NULL, NULL, NULL, NULL, "James Horner", NULL)
    insertEarliestHere(_conn, "Duel", "Steven Spielberg", NULL, "Richard Matheson", NULL, NULL, NULL, NULL, NULL, NULL, NULL)
    insertEarliestHere(_conn, "Fear and Desire", "Stanley Kubrick", NULL, "Stanley Kubrick", NULL, NULL, NULL, NULL, NULL, NULL, NULL)
    insertEarliestHere(_conn, "Dr Strangelove", NULL, NULL, NULL, NULL, NULL, "James Earl Jones", NULL, NULL, NULL, "Independent")
    insertEarliestHere(_conn, "Max Dugan Returns", NULL, NULL, "Neil Simon", "Herbert Ross", NULL, "Matthew Broderick", NULL, NULL, "Stanley Myers", NULL)
    insertEarliestHere(_conn, "Ironweed", "Herbert Ross", NULL, "Keith Barish", "Marcia Nasatir", NULL, "Nathan Lane", "Jack Nicolson", NULL, "John Morris", "Tri-Star")
    insertEarliestHere(_conn, "Nijinsky", "Hector Babenco", NULL, "Hugh Wheeler", "Romola Nijinsky", "Vaslav Nijinsky", "Jeremy Irons", NULL, NULL, NULL, NULL)
    insertEarliestHere(_conn, "Moonlighting", "Jerzy Skilowski", NULL, NULL, "Mark Shivas", "Jerzy Skolimowski", "Michael White", NULL, NULL, "Stanley Myers", "Miracle Films")
    insertEarliestHere(_conn, "Diamond Head", "Guy Green", NULL, NULL, NULL, NULL, NULL, NULL, NULL, "John Williams", "Columbia")
    insertEarliestHere(_conn, "A Clockwork Orange", NULL, NULL, "Bill Butler", NULL, NULL, NULL, NULL, NULL, "Wendy Carlos", "Warner Bros")
    
    print("++++++++++++++++++++++++++++++++++")

def deleteEarliestHereWTitle(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Title =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWDirector(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Director =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWDirectorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_DirectorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWProducer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Producer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWProducerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_ProducerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWProducerThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_ProducerThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWActor(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Actor =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWActorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_ActorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWActorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_ActorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWComposer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Composer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteEarliestHereWStudio(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete EarliestHere")
    try:
        sql="delete from earliestHere where e_Studio =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateEarliestHereTitle(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_Title as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereDirector(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_Director as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereDirectorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update EarliestHere")
    try: 
        sql="update earliestHere set e_DirectorTwo as ? where e_Title=?"
        args=[_up1, _up2]

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateEarliestHereProducer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_Producer as ? where e_Title=?"
        args=[_up1, _up2]

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereProducerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_ProducerTwo as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereProducerThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_ProducerThree as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateEarliestHereActor(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Earliest Here")
    try: 
        sql="update earliestHere set e_Actor as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereActorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update EarliestHere")
    try: 
        sql="update earliestHere set e_ActorTwo as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereActorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update EarliestHere")
    try: 
        sql="update earliestHere set e_ActorThree as ? where e_Title=?"
        args=[_up1, _up2]

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateEarliestHereComposer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update EarliestHere")
    try: 
        sql="update earliestHere set e_Composer as ? where e_Titler=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateEarliestHereStudio(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update EarliestHere")
    try: 
        sql="update earliestHere set e_Studio as ? where e_Title=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def insertWorkedWith(_conn, _name, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO, _composerTw):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert workedWith")
    try: 
        sql = "INSERT INTO workedWith VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_name, _directorO, directorTw, directorTr, directorFo, 
                directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, _actorO, 
                actorTw, actorTr, actorFo, actorFi, _composerO, _composerTw]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        
    print("++++++++++++++++++++++++++++++++++")
    
def populateWorkedWith(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate workedWith")
    
    insertWorkedWith(_conn, "Jeremy Irons", "Herbert Ross", "Jerzy Skilowski", NULL, NULL, NULL, "Vaslav Nijinsky", "Romola Nijinsky", "Mark Shivas", "Jerzy Skolimoski", "Michael White", NULL, NULL, NULL, NULL, NULL, "Stanley Myers", "Uncredited")
    insertWorkedWith(_conn, "Steven Spielberg", NULL, NULL, NULL, NULL, NULL, "Gerald Molen", "Branko Lustig", "Richard Matheson", NULL, NULL, "Dennis Weaver", "Liam Neeson", "Ralph Fiennes", NULL, NULL, "John Williams", "Billy Goldenberg")
    insertWorkedWith(_conn, "John Williams", "Roger Allers", "Rob Minkoff", "Guy Green", "Chris Columbus", "Steven Spielberg", "Steven Spielberg", "Gerald Molen", "Branko Lustig", "David Heyman", NULL, "Daniel Radcliffe", "Emma Watson", "Alan Rickman", "Liam Neeson", "Ralph Fiennes", NULL, NULL)
    insertWorkedWith(_conn, "Matthew Broderick", "Roger Allers", "Rob Minkoff", "Herbert Ross", NULL, NULL, "Don Hahn", "Herbert Ross", "Neil Simon", NULL, NULL, "Nathan Lane", "James Earl Jones", NULL, NULL, NULL, "Hans Zimmer", "David Shire")
    insertWorkedWith(_conn, "Stanley Kubrick", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "James Earl Jones", "Frank Silvera", NULL, NULL, NULL, "Laurie Johnson", "Gerald Fried")
    insertWorkedWith(_conn, "Nathan Lane",  "Roger Allers", "Rob Minkoff", "Hector Babenco", NULL, NULL, "Don Hahn", "Keith Barish", "William Kennedy", NULL, NULL, "Matthew Broderick", "James Earl Jones", "Jack Nicholson", NULL, NULL, "Hans Zimmer", "John Morris")
    insertWorkedWith(_conn, "Dennis Weaver", "Steven Spielberg", "Budd Boetticher", NULL, NULL, NULL, "Richard Matheson", "Albert Cohen", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "Billy Goldenberg", "Uncredited")
    
    print("++++++++++++++++++++++++++++++++++")

def deleteWorkedWithWName(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_Name =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWDirector(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_Director =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWDirectorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_DirectorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWDirectorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_DirectorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWDirectorFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_DirectorFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWDirectorFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_DirectorFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWProducer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_Producer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWProducerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ProducerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWProducerThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ProducerThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWProducerFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ProducerFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWProducerFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ProducerFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWActor(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_Actor =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWActorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ActorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWActorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ActorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWActorFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ActorFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWActorFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ActorFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWComposer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_Composer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteWorkedWithWComposerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete WorkedWith")
    try:
        sql="delete from workedWith where w_ComposerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
 
def updateWorkedWithName(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_Name as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithDirector(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_Director as ? where w_Name=?"
        args=[_up1, _up2]

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithDirectorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_DirectorTwo as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithDirectorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_DirectorThree as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithDirectorFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_DirectorFour as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithDirectorFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_DirectorFive as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithProducer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_Producer as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithProducerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ProducerTwo as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithProducerThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ProducerThree as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithProducerFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ProducerFour as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithProducerFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ProducerFive as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithActor(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_Actor as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithActorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ActorTwo as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithActorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ActorThree as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithActorFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ActorFour as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithActorFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ActorFive as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateWorkedWithComposer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_Composer as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateWorkedWithComposerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Worked With")
    try: 
        sql="update workedWith set w_ComposerTwo as ? where w_Name=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def insertYear(_conn, _year, _movie, _movietw, _movietr, _moviefo, _moviefi, 
               _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi, _president,
               _studio, _studioTw):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Year")
    try: 
        sql = "INSERT INTO year VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_year, _movie, _movietw, _movietr, _moviefo, _moviefi, _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi, _president, _studio, _studioTw]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
        
def populateYear(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Movie")
    
    
    insertYear(_conn, 1890, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Vaslav Nijinsky", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1891, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Romola Nijinsky", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1903, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Albert Cohoen", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1908, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Jerry Bresler", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1912, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Hugh Wheeler", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, "Universal", "Paramount")
    insertYear(_conn, 1913, NULL, NULL, NULL, NULL, NULL, 
               "Guy Green", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1916, NULL, NULL, NULL, NULL, NULL, 
               "Budd Boetticher", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1918, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, "Columbia", NULL)
    
    insertYear(_conn, 1918, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Tony Tenser", NULL, NULL)
    insertYear(_conn, 1921, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Bill Butler", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1923, NULL, NULL, NULL, NULL, NULL, 
               "Lindsay Anderson", NULL, NULL, NULL, NULL, 
               "Lindsay Anderson", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, "Disney", "Warner Bros")
    insertYear(_conn, 1924, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               "Dennis Weaver", NULL, NULL, NULL, NULL, 
               NULL,NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1926, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Richard Matheson", "Marcia Nasatir", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "John Morris", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1927, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Herbert Ross", "Neil Simon", NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "Laurie Johnson", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1928, NULL, NULL, NULL, NULL, NULL, 
               "Stanley Kubrick", NULL, NULL, NULL, NULL, 
               "Stanley Kubrick", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1929, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Marc Wilkinson", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1930, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Stanley Myers", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1931, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "James Earl Jones", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1932, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "John Williams", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1933, NULL, NULL, NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               "Jerzy Skilowski", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1935, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Gerald Molen", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1936, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Michael White", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Billy Goldenberg", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1937, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Skomlimoski Jerzy", NULL, NULL, NULL, NULL,
               "Jack Nicholson", NULL, NULL, NULL, NULL,
               "David Shire", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1938, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Mark Shivas", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1939, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Wendy Carlos", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1943, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "Malcom McDowell", "Jeff Bridges", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Terry Semel", NULL, NULL)
    insertYear(_conn, 1944, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Ronald Schwary", "Keith Barish", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, )
    insertYear(_conn, 1945, NULL, NULL, NULL, NULL, NULL, 
               "Matthew Robbins", NULL, NULL, NULL, NULL,
               "Donald Kushner", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1946, NULL, NULL, NULL, NULL, NULL, 
               "Steven Spielberg", "Hector Babenco", NULL, NULL, NULL, 
               "Steven Spielberg", NULL, NULL, NULL, NULL,
               "Alan Rickman", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1948, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "David Hayman", NULL, NULL, NULL, NULL, 
               "Jeremy Irons", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1949, NULL, NULL, NULL, NULL, NULL, 
               "Roger Allers", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1950, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, "Miracle Films", NULL)
    insertYear(_conn, 1951, NULL, NULL, NULL, NULL, NULL, 
               "Steven Lisberger", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Bob Iger", NULL, NULL)
    insertYear(_conn, 1952, "Horizon's West", "Fear and Desire", NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Liam Neeson", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL)
    insertYear(_conn, 1953, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "James Horner", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1956, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Nathan Lane", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1957, NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                "Hans Zimmer",  NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL)
    insertYear(_conn, 1958, NULL, NULL, NULL, NULL, NULL, 
               "Chris Columbus",  NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL)
    insertYear(_conn, 1960, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Peter Cramer", NULL, NULL)
    insertYear(_conn, 1962, "Diamond Head", NULL, NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Ralphe Fiennes", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1963, NULL, NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Brian Robbins", NULL, NULL)
    insertYear(_conn, 1964, "Dr Strangelove", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1968, "If", NULL, NULL, NULL, NULL,
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1971, "Duel", "A Clockwork Orange", NULL, NULL, NULL,  
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1980, "Nijinskhy", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Nicole Brown", NULL, NULL)
    insertYear(_conn, 1982, "Tron", "Moonlighting", NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, "Tri-Star", NULL)
    insertYear(_conn, 1987, "Batteries Not Included", "Ironweed", NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1993, "Schindler's List", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1994, "The Lion King", NULL, NULL, NULL, NULL,
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, "Dreamworks", NULL)
    insertYear(_conn, 1989, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Daniel Radcliffe", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 1989, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Emma Watson", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 2001, "Sorcerer's Stone", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL)
    insertYear(_conn, 0, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL,  NULL, NULL, NULL, 
               "Uncredited", NULL, NULL, NULL, NULL, 
               NULL, "Independent", NULL)
    
    print("++++++++++++++++++++++++++++++++++")

def deleteYear(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_year =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWMovie(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Movie =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWMovieTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_MovieTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWMovieThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_MovieThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWMovieFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_MovieFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWMovieFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_MovieFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWDirector(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Director =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWDirectorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_DirectorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWDirectorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_DirectorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWDirectorFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_DirectorFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWDirectorFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_DirectorFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWProducer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Producer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWProducerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ProducerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWProducerThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ProducerThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWProducerFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ProducerFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWProducerFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ProducerFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWActor(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Actor =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWActorTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ActorTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWActorThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ActorThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWActorFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ActorFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWActorFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ActorFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWComposer(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Composer =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWComposerTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ComposerTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWComposerThree(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ComposerThree =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWComposerFour(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ComposerFour =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWComposerFive(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_ComposerFive =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWPresident(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_President =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWStudio(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_Studio =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def deleteYearWStudioTwo(_conn, _del):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Year")
    try:
        sql="delete from year where y_StudioTwo =?"
        args=[_del]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearMovie(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Movie as ? where y_Movie=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearMovieTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_MovieTwo as ? where y_MovieTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearMovieThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_MovieThree as ? where y_MovieThree=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearMovieFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_MovieFour as ? where y_MovieFour=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearMovieFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update Year set y_MovieFive as ? where y_MovieFive=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearDirector(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Director as ? where y_Director=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearDirectorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_DirectorTwo as ? where y_DirectorTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearDirectorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_DirectorThree as ? where y_DirectorThree=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearDirectorFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_DirectorFour as ? where y_DirectorFour=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearDirectorFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update Year set y_DirectorFive as ? where y_DirectorFive=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearProducer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Produceras ? where y_Producer=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearProducerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ProducerTwo as ? where y_ProducerTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearProducerThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ProducerThree as ? where y_ProducerThree=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearProducerFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ProducerFour as ? where y_ProducerFour=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearProducerFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update Year set y_ProducerFive as ? where y_ProducerFive=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearActor(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Actor as ? where y_Actor=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearActorTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ActorTwo as ? where y_ActorTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearActorThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ActorThree as ? where y_ActorThree=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearActorFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ActorFour as ? where y_ActorFour=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearActorFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update Year set y_ActorFive as ? where y_ActorFive=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearComposer(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Composer as ? where y_Composer=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearComposerTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ComposerTwo as ? where y_ComposerTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearComposerThree(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ComposerThree as ? where y_ComposerThree=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearComposerFour(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_ComposerFour as ? where y_ComposerFour=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearComposerrFive(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update Year set y_ComposerFive as ? where y_ComposerFive=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearPresident(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_President as ? where y_President=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def updateYearStudio(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_Studio as ? where y_Studio=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    
def updateYearStudioTwo(_conn, _up1, _up2):
    print("++++++++++++++++++++++++++++++++++")
    print("Update Year")
    try: 
        sql="update year set y_StudioTwo as ? where y_StudioTwo=?"
        args=[_up1, _up2]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def trial1(_conn, _in):
    print("++++++++++++++++++++++++++++++++++")
    print("Genres with films with less than a million in revenue: ")

    try:
        sql = """select m_genre
                from movie
                where 
                m_revenue<?"""
        args=[_in]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} '.format("genre")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial2(_conn, _in):
    print("++++++++++++++++++++++++++++++++++")
    print("Presidents of _ reviews ")

    try:
        sql = """select pre_Name, r_author as president
                from president, review, movie
                where r_author=? and m_Review=r_reviewKey
                and m_Studio=pre_Studio"""
        args=[_in]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10} '.format("pre_Name","president")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} '.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Password on young presidents")

    try:
        sql = """select u_Password as password
                from user, president, movie, review
                where pre_Year>=1960 and pre_Studio=m_Studio and m_Review=r_reviewKey
                and r_author=u_Username"""
        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}'.format("password")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Revenue by genre ")

    try:
        sql = """select m_genre as Genre, sum(m_revenue) as revenue
                from movie
                group by Genre
                """


        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("Genre", "revenue")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Films of distinct genre: ")

    try:
        sql = """select distinct m1.m_Title as movie
                from movie m1, movie m2
                where 
                m1.m_Title<>m2.m_Title and m1.m_genre!=m2.m_genre"""

        args=[]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} '.format("movie")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial6(_conn, _in):
    print("++++++++++++++++++++++++++++++++++")
    print("President and film years ")

    try:
        sql = """select pre_Year as presBirth, m_Year
                from president, movie 
                where m_Revenue>? and pre_Studio=m_Studio"""

        args=[_in]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10} '.format("presBirth", "m_Year")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("years without producers as directors")

    try:
        sql = """select y_Year
                from year, movie
                except
                select y_Year
                from year, movie
                where y_Year=m_Year and m_Director=m_Producer"""

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("y_Year")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial8(_conn, _in):
    print("++++++++++++++++++++++++++++++++++")
    print("movies by collaborators ")

    try:
        sql = """select m_Title as movie
                from movie, workedWith
                where m_Director=w_Name and m_Director=? 
                """

        args=[_in]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} '.format("movie")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("President birth years of those who didn't work with producer/director combo: ")

    try:
        sql = """select pre_Year
                from president, movie
                where m_Studio=pre_Studio
                except
                select pre_Year
                from president, movie
                where m_Studio=pre_Studio and
                m_Director=m_Producer"""

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("pre_Year")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Obscure profit")

    try:
        sql = """select sum(m_Revenue) as profit
                from review, movie
                where r_reviewKey=m_Review and r_author="Michael Moua"
                """

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("profit")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Mainstream Profit")

    try:
        sql = """
                select sum(m_Revenue) as profit
                from review, movie
                where r_reviewKey=m_Review and r_author="Paul Kim"
                """

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("profit")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Distinct Film Genres")

    try:
        sql = """
                select distinct m1.m_genre
                from movie m1, movie m2
                where 
                m1.m_Title<>m2.m_Title and m1.m_genre!=m2.m_genre
                """

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}'.format("movie")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Establishing years of movies, studios, and presidents  ")

    try:
        sql = """select m_Title, m_Year, s_Year, pre_Year
                from movie, studio, president, earliestHere
                where m_Title=e_Title and m_Studio=s_Name and s_Name=pre_Studio
                """

        
        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>20} {:>10} {:>10} {:>10}'.format("m_Title","m_Year", "s_Year", "pre_Year")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>20} {:>10} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Recent Career Genre ")

    try:
        sql = """select distinct m_genre as genre
                from movie, earliestHere
                where m_Title=e_Title
                """

        
        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("genre")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Presidents of collaborators ")

    try:
        sql = """select distinct pre_Name
                from movie, workedWith, president
                where w_Name=m_Director 
                union
                select distinct pre_Name
                from movie, workedWith, president
                where w_Name=m_Actor
                union
                select distinct pre_Name
                from movie, workedWith, president
                where w_Name=m_Composer
                union
                select distinct pre_Name
                from movie, workedWith, president
                where w_Name=m_Producer and m_Producer!=m_Director
                """

        

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("pre_Name")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Sorted Films ")

    try:
        sql = """select m_Title
                from movie
                group by m_Year"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("model")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Presidents of Obscure Films ")

    try:
        sql = """select distinct pre_Name as president 
                from review, movie, president
                where r_author="Michael Moua" and r_reviewKey=m_Review
                and m_Studio=pre_Studio
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("president")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Producer's earliest films in database")

    try:
        sql = """
            select p_Name as Producer, p_FirstFilm as earliest
            from studio, movie, year, producer
            where s_Name=m_Studio and (s_Name=y_Studio or s_Name=y_StudioTwo) and 
            y_Producer=p_Name
        """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("Producer", "earliest")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Earliest Titles ")

    try:
        sql = """select distinct(e_Title)
                from workedWith, earliestHere, director
                where w_Name=d_Name
                union
                select distinct(e_Title)
                from workedWith, earliestHere, actor
                where w_Name=a_Name 
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} '.format("e_Title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial20(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Shared Genres")

    try:
        sql = """select distinct m1.m_genre as genre
                from movie m1, movie m2
                where 
                m1.m_Title<>m2.m_Title and m1.m_genre=m2.m_genre
                group by genre
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}'.format("genre")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial21(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Users")

    try:
        sql = """select u_Username
                from user
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}'.format("username")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} '.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial22(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Reviews")

    try:
        sql = """select *
                from review
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10} {:>10}'.format("reviewkey, author, title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} {:>10} '.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial23(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Directors")

    try:
        sql = """select *
                from director
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10} {:>20}'.format("name, birth, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} {:>20} '.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial24(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Producer")

    try:
        sql = """select *
                from producer
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10} {:>20}'.format("name, birth, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} {:>20} '.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial24(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Actor")

    try:
        sql = """select *
                from actor
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10} {:>20}'.format("name, birth, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} {:>20} '.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial23(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Composer")

    try:
        sql = """select *
                from composer
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10} {:>20}'.format("name, birth, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10} {:>20} '.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial24(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Studio")

    try:
        sql = """select *
                from studio
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>20} {:>10} {:>20}'.format("name, establishment, president, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20}{:>10} {:>20} '.format(row[0], row[1], row[2], row[3])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial25(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Presidents")

    try:
        sql = """select *
                from president
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10}{:>10} {:>20}'.format("name, birth, studio, Earliest title")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10}{:>10} {:>20} '.format(row[0], row[1], row[2], row[3])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)
def trial25(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Movies")

    try:
        sql = """select *
                from movie
                """

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format("title, genre, year, revenue, director, director2, producer, producer1, producer2, producer3, actor, actor1, actor2, actor3, composer, studio, review")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}{:>10}{:>10}{:>10}{:>10} {:>10}{:>10}{:>10}{:>10}{:>10} {:>10}{:>10}{:>10}{:>10}{:>10} '.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    trialing(_conn)







        
def populateTables(_conn):
    populateUser(_conn)
    populateReview(_conn)
    populateProducer(_conn)
    populateDirector(_conn)
    populateActor(_conn)
    populateComposer(_conn)
    populateStudio(_conn)
    populatePresident(_conn)
    populateMovie(_conn)
    populateEarliestHere(_conn)
    populateWorkedWith(_conn)
    populateYear(_conn)
   
def deleteTuple(_conn):
    deletion=input("Enter command code (1-12) to delete data: ")
    if deletion=="1":
        pathway=input("Enter command code (1-2)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteUserWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter valid password: ")
            deleteUserWPassword(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    elif deletion=="2":
        pathway=input("Enter command code (1-3)")
        if pathway=="1":
            deletion_i=int(input("Enter valid number: "))
            deleteReviewWKey(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter name: ")
            deleteReviewWAuthor(_conn, deletion)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter movie title: ")
            deleteReviewWMovieTitle(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    elif deletion=="3":
        pathway=input("Enter command code (1-3)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteDirectorWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion=int(input("Enter valid year: "))
            deleteDirectorWYear(_conn, deletion)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid title: ")
            deleteDirectorWFirstFilm(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="4":
        pathway=input("Enter command code (1-3)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteProducerWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion_i=int(input("Enter valid year: "))
            deleteProducerWYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid title: ")
            deleteProducerWFirstFilm(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="5":
        pathway=input("Enter command code (1-3)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteActorWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion_i=int(input("Enter valid year: "))
            deleteActorWYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid title: ")
            deleteActorWFirstFilm(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="6":
        pathway=input("Enter command code (1-3)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteComposerWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion_i=int(input("Enter valid year: "))
            deleteComposerWYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid title: ")
            deleteComposerWFirstFilm(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="7":
        pathway=input("Enter command code (1-4)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteStudioWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion_i=int(input("Enter valid year: "))
            deleteStudioWYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid president: ")
            deleteStudioWPresident(_conn, deletion)
            trialing(_conn)
        elif pathway=="4":
            deletion=input("Enter valid title: ")
            deleteStudioWFirstFilm(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    elif deletion=="8":
        pathway=input("Enter command code (1-4)")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deletePresidentWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion_i=int(input("Enter valid year: "))
            deletePresidentWYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid studio: ")
            deletePresidentWStudio(_conn, deletion)
            trialing(_conn)
        elif pathway=="4":
            deletion_i=int(input("Enter valid number: "))
            deletePresidentWYearsR(_conn, deletion_i)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="9":
        pathway=input("Enter command code (1-15): ")
        if pathway=="1":
            deletion=input("Enter valid title: ")
            deleteMovieWTitle(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter valid genre: ")
            deleteMovieWGenre(_conn, deletion)
            trialing(_conn)
        elif pathway=="3":
            deletion_i=int(input("Enter valid year: "))
            deleteMovieWYear(_conn, deletion)
            trialing(_conn)
        elif pathway=="4":
            deletion_i=int(input("Enter valid revenue: "))
            deleteMovieWRevenue(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="5":
            deletion=input("Enter valid director: ")
            deleteMovieWDirector(_conn, deletion)
            trialing(_conn)
        elif pathway=="6":
            deletion=input("Enter valid director: ")
            deleteMovieWDirectorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="7":
            deletion=input("Enter valid producer: ")
            deleteMovieWProducer(_conn, deletion)
            trialing(_conn)
        elif pathway=="8":
            deletion=input("Enter valid producer: ")
            deleteMovieWProducerTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="9":
            deletion=input("Enter valid producer: ")
            deleteMovieWProducerThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="10":
            deletion=input("Enter valid actor: ")
            deleteMovieWActor(_conn, deletion)
            trialing(_conn)
        elif pathway=="11":
            deletion=input("Enter valid actor: ")
            deleteMovieWActorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="12":
            deletion=input("Enter valid actor: ")
            deleteMovieWActorThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="13":
            deletion=input("Enter valid composer: ")
            deleteMovieWComposer(_conn, deletion)
            trialing(_conn)
        elif pathway=="14":
            deletion=input("Enter valid studio: ")
            deleteMovieWStudio(_conn, deletion)
            trialing(_conn)
        elif pathway=="15":
            deletion=int(input("Enter valid review key: "))
            deleteMovieWReview(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    elif deletion=="10":
        pathway=input("Enter command code (1-11): ")
        if pathway=="1":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWTitle(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWDirector(_conn, deletion)
            trialing(_conn)
        if pathway=="3":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWDirectorTwo(_conn, deletion)
            trialing(_conn)
        if pathway=="4":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWProducer(_conn, deletion)
            trialing(_conn)
        if pathway=="5":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWProducerTwo(_conn, deletion)
            trialing(_conn)
        if pathway=="6":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWProducerThree(_conn, deletion)
            trialing(_conn)
        if pathway=="7":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWActor(_conn, deletion)
            trialing(_conn)
        if pathway=="8":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWActorTwo(_conn, deletion)
            trialing(_conn)
        if pathway=="9":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWActorThree(_conn, deletion)
            trialing(_conn)
        if pathway=="10":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWComposer(_conn, deletion)
            trialing(_conn)
        if pathway=="11":
            deletion=input("Enter valid title: ")
            deleteEarliestHereWStudio(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    elif deletion=="11":
        pathway=input("Enter command code (1-18): ")
        if pathway=="1":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWName(_conn, deletion)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWDirector(_conn, deletion)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWDirectorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="4":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWDirectorThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="5":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWDirectorFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="6":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWDirectorFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="7":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWProducer(_conn, deletion)
            trialing(_conn)
        elif pathway=="8":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWProducerTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="9":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWProducerThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="10":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWProducerFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="11":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWProducerFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="12":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWActor(_conn, deletion)
            trialing(_conn)
        elif pathway=="13":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWActorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="14":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWActorThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="15":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWActorFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="16":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWActorFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="17":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWComposer(_conn, deletion)
            trialing(_conn)
        elif pathway=="18":
            deletion=input("Enter valid name: ")
            deleteWorkedWithWComposerTwo(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
    elif deletion=="12":
        pathway=input("Enter command code (1-29): ")
        if pathway=="1":
            deletion_i=int(input("Enter valid number: "))
            deleteYear(_conn, deletion_i)
            trialing(_conn)
        elif pathway=="2":
            deletion=input("Enter valid title: ")
            deleteYearWMovie(_conn, deletion)
            trialing(_conn)
        elif pathway=="3":
            deletion=input("Enter valid title: ")
            deleteYearWMovieTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="4":
            deletion=input("Enter valid title: ")
            deleteYearWMovieThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="5":
            deletion=input("Enter valid title: ")
            deleteYearWMovieFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="6":
            deletion=input("Enter valid title: ")
            deleteYearWMovieFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="7":
            deletion=input("Enter valid director: ")
            deleteYearWDirector(_conn, deletion)
            trialing(_conn)
        elif pathway=="8":
            deletion=input("Enter valid director: ")
            deleteYearWDirectorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="9":
            deletion=input("Enter valid director: ")
            deleteYearWDirectorThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="10":
            deletion=input("Enter valid director: ")
            deleteYearWDirectorFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="11":
            deletion=input("Enter valid director: ")
            deleteYearWDirectorFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="12":
            deletion=input("Enter valid producer: ")
            deleteYearWProducer(_conn, deletion)
            trialing(_conn)
        elif pathway=="13":
            deletion=input("Enter valid producer: ")
            deleteYearWProducerTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="14":
            deletion=input("Enter valid producer: ")
            deleteYearWProducerThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="15":
            deletion=input("Enter valid producer: ")
            deleteYearWProducerFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="16":
            deletion=input("Enter valid producer: ")
            deleteYearWProducerFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="17":
            deletion=input("Enter valid actor: ")
            deleteYearWActor(_conn, deletion)
            trialing(_conn)
        elif pathway=="18":
            deletion=input("Enter valid actor: ")
            deleteYearWActorTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="19":
            deletion=input("Enter valid actor: ")
            deleteYearWActorThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="20":
            deletion=input("Enter valid actor: ")
            deleteYearWActorFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="21":
            deletion=input("Enter valid actor: ")
            deleteYearWActorFive(_conn, deletion)
            trialing(_conn)
        elif pathway=="22":
            deletion=input("Enter valid number: ")
            deleteYearWComposer(_conn, deletion)
            trialing(_conn)
        elif pathway=="23":
            deletion=input("Enter valid number: ")
            deleteYearWComposerTwo(_conn, deletion)
            trialing(_conn)
        elif pathway=="24":
            deletion=input("Enter valid number: ")
            deleteYearWComposerThree(_conn, deletion)
            trialing(_conn)
        elif pathway=="25":
            deletion=input("Enter valid number: ")
            deleteYearWComposerFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="26":
            deletion=input("Enter valid number: ")
            deleteYearWComposerFour(_conn, deletion)
            trialing(_conn)
        elif pathway=="27":
            deletion=input("Enter valid number: ")
            deleteYearWPresident(_conn, deletion)
            trialing(_conn)
        elif pathway=="28":
            deletion=input("Enter valid number: ")
            deleteYearWStudio(_conn, deletion)
            trialing(_conn)
        elif pathway=="29":
            deletion=input("Enter valid number: ")
            deleteYearWStudioTwo(_conn, deletion)
            trialing(_conn)
        else:
            print("ERROR: Invalid Command")
            trialing(_conn)
    else:
        print("ERROR: Invalid command")    
        trialing(_conn)
        
def insertTuple(_conn):
    inserting=input("Enter command code (1-12) to add data: ")
    if inserting=="1":
        username=input("Insert username: ")
        password=input("Insert password: ")
        insertUser(_conn, username, password)
        trialing(_conn)
    elif inserting=="2":
        reviewKey=input("Insert review key:")
        author=input("Insert author: ")
        movieTitle=input("Insert movie: ")
        insertReview(_conn, reviewKey, author, movieTitle)
        trialing(_conn)
    elif inserting=="3":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        firstFilm=input("Insert earliest film here: ")
        insertDirector(_conn, name, year, firstFilm)
        trialing(_conn)
    elif inserting=="4":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        firstFilm=input("Insert earliest film here: ")
        insertProducer(_conn, name, year, firstFilm)
        trialing(_conn)
    elif inserting=="5":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        firstFilm=input("Insert earliest film here: ")
        insertActor(_conn, name, year, firstFilm)
        trialing(_conn)
    elif inserting=="6":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        firstFilm=input("Insert earliest film here: ")
        insertComposer(_conn, name, year, firstFilm)
        trialing(_conn)
    elif inserting=="7":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        president=input("Insert president: ")
        firstFilm=input("Insert earliest film here: ")
        insertStudio(_conn, name, year, president, firstFilm)
        trialing(_conn)
    elif inserting=="8":
        name=input("Insert name: ")
        year=int(input("Insert year: "))
        studio=input("Insert studio: ")
        yearsRan=input("Insert length of run: ")
        insertPresident(_conn, name, year, studio, yearsRan)
        trialing(_conn)
    elif inserting=="9":
        name=input("Insert name: ")
        genre=input("Insert genre: ")
        year=int(input("Insert year: "))
        revenue=int(input("Insert revenue: "))
        directorO=input("Insert director: ")
        directorTw=input("Insert second director (press space+enter if otherwise): ")
        producerO=input("Insert first producer: ")
        producerTw=input("Insert second producer (press space+enter if otherwise): ")
        producerTr=input("Insert third producer (press space+enter if otherwise): ")
        actorO=input("Insert first actor: ")
        actorTw=input("Insert second actor: ")
        actorTr=input("Insert third actor (press space+enter if otherwise): ")
        composer=input("Insert composer: ")
        studio=input("Insert studio: ")
        review=input("Insert review key: ")
        insertMovie(_conn, name, genre, year, revenue, directorO, directorTw, producerO,
                    producerTw, producerTr, actorO, actorTw, actorTr, composer, studio,
                    review)
        trialing(_conn)
    elif inserting=="10":
        name=input("insert name")
        directorO=input("Insert director: ")
        directorTw=input("Insert second director (press space+enter if otherwise): ")
        producerO=input("Insert first producer: ")
        producerTw=input("Insert second producer (press space+enter if otherwise): ")
        producerTr=input("Insert third producer (press space+enter if otherwise): ")
        actorO=input("Insert first actor: ")
        actorTw=input("Insert second actor: ")
        actorTr=input("Insert third actor (press space+enter if otherwise): ")
        composer=input("Insert composer: ")
        studio=input("Insert studio: ")
        insertEarliestHere(_conn, name, directorO, directorTw, producerO,
                    producerTw, producerTr, actorO, actorTw, actorTr, composer)
        trialing(_conn)
    elif inserting=="11":
        name=input("insert name")
        print("Press space+enter if needed\n")
        directorO=input("Insert director: ")
        directorTw=input("Insert director: ")
        directorTr=input("Insert director: ")
        directorFo=input("Insert director: ")
        directorFi=input("Insert director: ")
        producerO=input("Insert producer: ")
        producerTw=input("Insert producer: ")
        producerTr=input("Insert producer: ")
        producerFo=input("Insert producer: ")
        producerFi=input("Insert producer: ")
        actorO=input("Insert movie:")
        actorTw=input("Insert movie:")
        actorTr=input("Insert movie:")
        actorFo=input("Insert movie:")
        actorFi=input("Insert movie:")
        composerO=input("Insert composer: ")
        composerTw=input("Insert composer: ")
        insertWorkedWith(_conn, name, directorO, 
                   directorTw, directorTr, directorFo, directorFi, producerO, producerTw, 
                   producerTr, producerFo, producerFi, actorO, actorTw, actorTr, 
                   actorFo, actorFi, composerO, composerTw)
        trialing(_conn)
    elif inserting=="12":
        year=int(input("Insert year: "))
        print("Press space+enter if needed\n")
        movieO=input("Insert movie:")
        movieTw=input("Insert movie:")
        movieTr=input("Insert movie:")
        movieFo=input("Insert movie:")
        movieFi=input("Insert movie:")
        directorO=input("Insert director: ")
        directorTw=input("Insert director: ")
        directorTr=input("Insert director: ")
        directorFo=input("Insert director: ")
        directorFi=input("Insert director: ")
        producerO=input("Insert producer: ")
        producerTw=input("Insert producer: ")
        producerTr=input("Insert producer: ")
        producerFo=input("Insert producer: ")
        producerFi=input("Insert producer: ")
        actorO=input("Insert movie:")
        actorTw=input("Insert movie:")
        actorTr=input("Insert movie:")
        actorFo=input("Insert movie:")
        actorFi=input("Insert movie:")
        composerO=input("Insert composer: ")
        composerTw=input("Insert composer: ")
        composerTr=input("Insert composer: ")
        composerFo=input("Insert composer: ")
        composerFi=input("Insert composer: ")
        president=input("Insert president: ")
        studio=input("Insert studio: ")
        studioTw=input("Insert studio")
        insertYear(_conn, year, movieO, movieTw, movieTr, movieFo, movieFi, directorO, 
                   directorTw, directorTr, directorFo, directorFi, producerO, producerTw, 
                   producerTr, producerFo, producerFi, actorO, actorTw, actorTr, 
                   actorFo, actorFi, composerO, composerTw, composerTr, composerFo, 
                   composerFi, president, studio, studioTw)
        trialing(_conn)
        
def updateTuple(_conn):
    updating=input("Enter command code (1-12) to edit data: ")
    if updating=="1":
        name=input("Enter username: ")
        updating=input("Enter command code (1-2): ")
        if updating=="1":
            up=input("Enter new username: ")
            updateUserName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new password: ")
            updateUserPassword(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="2":
        name=input("Enter review key: ")
        updating=input("Enter command code (1-2): ")
        if updating=="1":
            up=input("Enter new author: ")
            updateReviewAuthor(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new movie title: ")
            updateReviewMovie(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="3":
        name=input("Enter director name: ")
        updating=input("Enter command code (1-3): ")
        if updating=="1":
            up_i=int(input("Enter new birth year: "))
            updateDirectorName(_conn, up_i, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new birth year: ")
            updateDirectorYear(_conn,  up, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new earliest movie title: ")
            updateDirectorFirstFilm(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="4":
        name=input("Enter producer name: ")
        updating=input("Enter command code (1-3): ")
        if updating=="1":
            up=input("Enter new name: ")
            updateProducerName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up_i=int(input("Enter new birth year: "))
            updateProducerYear(_conn, up_i, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new earliest movie title: ")
            updateProducerFirstFilm(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="5":
        name=input("Enter actor name: ")
        updating=input("Enter command code (1-3): ")
        if updating=="1":
            up=input("Enter new name: ")
            updateActorName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up_i=int(input("Enter new birth year: "))
            updateActorYear(_conn, up, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new earliest movie title: ")
            updateActorFirstFilm(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="6":
        name=input("Enter composer name: ")
        updating=input("Enter command code (1-3): ")
        if updating=="1":
            up=input("Enter new name:")
            updateComposerName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up_i=int(input("Enter new birth year: "))
            updateComposerYear(_conn, up_i, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new earliest movie title: ")
            updateComposerFirstFilm(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="7":
        name=input("Enter studio name: ")
        updating=input("Enter command code (1-4): ")
        if updating=="1":
            up=input("Enter new name: ")
            updateStudioName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up_i=int(input("Enter new founding year: "))
            updateStudioName(_conn, up_i, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new president: ")
            updateStudioPresident(_conn, up, name)
            trialing(_conn)
        elif updating=="4":
            up=input("Enter new earliest film: ")
            updateStudioFirstFilm(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="8":
        name=input("Enter president name: ")
        updating=input("Enter command code (1-4): ")
        if updating=="1":
            up=input("Enter new name: ")
            updatePresidentName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up_i=int(input("Enter new birth year: "))
            updatePresidentYear(_conn, up_i, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new studio: ")
            updatePresidentStudio(_conn, up, name)
            trialing(_conn)
        elif updating=="4":
            up_i=int(input("Enter new run length: "))
            updatePresidentYearsRan(_conn, up_i, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="9":
        name=input("Enter movie name: ")
        updating=input("Enter command code (1-15): ")
        if updating=="1":
            up=input("Enter new title: ")
            updateMovieTitle(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new genre: ")
            updateMovieGenre(_conn, up, name)
            trialing(_conn)
        elif updating=="3":
            up_i=int(input("Enter new release year: "))
            updateMovieYear(_conn, up, name)
            trialing(_conn)
        elif updating=="4":
            up_i=int(input("Enter new revenue: "))
            updateMovieRevenue(_conn, up, name)
            trialing(_conn)
        elif updating=="5":
            up=input("Enter new director: ")
            updateMovieDirector(_conn, up, name)
            trialing(_conn)
        elif updating=="6":
            up=input("Enter new director (space+enter if needed): ")
            updateMovieDirectorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="7":
            up=input("Enter new actor: ")
            updateMovieActor(_conn, up, name)
            trialing(_conn)
        elif updating=="8":
            up=input("Enter new actor (space+enter if needed): ")
            updateMovieActorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="9":
            up=input("Enter new actor (space+enter if needed): ")
            updateMovieActorThree(_conn, up, name)
            trialing(_conn)
        elif updating=="10":
            up=input("Enter new producer: ")
            updateMovieProducer(_conn, up, name)
            trialing(_conn)
        elif updating=="11":
            up=input("Enter new producer (space+enter if needed): ")
            updateMovieProducerTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="12":
            up=input("Enter new producer (space+enter if needed): ")
            updateMovieProducerThree(_conn, up, name)
            trialing(_conn)
        elif updating=="13":
            up=input("Enter new composer: ")
            updateMovieComposer(_conn, up, name)
            trialing(_conn)
        elif updating=="14":
            up=input("Enter new studio: ")
            updateMovieStudio(_conn, up, name)
            trialing(_conn)
        elif updating=="15":
            up=input("Enter new review key: ")
            updateMovieReview(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="10":
        name=input("Enter earliest film record name: ")
        updating=input("Enter command code (1-11): ")
        if updating=="1":
            up=input("Enter new title: ")
            updateEarliestHereTitle(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new director: ")
            updateEarliestHereDirector(_conn, up, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new director: ")
            updateEarliestHereDirectorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="4":
            up=input("Enter new producer: ")
            updateEarliestHereProducer(_conn, up, name)
            trialing(_conn)
        elif updating=="5":
            up=input("Enter new producer: ")
            updateEarliestHereProducerTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="6":
            up=input("Enter new producer: ")
            updateEarliestHereProducerThree(_conn, up, name)
            trialing(_conn)
        elif updating=="7":
            up=input("Enter new actor: ")
            updateEarliestHereActor(_conn, up, name)
            trialing(_conn)
        elif updating=="8":
            up=input("Enter new actor: ")
            updateEarliestHereActorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="9":
            up=input("Enter new actor: ")
            updateEarliestHereActorThree(_conn, up, name)
            trialing(_conn)
        elif updating=="10":
            up=input("Enter new composer: ")
            updateEarliestHereComposer(_conn, up, name)
            trialing(_conn)
        elif updating=="11":
            up=input("Enter new studio: ")
            updateEarliestHereStudio(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="11":
        name=input("Enter person's name: ")
        updating=input("Enter command code (1-18): ")
        if updating=="1":
            up=input("Enter new name: ")
            updateWorkedWithName(_conn, up, name)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new director: ")
            updateWorkedWithDirector(_conn, up, name)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new director: ")
            updateWorkedWithDirectorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="4":
            up=input("Enter new director: ")
            updateWorkedWithDirectorThree(_conn, up, name)
            trialing(_conn)
        elif updating=="5":
            up=input("Enter new director: ")
            updateWorkedWithDirectorFour(_conn, up, name)
            trialing(_conn)
        elif updating=="6":
            up=input("Enter new director: ")
            updateWorkedWithDirectorFive(_conn, up, name)
            trialing(_conn)
        elif updating=="7":
            up=input("Enter new producer: ")
            updateWorkedWithProducer(_conn, up, name)
            trialing(_conn)
        elif updating=="8":
            up=input("Enter new producer: ")
            updateWorkedWithProducerTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="9":
            up=input("Enter new producer: ")
            updateWorkedWithProducerThree(_conn, up, name)
            trialing(_conn)
        elif updating=="10":
            up=input("Enter new producer: ")
            updateWorkedWithProducerFour(_conn, up, name)
            trialing(_conn)
        elif updating=="11":
            up=input("Enter new producer: ")
            updateWorkedWithProducerFive(_conn, up, name)
            trialing(_conn)
        elif updating=="12":
            up=input("Enter new actor: ")
            updateWorkedWithActor(_conn, up, name)
            trialing(_conn)
        elif updating=="13":
            up=input("Enter new actor: ")
            updateWorkedWithActorTwo(_conn, up, name)
            trialing(_conn)
        elif updating=="14":
            up=input("Enter new actor: ")
            updateWorkedWithActorThree(_conn, up, name)
            trialing(_conn)
        elif updating=="15":
            up=input("Enter new actor: ")
            updateWorkedWithActorFour(_conn, up, name)
            trialing(_conn)
        elif updating=="16":
            up=input("Enter new actor: ")
            updateWorkedWithActorFive(_conn, up, name)
            trialing(_conn)
        elif updating=="17":
            up=input("Enter new composer: ")
            updateWorkedWithComposer(_conn, up, name)
            trialing(_conn)
        elif updating=="18":
            up=input("Enter new composer: ")
            updateWorkedWithComposerTwo(_conn, up, name)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    if updating=="12":
        year=int(input("Enter year: "))
        updating=input("Enter command code (1-28): ") 
        if updating=="1":
            up=input("Enter new movie: ")
            updateYearMovie(_conn, up, year)
            trialing(_conn)
        elif updating=="2":
            up=input("Enter new movie: ")
            updateYearMovieTwo(_conn, up, year)
            trialing(_conn)
        elif updating=="3":
            up=input("Enter new movie: ")
            updateYearMovieThree(_conn, up, year)
            trialing(_conn)
        elif updating=="4":
            up=input("Enter new movie: ")
            updateYearMovieFour(_conn, up, year)
            trialing(_conn)
        elif updating=="5":
            up=input("Enter new movie: ")
            updateYearMovieFive(_conn, up, year)
            trialing(_conn)
        elif updating=="6":
            up=input("Enter new director: ")
            updateYearDirector(_conn, up, year)
            trialing(_conn)
        elif updating=="7":
            up=input("Enter new director: ")
            updateYearDirectorTwo(_conn, up, year)
            trialing(_conn)
        elif updating=="8":
            up=input("Enter new director: ")
            updateYearDirectorThree(_conn, up, year)
            trialing(_conn)
        elif updating=="9":
            up=input("Enter new director: ")
            updateYearDirectorFour(_conn, up, year)
            trialing(_conn)
        elif updating=="10":
            up=input("Enter new director: ")
            updateYearDirectorFive(_conn, up, year)
            trialing(_conn)
        elif updating=="11":
            up=input("Enter new producer: ")
            updateYearProducer(_conn, up, year)
            trialing(_conn)
        elif updating=="12":
            up=input("Enter new producer: ")
            updateYearProducerTwo(_conn, up, year)
            trialing(_conn)
        elif updating=="13":
            up=input("Enter new producer: ")
            updateYearProducerThree(_conn, up, year)
            trialing(_conn)
        elif updating=="14":
            up=input("Enter new producer: ")
            updateYearProducerFour(_conn, up, year)
            trialing(_conn)
        elif updating=="15":
            up=input("Enter new producer: ")
            updateYearProducerFive(_conn, up, year)
            trialing(_conn)
        elif updating=="16":
            up=input("Enter new actor: ")
            updateYearActor(_conn, up, year)
            trialing(_conn)
        elif updating=="17":
            up=input("Enter new actor: ")
            updateYearActorTwo(_conn, up, year)
            trialing(_conn)
        elif updating=="18":
            up=input("Enter new actor: ")
            updateYearActorThree(_conn, up, year)
            trialing(_conn)
        elif updating=="19":
            up=input("Enter new actor: ")
            updateYearActorFour(_conn, up, year)
            trialing(_conn)
        elif updating=="20":
            up=input("Enter new actor: ")
            updateYearActorFive(_conn, up, year)
            trialing(_conn)
        elif updating=="21":
            up=input("Enter new composer: ")
            updateYearComposer(_conn, up, year)
            trialing(_conn)
        elif updating=="22":
            up=input("Enter new composer: ")
            updateYearComposer(_conn, up, year)
            trialing(_conn)
        elif updating=="23":
            up=input("Enter new composer: ")
            updateYearComposer(_conn, up, year)
            trialing(_conn)
        elif updating=="24":
            up=input("Enter new composer: ")
            updateYearComposer(_conn, up, year)
            trialing(_conn)
        elif updating=="25":
            up=input("Enter new composer: ")
            updateYearComposer(_conn, up, year)
            trialing(_conn)
        elif updating=="26":
            up=input("Enter new president: ")
            updateYearPresident(_conn, up, year)
            trialing(_conn)
        elif updating=="27":
            up=input("Enter new studio: ")
            updateYearStudio(_conn, up, year)
            trialing(_conn)
        elif updating=="28":
            up=input("Enter new studio: ")
            updateYearStudioTwo(_conn, up, year)
            trialing(_conn)
        else: 
            print("ERROR: Invalid command")
            trialing(_conn)
    else: 
        print("ERROR: Invalid command")
        trialing(_conn)

def trialing(_conn):
        
        trials=input("Enter command code (1-20, I/D/U/E): ")
        
        if trials=='1':
            enter_i=int(input("Enter a number: "))
            trial1(_conn, enter_i)
        elif trials=='2':
            enter=input("Enter a reviewer: ")
            trial2(_conn, enter)
        elif trials=='3':
            trial3(_conn)
        elif trials=='4':
            trial4(_conn)
        elif trials=='5':
            trial5(_conn)
        elif trials=='6':
            enter_i=int(input("Enter a number: "))
            trial6(_conn, enter_i)
        elif trials=='7':
            trial7(_conn)
        elif trials=='8':
            enter=input("Enter a director: ")
            trial8(_conn, enter)
        elif trials=='9':
            trial9(_conn)
        elif trials=='10':
            trial10(_conn)
        elif trials=='11':
            trial11(_conn)
        elif trials=='12':
            trial12(_conn)
        elif trials=='13':
            trial13(_conn)
        elif trials=='14':
            trial14(_conn)
        elif trials=='15':
            trial15(_conn)
        elif trials=='16':
            trial16(_conn)
        elif trials=='17':
            trial17(_conn)
        elif trials=='18':
            trial18(_conn)
        elif trials=='19':
            trial19(_conn)
        elif trials=='20':
            trial20(_conn)
        elif trials=='21':
            trial21(_conn)
        elif trials=='22':
            trial22(_conn)
        elif trials=='23':
            trial23(_conn)
        elif trials=='24':
            trial24(_conn)
        elif trials=='25':
            trial25(_conn)
        elif trials=='I':
            insertTuple(_conn)
        elif trials=="U":
            updateTuple(_conn)
        elif trials=='D':
            deleteTuple(_conn)
        elif trials=='E':
            print("Thank you. Have a nice day")
        else:
            print("ERROR: Invalid command")
            trialing(_conn)
            
            
def main():
    database = r"project.sqlite"
    
    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populateTables(conn)
        trialing(conn)
        
        

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
