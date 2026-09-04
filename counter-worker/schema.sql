CREATE TABLE IF NOT EXISTS completion_counter (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  total INTEGER NOT NULL DEFAULT 0 CHECK (total >= 0)
);
