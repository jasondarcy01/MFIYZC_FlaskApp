# import sqlite3
# import pandas as pd

# with sqlite3.connect("mfiyzc.db") as connection:
#   c = connection.cursor()
#   # c.execute("""DROP TABLE users""")
#   # c.execute("""CREATE TABLE users(name text, zipcode int, inter1 text, inter2 text, inter3 text )""")
#   # c.execute('INSERT INTO users VALUES("Jane Parker", 10022, "ice skating", "dancing", "reading")')
#   # c.execute('INSERT INTO users VALUES("Bob Smith", 10022, "boxing", "cars", "beers")')
#   c.execute('SELECT * FROM users')
#   rows = c.fetchall()
#   cols = [desc[0] for desc in c.description]
#   df = pd.DataFrame(rows, columns=cols)
#   df = df.set_index('name')
  # print df

#think about goal of matrix
  # Y = df[["name"]]
  # X = df[["inter1","inter2","inter3"]]

  # pd.options.mode.chained_assignment = None

  # X["zipcode"].replace([])

# 1. non-database logic. return set of neighbor_zips from list based on client zip input
# def foo(zip, zipcodes):
#     x = zipcodes.index(zip)
#     neighbors = zipcodes[x-1:x+2]
#     return neighbors

# foo(11377,zipcodes)

# c.execute('SELECT * FROM users WHERE zipcode='' ')



# 2. match set of zips to the database



