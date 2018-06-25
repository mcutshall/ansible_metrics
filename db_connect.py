import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="none",
                  db="metrics")
x = conn.cursor()

try:
   x.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
   conn.commit()
except:
   conn.rollback()

conn.close()


def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False
