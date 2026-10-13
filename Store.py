import sqlite3

conn = sqlite3.connect('nisha_store.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                  (name TEXT, amount INTEGER)''')

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
    print(f"\n--- HISAAB ---")
    print(f"Total: {total}")
    print(f"Average: {avg}")
    print(f"Top Seller: {top[0]} - {top[1]}")
    with open("hisaab.txt", "w") as f:
        f.write(f"Total: {total}, Avg: {avg}, Top: {top[0]} {top[1]}")

while True:
    print("\n--- NISHA STORE ---")
    print("1. Nayi Sale Add Karo")
    print("2. Report Dekho")
    print("3. Exit")
    choice = input("Aapka choice (1/2/3): ")
    if choice == '1':
        add_sale()
    elif choice == '2':
        show_report()
    elif choice == '3':
        print("Bye Bye! Dukaan band!")
        break
    else:
        print("Galat choice!")

conn.close()