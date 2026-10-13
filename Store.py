

    total = sum([row[1] for row in data])
    avg = total // len(data)
    top = max(data, key=lambda x: x[1])
    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    print(f"\n--- HISAAB ---")
    print(f"Total: {total}")
    print(f"Average: {avg}")
    print(f"Top Seller: {top[0]} - {top[1]}")

    # Day 27 - File me save karna
    with open("hisaab.txt", "w", encoding="utf-8") as f:
        f.write(f"NISHA STORE - HISAAB REPORT\n")
        f.write(f"Date: {date}\n")
        f.write(f"------------------------\n")
        f.write(f"Total Sale: {total}\n")
        f.write(f"Average Sale: {avg}\n")
        f.write(f"Top Customer: {top[0]} - {top[1]}\n")
        f.write(f"Total Customers: {len(data)}\n")
    print(">> hisaab.txt file me save ho gaya!")

def show_file():
    try:
        with open("hisaab.txt", "r", encoding="utf-8") as f:
            print("\n--- FILE KA HISAAB ---")
            print(f.read())
    except:
        print("File abhi bani nahi hai, pehle Report dekho (2 dabao)")

while True:
    print("\n--- NISHA STORE ---")
    print("1. Nayi Sale Add Karo")
    print("2. Report Dekho + File Save Karo")
    print("3. File Ka Hisaab Dekho")
    print("4. Exit")
    choice = input("Aapka choice (1/2/3/4): ")
    if choice == '1':
        add_sale()
    elif choice == '2':
        show_report()
    elif choice == '3':
        show_file()
    elif choice == '4':
        print("Bye Bye! Dukaan band!")
        break
    else:
        print("Galat choice!")

conn.close()