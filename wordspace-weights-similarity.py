import mysql.connector
cnx = mysql.connector.connect(user='research', password='research', host='stage-db-2.gavagai.se', database='research')

cursor1 = cnx.cursor(buffered=True)

query1 = ("select term from TermInformation where term like" + '"' + "%beautiful%" + '"')
cursor1.execute(query1)
for row in cursor1:
    print(row)

