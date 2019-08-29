#!/usr/bin/python
import psycopg2
from config import config
import csv 
import json

def add_bars():
  """ add data into the bars table """
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('bars.csv') as csvfile:
      barreader = csv.reader(csvfile, delimiter=',')
      for row in barreader:
        info = {
          "bar_name" : row[0],
          "bar_address" : row[1],
          "bar_phone" : row[2]
        }
        print(info)
        cur.execute("""INSERT INTO v1.bars (  info ) VALUES ( '{0}' ) """.format(json.dumps(info)))
        conn.commit()
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

if __name__ == '__main__':
  add_bars()