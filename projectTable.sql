CREATE TABLE user (
    u_Username char(20) NOT NULL,
    u_Password varchar(30) NOT NULL
);
CREATE TABLE review (
    r_reviewKey integer not null, 
    r_author varchar(20) not null, 
    r_movieTitle varchar(40) not null
);
CREATE TABLE director(
    d_Name varchar(30) not null, 
    d_Year integer not null,
    d_FirstFilm varchar(40) not null
);
CREATE TABLE producer(
    p_Name varchar(30) not null, 
    p_Year integer not null,
    p_FirstFilm varchar(40) not null
);
CREATE TABLE actor(
    a_Name varchar(30) not null, 
    a_Year integer not null,
    a_FirstFilm varchar(40) not null
);
CREATE TABLE composer(
    c_Name varchar(30) not null, 
    c_Year integer not null,
    c_FirstFilm varchar(40) not null
);
CREATE TABLE studio(
    s_Name varchar(30) not null, 
    s_Year integer not null,
    s_President varchar(30) not null,
    s_FirstFilm varchar(40) not null
);
CREATE TABLE president(
    pre_Name varchar(30) not null,
    pre_Year integer not null, 
    pre_Studio varchar(30) not null,
    pre_YearsRan integer not null
);
CREATE TABLE movie(
    m_Title varchar(40) not null, 
    m_genre char(10) not null, 
    m_Year integer not null, 
    m_Revenue integer not null, 
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
    m_Review integer not null
);
CREATE TABLE earliestHere (
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
    e_Studio varchar(40)
);
CREATE TABLE workedWith(
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
);
CREATE TABLE year(
    y_year integer not null, 
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
);