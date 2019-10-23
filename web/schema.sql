-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS group;
DROP TABLE IF EXISTS treatment;

CREATE TABLE group (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_type TEXT NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP
);

CREATE TABLE treatment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP,
  group_id INTEGER NOT NULL,
  treatment_type TEXT NOT NULL,
  FOREIGN KEY (group_id) REFERENCES group (id)
);
