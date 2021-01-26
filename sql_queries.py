# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
# set songplay_id as SERIAL type to automatically generate the id number
songplay_table_create = ("""
CREATE TABLE songplays 
(songplay_id SERIAL, 
start_time TIMESTAMP NOT NULL, 
user_id INT NOT NULL, 
level VARCHAR NOT NULL, 
song_id VARCHAR(18), 
artist_id VARCHAR(18), 
session_id INT NOT NULL, 
location VARCHAR NOT NULL, 
user_agent VARCHAR NOT NULL,
PRIMARY KEY(songplay_id));
""")

# user_id, first_name, last_name, gender, level
user_table_create = ("""
CREATE TABLE users
(user_id INT, 
first_name VARCHAR NOT NULL, 
last_name VARCHAR NOT NULL, 
gender CHAR(1) NOT NULL, 
level VARCHAR NOT NULL,
PRIMARY KEY(user_id));
""")

# song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE songs
(song_id VARCHAR(18), 
title VARCHAR NOT NULL, 
artist_id VARCHAR(18) NOT NULL, 
year INT NOT NULL, 
duration FLOAT NOT NULL,
PRIMARY KEY(song_id));
""")

# artist_id, name, location, latitude, longitude
artist_table_create = ("""
CREATE TABLE artists
(artist_id VARCHAR(18),
name VARCHAR NOT NULL,
location VARCHAR NOT NULL,
latitude FLOAT,
longitude FLOAT,
PRIMARY KEY(artist_id));
""")

# start_time, hour, day, week, month, year, weekday
time_table_create = ("""
CREATE TABLE time
(start_time TIMESTAMP,
hour INT NOT NULL,
day INT NOT NULL,
week INT NOT NULL,
month INT NOT NULL,
year INT NOT NULL,
weekday INT NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# update users' level in case there is a upgrade or downgrade of the plan.
user_table_insert = ("""
INSERT INTO users
    (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE SET level = excluded.level;
""")

# for songs tables, we expect their values are unlikely to change
song_table_insert = ("""
INSERT INTO songs
    (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING
""")

# 'artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude'
# for artists tables, we expect their values are unlikely to change
artist_table_insert = ("""
INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING
""")

# for time tables, we expect their values are unlikely to change
time_table_insert = ("""
INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING
""")

# FIND SONGS

# by matching song, artist and length
song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM songs
JOIN artists
ON songs.artist_id = artists.artist_id
WHERE
songs.title = %s
AND artists.name = %s
AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]