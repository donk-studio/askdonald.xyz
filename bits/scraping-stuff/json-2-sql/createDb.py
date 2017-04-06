import sqlite3
import json

# CREATE DATABASE
conn = sqlite3.connect('ASKDONALD.db')
print "Opened database successfully";

# CREATE TABLE
conn.execute('''CREATE TABLE TWEETS
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       DATE TEXT NOT NULL,
       TEXT TEXT NOT NULL,
	   SOURCE TEXT NOT NULL);''')
print "Table created successfully";

# ITERATE THROUGH JSON
with open('source.json') as json_data:
    data = json.load(json_data)
	
    i = 0
	
    for tweet in data:
        i += 1
		
        tDate = (tweet['created_at'])
        tText = (tweet['text'])
        tSource = "https://twitter.com/realDonaldTrump/status/" + tweet['id_str'] # there is no url attribute, but this creates a valid link
		
        conn.execute("INSERT INTO TWEETS (DATE,TEXT,SOURCE) VALUES ( ?, ?, ?);", (tDate, tText, tSource))
        conn.commit() #can maybe just call this once at end? really slows down insert
		
        print(str(i))
        print(tDate, tText, tSource)
	
    print("insert complete")
	
conn.close()