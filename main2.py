import json
import os
from enum import Enum
# from models import Account, Admin, Customer, Rider, Product, Order
from models import Account, Admin, Customer, Rider
from storage import load_data, save_data

class OrderStatus(Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DELIVERED = "DELIVERED"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("Welcome to QuickCart Console MVP")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                if user.role == 'ADMIN':
                    admin_menu(user)
                elif user.role == 'CUSTOMER':
                    customer_menu(user)
                elif user.role == 'RIDER':
                    rider_menu(user)
        elif choice == '3':
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

def register():
    clear_screen()
    print("Register New Account")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    role = input("Role (CUSTOMER/RIDER/ADMIN): ").strip().upper()
    if role not in ['CUSTOMER', 'RIDER', 'ADMIN']:
        print("Invalid role.")
        input("Press Enter to continue...")
        return
    users = load_data('users')
    if any(u['username'] == username for u in users):
        print("Username already exists.")
        input("Press Enter to continue...")
        return
    new_id = max((u['id'] for u in users), default=0) + 1
    new_user = {'id': new_id, 'username': username, 'password': password, 'role': role}
    users.append(new_user)
    save_data('users', users)
    print("Registration successful.")
    input("Press Enter to continue...")

def login():
    clear_screen()
    print("Login")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    users = load_data('users')
    for u in users:
        if u['username'] == username and u['password'] == password:
            if u['role'] == 'ADMIN':
                return Admin(u['id'], username, password)
            elif u['role'] == 'CUSTOMER':
                return Customer(u['id'], username, password)
            elif u['role'] == 'RIDER':
                return Rider(u['id'], username, password)
    print("Invalid credentials.")
    input("Press Enter to continue...")
    return None

def admin_menu(admin):
    while True:
        clear_screen()
        print(f"Admin Menu - {admin.username}")
        print("1. Add Product")
        print("2. Restock Product")
        print("3. View All Orders")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            admin.add_product()
        elif choice == '2':
            admin.restock_product()
        elif choice == '3':
            admin.view_all_orders()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        input("Press Enter to continue...")

def customer_menu(customer):
    while True:
        clear_screen()
        print(f"Customer Menu - {customer.username}")
        print("1. Browse Products")
        print("2. Place Order")
        print("3. View Order History")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            customer.browse_products()
        elif choice == '2':
            customer.place_order()
        elif choice == '3':
            customer.view_order_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        input("Press Enter to continue...")

def rider_menu(rider):
    while True:
        clear_screen()
        print(f"Rider Menu - {rider.username}")
        print("1. View Pending Orders")
        print("2. Accept Order")
        print("3. Update Order Status")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            rider.view_pending_orders()
        elif choice == '2':
            rider.accept_order()
        elif choice == '3':
            rider.update_order_status()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    # Initialize data files if not exist
    if not os.path.exists('users.json'):
        save_data('users', [{'id': 1, 'username': 'admin', 'password': 'admin', 'role': 'ADMIN'}])  # Default admin
    if not os.path.exists('products.json'):
        save_data('products', [])
    if not os.path.exists('orders.json'):
        save_data('orders', [])
    main_menu()