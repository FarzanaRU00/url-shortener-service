-- database model 

DROP TABLE IF EXISTS urlshortener

CREATE TABLE urlshortener (
    original_url = TEXT NOT NULL
    short_url TEXT NOT NULL
)