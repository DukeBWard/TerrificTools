import psycopg2
import dbcfg as cfg
from sshtunnel import SSHTunnelForwarder

username = cfg.sql["user"]
password = cfg.sql["passwd"]
dbName = "p32001_12"


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
        curs = conn.cursor()
        print("Database connection established")
        conn.close()
except:
    print("Connection failed")