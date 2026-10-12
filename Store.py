import sqlite3

# Nisha Store Management - Day 25 Project
conn = sqlite3.connect('nisha_store.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS sales
             (name TEXT, amount INTEGER)''')

# Data insert
sales = [('Anjali', 150), ('Riya', 300), ('Pooja', 180), ('Riya', 73)]
c.executemany('INSERT INTO sales VALUES (?,?)', sales)

# Total aur Average
c.execute('SELECT SUM(amount) FROM sales')
total = c.fetchone()[0]

c.execute('SELECT AVG(amount) FROM sales')
avg = c.fetchone()[0]

c.execute('SELECT name, MAX(amount) FROM sales')
top = c.fetchone()

print(f"Total Sale: {total}")
print(f"Average Sale: {avg:.0f}")
print(f"Top Seller: {top[0]} - {top[1]}")

# File me save karna
with open('hisaab.txt', 'w') as f:
    f.write(f"Total: {total}\nAverage: {avg:.0f}\nTop: {top[0]}")

conn.commit()
conn.close()
