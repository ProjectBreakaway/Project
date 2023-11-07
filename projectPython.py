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
        sql =""""CREATE TABLE user(
                u_Username char(20) not null,
                u_Password varchar(30) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE review(
                r_reviewKey decimal(4, 0) not null, 
                r_movieTitle varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE director(
                d_Name varchar(30) not null, 
                d_Year decimal(4, 0) not null,
                d_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE producer(
                p_Name varchar(30) not null, 
                p_Year decimal(4, 0) not null,
                p_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE actor(
                a_Name varchar(30) not null, 
                a_Year decimal(4, 0) not null,
                a_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE composer(
                c_Name varchar(30) not null, 
                c_Year decimal(4, 0) not null,
                c_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE studio(
                s_Name varchar(30) not null, 
                s_FoundingDate decimal(4, 0) not null,
                s_currentPresident varchar(30) not null,
                s_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE president(
                pre_Name varchar(30) not null,
                pre_Year decimal(4, 0) not null, 
                pre_Studio varchar(30) not null,
                pre_YearsRan decimal(3) not null,
                pre_FirstFilm varchar(40) not null)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE movie(
                m_Title varchar(40) not null, 
                m_genre char(10) not null, 
                m_Year decimal(4, 0) not null, 
                m_Revenue decimal(15, 2) not null, 
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
                m_Review decimal(4, 0)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE earliestHere(
                e_Title varchar(40)
                e_Director varchar(40) not null,
                e_DirectorTwo varchar(40),
                e_DirectorThree varchar(40),
                e_Producer varchar(40) not null,
                e_ProducerTwo varchar(40),
                e_ProducerThree varchar(40),
                e_ProducerFour varchar(40),
                e_Actor varchar(40) not null,
                e_ActorTwo varchar(40),
                e_ActorThree varchar(40),
                e_ActorFour varchar(40),
                e_ActorFive varchar(40),
                e_Composer varchar(40) not null,
                e_ComposerTwo varchar(40),
                e_Studio varchar(40) not null,
                e_StudioTwo varchar(40))"""
        _conn.execute(sql)
        sql =""""CREATE TABLE workedWith(
                w_Name varchar(40) not null, 
                w_Director varchar(40) not null,
                w_DirectorTwo varchar(40),
                w_DirectorThree varchar(40),
                w_DirectorFour varchar(40),
                w_DirectorFivee varchar(40),
                w_Producer varchar(40) not null,
                w_ProducerTwo varchar(40),
                w_ProducerThree varchar(40),
                w_ProducerFour varchar(40),
                w_ProducerFive varchar(40),
                w_Actor varchar(40) not null,
                w_ActorTwo varchar(40),
                w_ActorThree varchar(40),
                w_ActorFour varchar(40),
                w_ActorFive varchar(40),
                w_Composer varchar(40) not null, 
                w_ComposerTwo varchar(40), 
                w_ComposerThree varchar(40))"""
        _conn.execute(sql)
        sql =""""CREATE TABLE year(
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
                y_PresidentTwo varchar(40),
                y_PresidentThree varchar(40),
                y_PresidentFour varchar(40),
                y_PresidentFive varchar(40), 
                y_Studio varchar(40),
                y_StudioTw varchar(40))"""
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
        sql = "DROP TABLE firstFilm"
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
    
def insertReview(_conn, _reviewKey, _movieTitle):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Review")
    try: 
        sql = "INSERT INTO review VALUES(?, ?)"
        args = [_reviewKey, _movieTitle]
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
    
    insertReview(_conn, 1, "The Lion King")
    insertReview(_conn, 2, "If")
    insertReview(_conn, 3, "Schindler's List")
    insertReview(_conn, 4, "Horizons West")
    insertReview(_conn, 5, "Sorcerer's Stone")
    insertReview(_conn, 6, "Tron")
    insertReview(_conn, 7, "Batteries Not Included")
    insertReview(_conn, 8, "The Prince of Egypt")
    insertReview(_conn, 9, "Duel")
    insertReview(_conn, 10, "Fear and Desire")
    insertReview(_conn, 11, "Dr Strangelove")
    insertReview(_conn, 12, "Max Dugan Returns")
    insertReview(_conn, 13, "Ironweed")
    insertReview(_conn, 14, "Nijinsky")
    insertReview(_conn, 15, "Moonlighting")
    insertReview(_conn, 16, "Diamond Head")
    insertReview(_conn, 17, "A Clockwork Orange")
    
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
    insertProducer(_conn, "Don Haln", 1955, "Beauty and the Beast")
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
    insertActor(_conn, "Patrick Stewart", 1940, "The Prince of Egypt")
    
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
        
def populateComposer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Composer")
    
    insertComposer(_conn, "Hans Zimmer", 1957, "Moonlighting")
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
    
    insertStudio(_conn, "Disney", 1923, "")
    insertStudio(_conn, "Dreamworks", 1994, "")
    insertStudio(_conn, "Universal Pictures", 1912, "")
    insertStudio(_conn, "Warner Bros", 1923, "")
    insertStudio(_conn, "Miracle Films", 1950, "")
    insertStudio(_conn, "Paramount", 1912, "")
    insertStudio(_conn, "Tri-Star", 1982, "")
    insertStudio(_conn, "Columbia", 1918, "")
    insertStudio(_conn, "Independent", 0, "Not Applicable")
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertPresident(_conn, _name, _year, _studio, _yearsRan, _firstFilm):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert President")
    try: 
        sql = "INSERT INTO president VALUES(?, ?, ?, ?, ?)"
        args = [_name, _year, _studio, _yearsRan, _firstFilm]
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
    
    insertPresident(_conn, "Jeffery Katzenberg", )
    insertPresident(_conn, "Walt Disney",)
    insertPresident(_conn, "Roy Disney",)
    insertPresident(_conn, "Bob Eisner", )
    
    
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
    insertMovie(_conn, "If", "Drama", 1968, 2300000, "Lindsay Anderson", NULL, "Lindsay Anderson", "Michael Medwin", NULL, "Malcolm McDowell", NULL, NULL, "Marc Wilkinson", NULL, "Paramount", 2)
    insertMovie(_conn, "Schindler's List", "Drama", 1993, 322200000, "Steven Spielberg", NULL, "Steven Spielberg", "Gerald Molen", "Branko Lustig", "Liam Neeson", "Ralph Fiennes", NULL, "John Williams", "Universal Pictures", 3)
    insertMovie(_conn, "Horizons West", "Western", 1952, 500000, "Budd Boetticher", NULL, "Albert Cohen", NULL, NULL, "Dennis Weaver", NULL, NULL, "Uncredited", NULL, "Universal Pictures", 4)
    insertMovie(_conn, "Sorcerer's Stone", "Fantasy", 2001, 1024000000, "Chris Columbus", NULL, "David Heyman", NULL, NULL,"Daniel Radcliffe", "Emma Watson", "Alan Rickman", "John Williams", "Warner Bros", 5)
    insertMovie(_conn, "Tron", "Science Fiction", 1982, 50000000, "Steven Lisberger", NULL, "Donald Kushner", NULL, NULL, "Jeff Bridges", NULL, NULL, "Wendy Carlos", "Disney", 6)
    insertMovie(_conn, "Batteries Not Included", "Horror", 1987, 65100000, "Matthew Robbins", NULL, "Ronald Schwary", NULL, NULL, "Hume Croyn", NULL, NULL, "James Horner", "Universal", 7)
    insertMovie(_conn, "The Prince of Egypt", "Drama", 20, 0000, "", NULL, "", NULL, NULL, "Ralph Fiennes", "Patrick Stewart", "", "", NULL, "Dreamworks", 8)
    insertMovie(_conn, "Duel", "Thriller", 1971, 450000, "Steven Speilberg", NULL, "Richard Matheson", NULL, NULL, "Dennis Weaver", NULL, NULL, "Billy Goldenberg", "Universal Studios",  9)
    insertMovie(_conn, "Fear and Desire", "War", 1952, 53000, "Stanley Kubrick", NULL, "Stanley Krubrick", NULL, NULL, "Frank Silvera", NULL, NULL, "Gerald Fried", "Independent", 10)
    insertMovie(_conn, "Dr Strangelove", "Satire", 1964, 9200000, "Stanley Kubrick", NULL, "Stanley Kubrick", NULL, NULL, "James Earl Jones", NULL, NULL, "Laurie Johnson", "Columbia", 11)
    insertMovie(_conn, "Max Dugan Returns", "Drama", 1983, 17613720, "Herbert Ross", NULL, "Herbert Ross", "Neil Simon", NULL, "Matthew Broderick", NULL, NULL, "David Shire", "Fox", 12)
    insertMovie(_conn, "Ironweed", "Drama", 1987, 7300000, "Hector Babenco", NULL, "Keith Barish", "William Kennedy", NULL, "Jack Nicholson", "Nathan Lane", NULL, "John Morris", "Tri-Star", 13)
    insertMovie(_conn, "Nijinsky", "Biographical", 1980, 1047454, "Herbert Ross", NULL, "Hugh Wheeler", "Romola Nijinsky", "Vaslav Nijinsky", "Jeremy Irons", NULL, NULL, "Uncredited", "Paramount", 14)
    insertMovie(_conn, "Moonlighting", "Drama", 1982, 2000000, "Jerzy Skilowski", NULL, "Mark Shivas", "Jerzy Skolimowski", "Michael White", "Jeremy Irons", NULL, NULL, "Stanley Myers", "Miracle Films", 15)
    insertMovie(_conn, "Diamond Head", "Romance", 1962, 4500000, "Guy Green", NULL, "Jerry Bresler", NULL, NULL, "Charlton Heston", NULL, NULL, "John Williams", "Columbia", 16)
    insertMovie(_conn, "A Clockwork Orange", "Crime", 1971, 1440000000, "Stanley Kurbrick", NULL, "Bill Butler", NULL, NULL, "Malcolm McDowell", NULL, NULL, "Wendy Carlos", NULL, "Warner Bros", 17)
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertEarliestHere(_conn, _movie, _directorO, directorTw, _producerO, producerTw, producerTr, 
    _actorO, actorTw, actorTr, _composerO):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert earliestHere")
    try: 
        sql = "INSERT INTO earliestHere VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_movie, _directorO, directorTw, _producerO, producerTw, producerTr, 
    _actorO, actorTw, actorTr, _composerO]
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
    
    insertEarliestHere(_conn, "The Lion King", "Roger Allers", "Rob Minkoff", )
    insertEarliestHere(_conn, "If", "Lindsay Anderson", NULL, )
    insertEarliestHere(_conn, "Schindler's List", NULL, )
    insertEarliestHere(_conn, "Horizons West", "Budd Boetticher", NULL, )
    insertEarliestHere(_conn, "Sorcerer's Stone", "Chris Columbus", NULL)
    insertEarliestHere(_conn, "Tron", "Steven Lisberger", NULL, )
    insertEarliestHere(_conn, "Batteries Not Included", "Matthew Robbins", NULL, )
    insertEarliestHere(_conn, "The Prince of Egypt", )
    insertEarliestHere(_conn, "Duel", "Steven Spielberg", NULL, )
    insertEarliestHere(_conn, "Fear and Desire", "Stanley Kubrick", NULL, )
    insertEarliestHere(_conn, "Dr Strangelove", NULL, NULL, )
    insertEarliestHere(_conn, "Max Dugan Returns", NULL, NULL, )
    insertEarliestHere(_conn, "Ironweed", "Herbert Ross", NULL, NULL, )
    insertEarliestHere(_conn, "Nijinsky", "Hector Babenco", NULL, )
    insertEarliestHere(_conn, "Moonlighting", "Jerzy Skilowski", NULL, NULL, )
    insertEarliestHere(_conn, "Diamond Head", "Guy Green", NULL, NULL, )
    insertEarliestHere(_conn, "A Clockwork Orange", NULL, NULL, )
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertWorkedWith(_conn, _name, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert workedWith")
    try: 
        sql = "INSERT INTO workedWith VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_name, _directorO, directorTw, directorTr, directorFo, 
                directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, _actorO, 
                actorTw, actorTr, actorFo, actorFi, _composerO]
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
    
    insertWorkedWith(_conn, "", )
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertYear(_conn, _year, _movie, _movietw, _movietr, _moviefo, _moviefi, 
               _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi,
               _studio, _studioTw):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Year")
    try: 
        sql = "INSERT INTO year VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_year, _movie, _movietw, _movietr, _moviefo, _moviefi, _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi, _studio, _studioTw]
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
               NULL, NULL)
    insertYear(_conn, 1891, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Romola Nijinsky", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1903, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Albert Cohoen", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1908, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Jerry Bresler", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1912, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Hugh Wheeler", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Universal Studios", "Paramount")
    insertYear(_conn, 1913, NULL, NULL, NULL, NULL, NULL, 
               "Guy Green", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1916, NULL, NULL, NULL, NULL, NULL, 
               "Budd Boetticher", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1918, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Columbia", NULL)
    insertYear(_conn, 1921, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Bill Butler", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1923, NULL, NULL, NULL, NULL, NULL, 
               "Lindsay Anderson", NULL, NULL, NULL, NULL, 
               "Lindsay Anderson", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Disney", "Warner Bros")
    insertYear(_conn, 1924, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               "Dennis Weaver", NULL, NULL, NULL, NULL, 
               NULL,NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1926, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Richard Matheson", "Marcia Nasatir", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "John Morris", NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1927, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Herbert Ross", "Neil Simon", NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "Laurie Johnson", NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1928, NULL, NULL, NULL, NULL, NULL, 
               "Stanley Kubrick", NULL, NULL, NULL, NULL, 
               "Stanley Kubrick", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1929, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Marc Wilkinson", NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1930, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Stanley Myers", NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1931, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "James Earl Jones", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1932, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "John Williams", NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1933, NULL, NULL, NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               "Jerzy Skilowski", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1935, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Gerald Molen", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1936, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Michael White", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Billy Goldenberg", NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1937, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Skomlimoski Jerzy", NULL, NULL, NULL, NULL,
               "Jack Nicholson", NULL, NULL, NULL, NULL,
               "David Shire", NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1938, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Mark Shivas", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1939, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Wendy Carlos", NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1940, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Patrick Stewart", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1943, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "Malcom McDowell", "Jeff Bridges", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1944, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Ronald Schwary", "Keith Barish", NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, )
    insertYear(_conn, 1945, NULL, NULL, NULL, NULL, NULL, 
               "Matthew Robbins", NULL, NULL, NULL, NULL,
               "Donald Kushner", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1946, NULL, NULL, NULL, NULL, NULL, 
               "Steven Spielberg", "Hector Babenco", NULL, NULL, NULL, 
               "Steven Spielberg", NULL, NULL, NULL, NULL,
               "Alan Rickman", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1948, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "David Hayman", NULL, NULL, NULL, NULL, 
               "Jeremy Irons", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1949, NULL, NULL, NULL, NULL, NULL, 
               "Roger Allers", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1950, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               "Miracle Films", NULL)
    insertYear(_conn, 1951, NULL, NULL, NULL, NULL, NULL, 
               "Steven Lisberger", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1952, "Horizon's West", "Fear and Desire", NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Liam Neeson", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL)
    insertYear(_conn, 1953, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               "James Horner", NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1956, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Nathan Lane", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1957, NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                "Hans Zimmer",  NULL, NULL, NULL, NULL, 
                NULL, NULL)
    insertYear(_conn, 1958, NULL, NULL, NULL, NULL, NULL, 
               "Chris Columbus",  NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL)
    insertYear(_conn, 1962, "Diamond Head", NULL, NULL, NULL, NULL,  
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Ralphe Fiennes", NULL, NULL, NULL, NULL,
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1964, "Dr Strangelove", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1968, "If", NULL, NULL, NULL, NULL,
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1971, "Duel", "A Clockwork Orange", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1980, "Nijinskhy", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1982, "Tron", "Moonlighting", NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Tri-Star", NULL)
    insertYear(_conn, 1987, "Batteries Not Included", "Ironweed", NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1993, "Schindler's List", NULL, NULL, NULL, NULL, 
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1994, "The Lion King", NULL, NULL, NULL, NULL,
               NULL,  NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Dreamworks", NULL)
    insertYear(_conn, 1989, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Daniel Radcliffe", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 1989, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               "Emma Watson", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 2001, "Sorcerer's Stone", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL)
    insertYear(_conn, 0, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL,  NULL, NULL, NULL, 
               "Uncredited", NULL, NULL, NULL, NULL, 
               "Independent", NULL)
    
    print("++++++++++++++++++++++++++++++++++")

#Example Route

def trial1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Genres with films with less than a billion in revenue: ")

    try:
        sql = """select genre
                from movie
                where revenue<1000000000"""

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
def trial2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def trial20(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ")

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = 'E'"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
        
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
        
def main():
    database = r"projectTable.sql"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populateTables(conn)
        
        trial1(conn)
        trial2(conn)
        trial3(conn)
        trial4(conn)
        trial5(conn)
        trial6(conn)
        trial7(conn)
        trial8(conn)
        trial9(conn)
        trial10(conn)
        trial11(conn)
        trial12(conn)
        trial13(conn)
        trial14(conn)
        trial15(conn)
        trial16(conn)
        trial17(conn)
        trial18(conn)
        trial19(conn)
        trial20(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
