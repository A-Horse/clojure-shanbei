-- name: create-word-table
-- Create word table
create table if not exists word (
word text primary key,
meaning text not null,
learn_time integer default 0,
status integer default 0,
add_date datetime not null,
last_learn_date datetime,
audio_url text);               

