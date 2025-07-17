from db import get_connection, initialize_db

# Initialize DB and table
initialize_db()

def view_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("No contacts found.")
        return
    for row in rows:
        print(f"\nID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        for row in rows:
            print(f"\nID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
    else:
        print("Contact not found.")

def update_contact():
    contact_id = input("Enter contact ID to update: ").strip()
    name = input("New name: ").strip()
    phone = input("New phone: ").strip()
    email = input("New email: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()
    print("Contact updated.")

def delete_contact():
    contact_id = input("Enter contact ID to delete: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    print("Contact deleted.")

def main():
    while True:
        print("\n--- Contact Book (SQLite) ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
