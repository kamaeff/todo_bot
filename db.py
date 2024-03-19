import psycopg2
from config import DATABASE, HOST, PORT , PASS, USER

async def conn():
  try:
    connection = psycopg2.connect(
        user=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DATABASE
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)

  except (Exception, psycopg2.Error) as error:
      print("Error while connecting to PostgreSQL", error)

  finally:
      if (connection):
          cursor.close()
          connection.close()
          print("PostgreSQL connection is closed")