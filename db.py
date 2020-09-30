import sqlite3
from sqlite3 import Error
from SpsParser import Point

DB_TABLE = 'plan'


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_record_from_parsed_sps(conn, sps_data):
    line = str(int(sps_data[1]))
    point = str(int(sps_data[2]))
    line_point = line + point
    easting = sps_data[10]
    northing = sps_data[11]
    print(line_point)

    c = conn.cursor()
    c.execute("SELECT count(*) FROM " + DB_TABLE + " WHERE lp = ?", (line_point,))
    data = c.fetchone()[0]
    if data == 0:
        """
            insert record
        """
        sql_insert = "INSERT INTO " + DB_TABLE + "(lp, easting, northing) VALUES (?, ?, ?);"

        data = (line_point, easting, northing)
        c.execute(sql_insert, data)
        conn.commit()

    c.close()


def get_record_for_point(conn, sps_point):
    """

    :param conn:
    :param Point sps_point:
    :return:
    """
    line_point = str(int(sps_point.line)) + str(int(sps_point.point))

    c = conn.cursor()

    c.execute("SELECT easting, northing FROM " + DB_TABLE + " WHERE lp=?", (line_point,))

    rows = c.fetchall()

    data = [rows[0][0], rows[0][1]]

    return data
