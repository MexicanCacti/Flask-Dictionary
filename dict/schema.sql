DROP TABLE IF EXISTS en_sp

CREATE TABLE en_sp(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    en TEXT UNIQUE NOT NULL,
    sp TEXT,
    ex TEXT
);
