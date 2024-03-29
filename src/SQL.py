import psycopg2
import psycopg2.extras
import dbcfg as cfg
from sshtunnel import SSHTunnelForwarder
import Driver

username = cfg.sql["user"]
password = cfg.sql["passwd"]
dbName = "p32001_12"

# 
# 
# YOU GOTTA RUN THIS FILE FIRST!!!
# 
# 

def main():

    try:
        with SSHTunnelForwarder(('starbug.cs.rit.edu', 22),
                                ssh_username=username,
                                ssh_password=password,
                                remote_bind_address=('localhost', 5432)) as server:
            server.start()
            print("SSH tunnel established")
            params = {
                'database': dbName,
                'user': username,
                'password': password,
                'host': 'localhost',
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            work_mem = 2048
            cursor.execute('SET work_mem TO %s', (work_mem,))
            cursor.execute('SHOW work_mem')

            print("Database connection established")
            Driver.driver(conn,cursor)
            conn.close()

    except Exception as e:
        print(e)
        print("Connection failed")
    finally:
        conn.close()

if __name__ == "__main__":
    main()