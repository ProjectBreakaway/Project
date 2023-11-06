CREATE TABLE user (
    u_Username char(20) not null,
    u_Password varchar(30) not null
);
CREATE TABLE review (
    r_reviewKey decimal(4, 0) not null, 
    r_movieTitle varchar(40) not null
);
CREATE TABLE director(
    d_Name varchar(30) not null, 
    d_Year decimal(4, 0) not null,
    d_FirstFilm varchar(40) not null
);
CREATE TABLE producer(
    p_Name varchar(30) not null, 
    p_Year decimal(4, 0) not null,
    p_FirstFilm varchar(40) not null
);
CREATE TABLE actor(
    a_Name varchar(30) not null, 
    a_Year decimal(4, 0) not null,
    a_FirstFilm varchar(40) not null
);
CREATE TABLE composer(
    c_Name varchar(30) not null, 
    c_Year decimal(4, 0) not null,
    c_FirstFilm varchar(40) not null
);
CREATE TABLE studio(
    s_Name varchar(30) not null, 
    s_FoundingDate decimal(4, 0) not null,
    s_currentPresident varchar(30) not null,
    s_FirstFilm varchar(40) not null
);
CREATE TABLE president(
    pre_Name varchar(30) not null,
    pre_Year decimal(4, 0) not null, 
    pre_Studio varchar(30) not null,
    pre_YearsRan decimal(3) not null,
    pre_FirstFilm varchar(40) not null
);
CREATE TABLE movie(
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
    m_Review decimal(4, 0)
);
CREATE TABLE firstFilm (
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
    f_StudioTwo varchar(40)
);
CREATE TABLE workedWith(
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
    w_ComposerThree varchar(40) 
);
CREATE TABLE year(
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
    y_Studio varchar(40)
);