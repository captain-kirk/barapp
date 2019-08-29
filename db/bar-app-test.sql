CREATE SCHEMA barapptest
  CREATE TABLE bars (
    bar_id serial NOT NULL PRIMARY KEY,
    info jsonb NOT NULL
  );
  INSERT INTO bars VALUES (1, '{"name": "The Slammer", "Address": "500 SE 8th Ave, Portland, OR 97214", "Phone":"(503) 232-6504"}');
  INSERT INTO bars VALUES (2, '{"name": "Mad Hanna", "Address": "6129 NE Fremont, Portland, OR 97213", "Phone":"(503) 288-2944"}');
  FROM 'pwd' DELIMITER ',' CSV HEADER;
  CREATE TABLE users (
    user_id serial NOT NULL PRIMARY KEY,
    info jsonb NOT NULL
  );
  CREATE TABLE tags (
    tag_id serial NOT NULL PRIMARY KEY,
    info jsonb NOT NULL
  );