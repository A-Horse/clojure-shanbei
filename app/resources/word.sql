-- name: add-word
-- add word to table
insert into word (word, meaning, add_date)
value (:word, :meaning, now());
