import sqlite3


class SQLite():
    def __init__(self, file='db.sqlite3'):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    with SQLite("data.db") as cur:
        sql = """
CREATE TABLE "adresy" (
    "zkratka" TEXT NOT NULL,
    "adresy" TEXT NOT NULL,
    "user" TEXT,
    PRIMARY KEY("zkratka")
);
"""
        cur.execute(sql)

        sql = """
CREATE TABLE "user"(
    "login" TEXT,
    "passwd" TEXT,
    PRIMARY KEY("login")
);
"""
        cur.execute(sql)