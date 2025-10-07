from enum import Enum
import json


from storage import load_data, save_data

class OrderStatus(Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DELIVERED = "DELIVERED"

class Account:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password  
        self.role = None  

class Admin(Account):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        self.role = 'ADMIN'

    def add_product(self):
        name = input("Product Name: ").strip()
        try:
            price = float(input("Price: ").strip())
            stock = int(input("Initial Stock: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        products = load_data('products')
        new_id = max((p['id'] for p in products), default=0) + 1
        products.append({'id': new_id, 'name': name, 'price': price, 'stock': stock})
        save_data('products', products)
        print("Product added.")

    def restock_product(self):
        try:
            product_id = int(input("Product ID: ").strip())
            additional_stock = int(input("Additional Stock: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        products = load_data('products')
        for p in products:
            if p['id'] == product_id:
                p['stock'] += additional_stock
                save_data('products', products)
                print("Product restocked.")
                return
        print("Product not found.")

    def view_all_orders(self):
        orders = load_data('orders')
        if not orders:
            print("No orders.")
            return
        for o in orders:
            print(f"Order ID: {o['id']}, Customer: {o['customer_id']}, Status: {o['status']}, Rider: {o.get('rider_id', 'None')}")

class Customer(Account):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        self.role = 'CUSTOMER'

    def browse_products(self):
        products = load_data('products')
        if not products:
            print("No products available.")
            return
        for p in products:
            print(f"ID: {p['id']}, Name: {p['name']}, Price: {p['price']}, Stock: {p['stock']}")

    def place_order(self):
        products = load_data('products')
        if not products:
            print("No products available.")
            return
        order_items = {}
        while True:
            try:
                product_id = int(input("Product ID (0 to finish): ").strip())
                if product_id == 0:
                    break
                quantity = int(input("Quantity: ").strip())
            except ValueError:
                print("Invalid input.")
                continue
            for p in products:
                if p['id'] == product_id:
                    if p['stock'] < quantity:
                        print("Insufficient stock.")
                        break
                    order_items[product_id] = quantity
                    p['stock'] -= quantity
                    break
            else:
                print("Product not found.")
        if not order_items:
            print("No items added.")
            return
        orders = load_data('orders')
        new_id = max((o['id'] for o in orders), default=0) + 1
        orders.append({'id': new_id, 'customer_id': self.id, 'items': order_items, 'status': OrderStatus.PENDING.value, 'rider_id': None})
        save_data('orders', orders)
        save_data('products', products)
        print("Order placed.")

    def view_order_history(self):
        orders = load_data('orders')
        my_orders = [o for o in orders if o['customer_id'] == self.id]
        if not my_orders:
            print("No orders.")
            return
        for o in my_orders:
            print(f"Order ID: {o['id']}, Status: {o['status']}, Rider: {o.get('rider_id', 'None')}")

class Rider(Account):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        self.role = 'RIDER'

    def view_pending_orders(self):
        orders = load_data('orders')
        pending = [o for o in orders if o['status'] == OrderStatus.PENDING.value]
        if not pending:
            print("No pending orders.")
            return
        for o in pending:
            print(f"Order ID: {o['id']}, Customer: {o['customer_id']}")

    def accept_order(self):
        try:
            order_id = int(input("Order ID to accept: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        orders = load_data('orders')
        for o in orders:
            if o['id'] == order_id and o['status'] == OrderStatus.PENDING.value:
                o['status'] = OrderStatus.ACCEPTED.value
                o['rider_id'] = self.id
                save_data('orders', orders)
                print("Order accepted.")
                return
        print("Order not found or not pending.")

    def update_order_status(self):
        try:
            order_id = int(input("Order ID: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        orders = load_data('orders')
        for o in orders:
            if o['id'] == order_id and o['rider_id'] == self.id and o['status'] == OrderStatus.ACCEPTED.value:
                o['status'] = OrderStatus.DELIVERED.value
                save_data('orders', orders)
                print("Status updated to DELIVERED.")
                return
        print("Order not found, not assigned to you, or not accepted.")