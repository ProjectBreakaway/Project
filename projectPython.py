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
                m_DirectorThree varchar(40),
                m_Producer varchar(40) not null,
                m_ProducerTwo varchar(40),
                m_ProducerThree varchar(40),
                m_ProducerFour varchar(40),
                m_Actor varchar(40) not null,
                m_ActorTwo varchar(40),
                m_ActorThree varchar(40),
                m_ActorFour varchar(40),
                m_ActorFive varchar(40),
                m_ActorSix varchar(40),
                m_AtorSeven varchar(40),
                m_Composer varchar(40) not null,
                m_ComposerTwo varchar(40),
                m_Studio varchar(40) not null,
                m_Review decimal(4, 0)"""
        _conn.execute(sql)
        sql =""""CREATE TABLE firstFilm(
                f_Title varchar(40)
                f_Director varchar(40) not null,
                f_DirectorTwo varchar(40),
                f_DirectorThree varchar(40),
                f_Producer varchar(40) not null,
                f_ProducerTwo varchar(40),
                f_ProducerThree varchar(40),
                f_ProducerFour varchar(40),
                f_Actor varchar(40) not null,
                f_ActorTwo varchar(40),
                f_ActorThree varchar(40),
                f_ActorFour varchar(40),
                f_ActorFive varchar(40),
                f_Composer varchar(40) not null,
                f_ComposerTwo varchar(40),
                f_Studio varchar(40) not null,
                f_StudioTwo varchar(40))"""
        _conn.execute(sql)
        sql =""""CREATE TABLE workedWith(
                w_Director varchar(40) not null,
                w_DirectorTwo varchar(40),
                w_DirectorThree varchar(40),
                w_DirectorFour varchar(40),
                w_DirectorFivee varchar(40),
                w_Producer varchar(40) not null,
                w_ProducerTwo varchar(40),
                w_ProducerThree varchar(40),
                w_ProducerFour varchar(40),
                w_ProducerFivee varchar(40),
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
                y_Studio varchar(40))"""
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
    insertReview(_conn, 6, "The Hunchback of Notre Dame")
    insertReview(_conn, 7, "Tron")
    insertReview(_conn, 8, "Raiders of the Lost Ark")
    insertReview(_conn, 9, "Batteries Not Included")
    insertReview(_conn, 10, "Beauty and the Beast")
    insertReview(_conn, 11, "Duel")
    insertReview(_conn, 12, "Fear and Desire")
    insertReview(_conn, 13, "Dr Strangelove")
    insertReview(_conn, 14, "Max Dugan Returns")
    insertReview(_conn, 15, "Ironweed")
    insertReview(_conn, 16, "Nijinsky")
    insertReview(_conn, 17, "Moonlighting")
    insertReview(_conn, 18, "Diamond Head")
    insertReview(_conn, 19, "A Clockwork Orange")
    insertReview(_conn, 20, "The Prince of Egypt")
    
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
    
    insertProducer(_conn, "Kathleen Kennedy", 1953, "Raiders of the Lost Ark")
    insertProducer(_conn, "Gerald Molen", 1935, "Batteries Not Included")
    insertProducer(_conn, "Don Haln", 1955, "Beauty and the Beast")
    insertProducer(_conn, "David Hayman", 19, "Sorcerer's Stone")
    insertProducer(_conn, "Steven Spielberg", 1946, "Schindler's List")
    insertProducer(_conn, "Michael Medwin", 1923, "If")
    insertProducer(_conn, "Stanley Kubrick", 1928, "Fear and Desire")
    insertProducer(_conn, "Donald Kushner", 19, "Tron")
    insertProducer(_conn, "Neil Simon", 19, "Nijinsky")
    insertProducer(_conn, "Ronald Schwary", 19, "Batteries Not Included")
    insertProducer(_conn, "Richard Matheson", 19, "Duel")
    insertProducer(_conn, "Keith Barish", 19, "Ironweed")
    insertProducer(_conn, "William Kennedy", 19, "Ironweed")
    insertProducer(_conn, "Herbert Ross", 19, "Max Dugan Returns")
    insertProducer(_conn, "Hugh Wheeler", 19, "Nijinsky")
    insertProducer(_conn, "Romola Nijinsky", 19, "Nijinsky")
    insertProducer(_conn, "Vaslav Nijinsky", 19, "Nijinsky")
    insertProducer(_conn, "Mark Shivas", 19, "Moonlighting")
    insertProducer(_conn, "Jerzy Skolimowski", 19, "Moonlighting")
    insertProducer(_conn, "Michael White", 19, "Moonlighting")
    insertProducer(_conn, "Jerry Bresler", 19, "Diamond Head")
    insertProducer(_conn, "Albert Cohen", 19, "Horizons West")
    insertProducer(_conn, "Bill Butler", 19, "A Clockwork Orange")
    insertProducer(_conn, "Lindsay Anderson", 19, "If")
    
    
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
    insertDirector(_conn, "Chris Columbus", 1958, "Sorcerer's Stone")
    insertDirector(_conn, "George Lucas", 19, "Star Wars")
    insertDirector(_conn, "Steven Lisberger", 19, "Tron")
    insertDirector(_conn, "Herbert Ross", 19, "Nijinsky")
    insertDirector(_conn, "Hector Babenco", 19, "Ironweed")
    insertDirector(_conn, "Guy Green", 19, "Diamond Head")
    insertDirector(_conn, "Budd Boetticher", 19, "Horizons West")
    insertDirector(_conn, "Jerzy Skilowski", 19, "Moonlighting")
    insertDirector(_conn, "Lindsay Anderson", 19, "If")
    insertDirector(_conn, "Matthew Robbins", 19, "Batteries Not Included")
    insertDirector(_conn, "Budd Boetticher", 19, "Horizons West")

    
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
    insertActor(_conn, "Dennis Weaver", 19, "Horizons West")
    insertActor(_conn, "Jeff Bridges", 1943, "Tron")
    insertActor(_conn, "Patrick Stewart", 1943, "The Prince of Egypt")
    
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
    
    insertMovie(_conn, "The Lion King", "Dramedy", 1994, 968400000, "Roger Allers", "Rob Minkoff", "Don Hahn", NULL, NULL, "Nathan Lane", "Matthew Broderick", "Jeremy Irons", "Hans Zimmer", "Disney", 1)
    insertMovie(_conn, "Sorcerer's Stone", "Fantasy", 2001, 1024000000, "Chris Columbus", NULL, "David Heyman", NULL, NULL,"Daniel Radcliffe", "Emma Watson", "Alan Rickman", "John Williams", "Warner Bros", 5)
    insertMovie(_conn, "Schindler's List", "Drama", 1993, 322200000, "Steven Spielberg", NULL, "Steven Spielberg", "Gerald Molen", "Branko Lustig", "Liam Neeson", "Ralph Fiennes", NULL, "John Williams", "Universal Pictures", 3)
    insertMovie(_conn, "The Prince of Egypt", "Drama", 20, 0000, "", NULL, "", NULL, NULL, "Ralph Fiennes", "Patrick Stewart", "", "", NULL, "Dreamworks", 20)
    insertMovie(_conn, "Tron", "Science Fiction", 1982, 50000000, "Steven Lisberger", NULL, "Donald Kushner", NULL, NULL, "Jeff Bridges", NULL, NULL, "Wendy Carlos", "Disney", 7)
    insertMovie(_conn, "Dr Strangelove", "Satire", 19, 0, "Stanley Kubrick", NULL, "Stanley Kubrick", NULL, NULL, "James Earl Jones", NULL, NULL, "Laurie Johnson", "Columbia", 13)   
    insertMovie(_conn, "Max Dugan Returns", "Drama", 1983, 17613720, "Herbert Ross", NULL, "Herbert Ross", "Neil Simon", NULL, "Matthew Broderick", NULL, NULL, "David Shire", "Fox", 17)
    insertMovie(_conn, "Batteries Not Included", "Horror", 1987, 65100000, "Matthew Robbins", NULL, "Ronald Schwary", NULL, NULL, "Hume Croyn", NULL, NULL, "James Horner", "Universal", 9)
    insertMovie(_conn, "Duel", "Thriller", 1971, 450000, "Steven Speilberg", NULL, "Richard Matheson", NULL, NULL, "Dennis Weaver", NULL, NULL, "Billy Goldenberg", "Universal Studios",  11)
    insertMovie(_conn, "Fear and Desire", "War", 1952, 53000, "Stanley Kubrick", NULL, "Stanley Krubrick", NULL, NULL, "Frank Silvera", NULL, NULL, "Gerald Fried", "Independent", 12)
    insertMovie(_conn, "Ironweed", "Drama", 1987, 7300000, "Hector Babenco", NULL, "Keith Barish", "William Kennedy", NULL, "Jack Nicholson", "Nathan Lane", NULL, "John Morris", "Tri-Star", 15)
    insertMovie(_conn, "Nijinsky", "Biographical", 1980, 1047454, "Herbert Ross", NULL, "Hugh Wheeler", "Romola Nijinsky", "Vaslav Nijinsky", "Jeremy Irons", NULL, NULL, "Uncredited", "Paramount", 16)
    insertMovie(_conn, "Moonlighting", "Drama", 1982, 2000000, "Jerzy Skilowski", NULL, "Mark Shivas", "Jerzy Skolimowski", "Michael White", "Jeremy Irons", NULL, NULL, "Stanley Myers", "Miracle Films", 17)
    insertMovie(_conn, "Diamond Head", "Romance", 1962, 4500000, "Guy Green", NULL, "Jerry Bresler", NULL, NULL, "Charlton Heston", NULL, NULL, "John Williams", "Columbia", 18)
    insertMovie(_conn, "Horizons West", "Western", 1952, 500000, "Budd Boetticher", NULL, "Albert Cohen", NULL, NULL, "Dennis Weaver", NULL, NULL, "Uncredited", NULL, "Universal Pictures", 7)
    insertMovie(_conn, "A Clockwork Orange", "Crime", 1971, 1440000000, "Stanley Kurbrick", NULL, "Bill Butler", NULL, NULL, "Malcolm McDowell", NULL, NULL, "Wendy Carlos", NULL, "Warner Bros", 19)
    insertMovie(_conn, "If", "Drama", 1968, 2300000, "Lindsay Anderson", NULL, "Lindsay Anderson", "Michael Medwin", NULL, "Malcolm McDowell", NULL, NULL, "Marc Wilkinson", NULL, "Paramount", 2)
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertEarliestHere(_conn, _movie, _directorO, directorTw, _producerO, producerTw, producerTr, 
    _actorO, actorTw, actorTr, _composerO):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert earliestHere")
    try: 
        sql = "INSERT INTO earliestHere VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_movie, _directorO, directorTw , _producerO, producerTw, producerTr, 
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
    
    insertEarliestHere(_conn, "The Lion King")
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertWorkedWith(_conn, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert workedWith")
    try: 
        sql = "INSERT INTO workedWith VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_directorO, directorTw, directorTr, directorFo, 
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
    
    insertWorkedWith(_conn, "")
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertYear(_conn, _year, _movie, _movietw, _movietr, _moviefo, _moviefi, 
               _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi,
               _studio):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Year")
    try: 
        sql = "INSERT INTO year VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_year, _movie, _movietw, _movietr, _moviefo, _moviefi, _director, _directortw, _directortr, _directorfo, _directorfi,
               _producer, _producertw, _producertr, _producerfo, _producerfi,
               _actor, _actortwo, _actortre, _actorfo, _actorfi,
               _composer, _composertwo, _composertr, _composerfo, _composerfi, _studio]
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
    
    insertYear(_conn, 1953, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, "Kathleen Kennedy", NULL, NULL, NULL, NULL, 
               NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
    insertYear(_conn, 1955, )
    insertYear(_conn, 1994, )
    insertYear(_conn, 2001, "Sorcerer's Stone", )
    insertYear(_conn, 1912, )
    insertYear(_conn, 1918, )
    insertYear(_conn, 1950, )
    insertYear(_conn, 1932, )
    insertYear(_conn, 1957, )
    insertYear(_conn, 1971, )
    insertYear(_conn, 1987, )
    insertYear(_conn, 1968, )
    insertYear(_conn, 1952, )
    insertYear(_conn, 1962, )
    insertYear(_conn, 1956, )
    insertYear(_conn, 1948, )
    insertYear(_conn, 1931, )
    insertYear(_conn, 2001, )
    insertYear(_conn, 1993, )
    insertYear(_conn, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "Uncredited", NULL, NULL, NULL, NULL, NULL)
    
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
