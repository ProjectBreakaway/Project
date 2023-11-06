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
    print("Insert User")
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
    insertReview(_conn, 2, "Sorceror's Stone")
    insertReview(_conn, 3, "Amazing Spider Man")
    insertReview(_conn, 4, "Spider-Man")
    insertReview(_conn, 5, "Jurrassic Park")
    insertReview(_conn, 6, "Schindler's List")
    insertReview(_conn, 7, "The Land Before Time")
    insertReview(_conn, 8, "The Prince of Egypt")
    insertReview(_conn, 9, "Infinity War")
    insertReview(_conn, 10, "Endgame")
    insertReview(_conn, 11, "Iron Man")
    insertReview(_conn, 12, "The Tom and Jerry Movie")
    insertReview(_conn, 13, "The Hunchback of Notre Dame")
    insertReview(_conn, 14, "The Batman")
    insertReview(_conn, 15, "The Hunger Games")
    insertReview(_conn, 16, "Tron")
    
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
    insertDirector(_conn, "Roger Allers", 1949, "Tron")
    insertDirector(_conn, "Rob Minkoff", 1962, "The Lion King")
    insertDirector(_conn, "Stanley Kubrick", 1928, "Fear and Desire")
    insertDirector(_conn, "Chris Columbus")

    
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
    
    insertActor(_conn, "Matthew Boderick", 1962, "Max Dugan Returns")
    insertActor(_conn, "Nathan Lane", 1956, "Ironweed")
    insertActor(_conn, "Jeremy Irons", 1948, "Nijinsky")
    insertActor(_conn, "James Earl Jones", 1931, "Dr Strangelove")
    insertActor(_conn, "Daniel Radcliffe", 19)
    insertActor(_conn, "Emma Watson", 19)
    insertActor(_conn, "Alan Rickman", 19)
    insertActor(_conn, "Tony Jay", 19)
    insertActor(_conn, "Jackie Chan", 19)
    insertActor(_conn, "Jack Black", 19)
    insertActor(_conn, "Ralph Fiennes", 19)
    
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
    insertComposer(_conn, "John Williams", 1932, "Diamond  Head")
    
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
    
    insertStudio(_conn, "Dreamworks",)
    insertStudio(_conn, "Disney", )
    insertStudio(_conn, "Universal", )
    insertStudio(_conn, "Warner Bros", )
    insertStudio(_conn, "Lionsgate", )
    insertStudio(_conn, "Miracle Films", 1950)
    insertStudio(_conn, "Paramount", 1912)
    insertStudio(_conn, "Sony", )
    insertStudio(_conn, "Tri-Star", )
    insertStudio(_conn, "Columbia", 1918)
    
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
    insertPresident(_conn, "Bob Eisner", )
    
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertMovie(_conn, _name, _genre, _year, _revenue, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO, composerTw, _studioO, studioTw, _review):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Movie")
    try: 
        sql = "INSERT INTO movie VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"#24
        args = [_name, _genre, _year, _revenue, _directorO, directorTw, directorTr, directorFo, 
                directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, _actorO, 
                actorTw, actorTr, actorFo, actorFi, _composerO, composerTw,
                _studioO, studioTw, _review]
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
    
    insertMovie(_conn, "The Lion King", "Dramedy", 1994, 968400000, "Roger Allers", "Rob Minkoff", NULL, NULL, NULL, "Don Hahn", NULL, NULL, NULL, NULL, "Matthew Boderick", "Nathan Lane", "Jeremy Irons", "James Earl Jones", NULL, "Hans Zimmer", NULL,  "Disney", NULL, 1)
    insertMovie(_conn, "Sorceror's Stone", "Fantasy", 2001, 1024000000, "Chris Columbus", NULL, NULL, NULL, NULL, "David Heyman", NULL, NULL, NULL, NULL, "Daniel Radcliffe", "Emma Watson", "Alan Rickman", NULL, NULL, "John Williams", NULL, "Warner Bros", NULL, 2)
    insertMovie(_conn, "The Amazing Spider Man", "Hero", 20)
    insertMovie(_conn, "Spider-Man", "Hero", 20)
    insertMovie(_conn, "Jurassic Park", "Science Fiction", 1993, 1057000000, "Steven Spielberg", NULL, NULL, NULL, NULL, "Kathleen Kennedy", "Gerald Molen", NULL, NULL, NULL, "")
    insertMovie(_conn, "Schindler's List", "Drama", 19, NULL, "Steven Spielberg")
    insertMovie(_conn, "The Land Before Time", "Drama", 19, "Steven Spielberg", "George Lucas", "Don Bluth")
    insertMovie(_conn, "The Prince of Egypt", "Drama", 19, )
    insertMovie(_conn, "Infinity War", "Hero", 20)
    insertMovie(_conn, "Endgame", "Hero", 20)
    insertMovie(_conn, "Iron Man", "Hero", 2005)
    insertMovie(_conn, "The Tom and Jerry Movie", "Comedy", )
    insertMovie(_conn, "The Hunchback of Notre Dame", "Drama", )
    insertMovie(_conn, "The Batman", "Hero", 20)
    insertMovie(_conn, "The Hunger Games", "Drama", 20)
    insertMovie(_conn, "Tron", "Science Fiction", 19)
    insertMovie(_conn, "Dr Strangelove", "Horror", 19)   
    insertMovie(_conn, "Max Dugan Returns", "Drama", 19) 
    
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertFirstFilm(_conn, _movie, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO, composerTw):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Year")
    try: 
        sql = "INSERT INTO year VALUES(?, ?, ?, ?, ?, ?, ?)"
        args = [_movie, _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO, composerTw]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")
        
def populateFirstFilm(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Movie")
    
    insertFirstFilm(_conn, "The Lion King")
    
    print("++++++++++++++++++++++++++++++++++")
    
def insertWorkedWith(_conn,  _directorO, directorTw, directorTr, 
    directorFo, directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, 
    _actorO, actorTw, actorTr, actorFo, actorFi, _composerO, composerTw):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert workedWith")
    try: 
        sql = "INSERT INTO movie VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [_directorO, directorTw, directorTr, directorFo, 
                directorFi, _producerO, producerTw, producerTr, producerFo, producerFi, _actorO, 
                actorTw, actorTr, actorFo, actorFi, _composerO, composerTw]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
        
    print("++++++++++++++++++++++++++++++++++")
    
def populateWorkedWith(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Movie")
    
    insertWorkedWith(_conn, "The Lion King")
    
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
    
    insertYear(_conn, 1953)
    insertYear(_conn, 1955)
    insertYear(_conn, 1994)
    insertYear(_conn, 2001)
    insertYear(_conn, 1912)
    insertYear(_conn, 1918)
    insertYear(_conn, 1950)
    insertYear(_conn, 1932)
    insertYear(_conn, 1957)
    insertYear(_conn, 1962)
    insertYear(_conn, 1956)
    insertYear(_conn, 1948)
    insertYear(_conn, 1931)
    insertYear(_conn, )
    
    print("++++++++++++++++++++++++++++++++++")

#Example Route

def pcsByMaker(_conn):
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
    populateFirstFilm(_conn)
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

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
