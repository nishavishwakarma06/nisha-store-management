
import sqlite3
from datetime import datetime
conn = sqlite3.connect('nisha_store.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sales (name TEXT, amount INTEGER)''')
def add_sale():
    name = input("Customer ka naam: ")
    amount = int(input("Kitne ki sale: "))
    cursor.execute("INSERT INTO sales VALUES (?,?)", (name, amount))
    conn.commit()
    print(f"{name} ki sale add ho gayi!")
def show_report():
    cursor.execute("SELECT * FROM sales")
    data = cursor.fetchall()
    if not data:
        print("Abhi koi data nahi hai")
        return
    total = sum([row[1] for row in data])
    avg = total // len(data)
    top = max(data, key=lambda x: x[1])
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    print(f"\n--- HISAAB ---\nTotal: {total} | Avg: {avg} | Count: {len(data)}\nTop: {top[0]} - {top[1]}")
    with open("hisaab.txt", "w", encoding="utf-8") as f:
        f.write(f"NISHA STORE - {date}\nTotal: {total}, Avg: {avg}\nTop: {top[0]}-{top[1]}\n")
        for n,a in data:
            f.write(f"{n} - {a}\n")
    print(">> file save ho gaya!")
def show_all():
    cursor.execute("SELECT rowid, * FROM sales")
    data = cursor.fetchall()
    if not data:
        print("Koi customer nahi")
        return
    print("\n--- SAARE CUSTOMERS ---")
    for i,n,a in data:
        print(f"{i}. {n} - {a}")
def delete_customer():
    show_all()
    try:
        idd = int(input("Delete kaunsa ID? "))
        cursor.execute("DELETE FROM sales WHERE rowid=?", (idd,))
        conn.commit()
        print(f"ID {idd} delete ho gaya!")
    except:
        print("Sahi number likho!")
while True:
    print("\n--- NISHA STORE [FINAL] ---\n1. Sale Add\n2. Report\n3. File Dekho\n4. Saare Customers\n5. Delete\n6. Exit")
    ch = input("Choice (1-6): ")
    if ch=='1': add_sale()
    elif ch=='2': show_report()
    elif ch=='3':
        try:
            print(open("hisaab.txt","r",encoding="utf-8").read())
        except:
            print("File nahi hai")
    elif ch=='4': show_all()
    elif ch=='5': delete_customer()
    elif ch=='6':
        print("Bye Bye! Project Complete!")
        break
conn.close()