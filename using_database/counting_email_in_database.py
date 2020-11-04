import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    (emailname, orgname) = email.split('@')
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgname,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (orgname,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (orgname,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()