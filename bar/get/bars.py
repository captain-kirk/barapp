#!/usr/bin/python
import psycopg2
from config import config

def get_bars():
  """ query data from the bars table """
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("SELECT bar_id, info FROM v1.bars ORDER BY bar_id")
    print("The number of bars: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
      print(row)
      row = cur.fetchone()
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

if __name__ == '__main__':
  get_bars()