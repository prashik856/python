CREATE TABLE VIDEOS(
    ID int(10) unsigned AUTO_INCREMENT,
    NAME text not null,
    VIEWS int(10) unsigned,
    primary key(ID)
);

CREATE TABLE MODELS(
    ID int(10) unsigned AUTO_INCREMENT,
    INNERID text not null,
    NAME text not null,
    VIEWS int(10) unsigned,
    primary key(ID)
);

CREATE TABLE MODELTAGS(
    ID int(10) unsigned AUTO_INCREMENT,
    VIDEOID int(10) unsigned,
    MODELID int(10) unsigned,
    primary key(ID),
    foreign key (VIDEOID) references VIDEOS(ID),
    foreign key (MODELID) references MODELS(ID)
);

