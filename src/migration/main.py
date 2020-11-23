import sys
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def main():
    db_file = sys.argv[1]
    sql_file = open(sys.argv[2])
    sql_as_string = sql_file.read()
    print(sql_as_string)
    conn = create_connection(db_file)
    cursor = conn.cursor()
    cursor.executescript(sql_as_string)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    if (len(sys.argv) > 3 or len(sys.argv) < 3):
        raise Error('Invalid number of arguments')

    main()
