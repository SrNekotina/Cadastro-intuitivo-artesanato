import datetime

artisans = []
products = []
sales = []

def main_menu():
    while True:
        print("\n===== ARTISAN GROUP MANAGEMENT SYSTEM =====")
        print("1. Register Artisan")
        print("2. Register Product")
        print("3. Record Sale")
        print("4. List Artisans")
        print("5. List Products")
        print("6. Sales History")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_artisan()
        elif choice == "2":
            register_product()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            list_artisans()
        elif choice == "5":
            list_products()
        elif choice == "6":
            sales_history()
        elif choice == "0":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option!")

def register_artisan():
    name = input("Artisan's name: ")
    contact = input("Contact: ")
    artisan = {"name": name, "contact": contact}
    artisans.append(artisan)
    print("✅ Artisan successfully registered!")

def register_product():
    name = input("Product name: ")
    price = float(input("Product price (R$): "))
    stock = int(input("Stock quantity: "))
    product = {"name": name, "price": price, "stock": stock}
    products.append(product)
    print("✅ Product successfully registered!")

def record_sale():
    list_products()
    product_idx = int(input("Enter the number of the sold product: ")) - 1
    quantity = int(input("Quantity sold: "))
    
    if product_idx < 0 or product_idx >= len(products):
        print("Invalid product.")
        return

    product = products[product_idx]
    if product["stock"] < quantity:
        print("❌ Not enough stock!")
        return

    product["stock"] -= quantity
    total = quantity * product["price"]
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    sales.append({"product": product["name"], "quantity": quantity, "total": total, "date": date})
    print(f"✅ Sale recorded! Total: R$ {total:.2f}")

def list_artisans():
    print("\n===== REGISTERED ARTISANS =====")
    for idx, a in enumerate(artisans, 1):
        print(f"{idx}. {a['name']} - Contact: {a['contact']}")

def list_products():
    print("\n===== REGISTERED PRODUCTS =====")
    for idx, p in enumerate(products, 1):
        print(f"{idx}. {p['name']} - Price: R$ {p['price']:.2f} - Stock: {p['stock']}")

def sales_history():
    print("\n===== SALES HISTORY =====")
    if not sales:
        print("No sales recorded yet.")
    for s in sales:
        print(f"{s['date']} - {s['product']} x{s['quantity']} - Total: R$ {s['total']:.2f}")

# Run the system
main_menu()
