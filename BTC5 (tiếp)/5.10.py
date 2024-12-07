import sqlite3

# Kết nối đến cơ sở dữ liệu 
conn = sqlite3.connect('product.db')
cursor = conn.cursor()
# Tạo bảng 'product' 
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')
conn.commit()

#HIỂN THỊ DANH SÁCH SẢN PHẨM
def display_products():
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    if products:
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Amount':<10}")
        print("-" * 50)
        for product in products:
            print(f"{product[0]:<5} {product[1]:<20} {product[2]:<10} {product[3]:<10}")
    else:
        print("No products found.")

#THÊM SẢN PHẨM VÀO BẢNG
def add_product(name, price, amount):
    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    print(f"Product '{name}' added successfully.")

#TÌM KIẾM SẢN PHẨM THEO TÊN
def search_product_by_name(name):
    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    products = cursor.fetchall()
    if products:
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Amount':<10}")
        print("-" * 50)
        for product in products:
            print(f"{product[0]:<5} {product[1]:<20} {product[2]:<10} {product[3]:<10}")
    else:
        print(f"No product found with name '{name}'.")

#CẬP NHẬT ĐƠN GIÁ VÀ SỐ LƯỢNG CỦA MỘT SẢN PHẨM THEO ID
def update_product(id, price, amount):
    cursor.execute('UPDATE product SET Price = ?, Amount = ? WHERE ID = ?', (price, amount, id))
    conn.commit()
    print(f"Product with ID {id} updated successfully.")

#XÓA MỘT SẢN PHẨM THEO ID
def delete_product(id):
    cursor.execute('DELETE FROM product WHERE ID = ?', (id,))
    conn.commit()
    print(f"Product with ID {id} deleted successfully.")
          
                
                ###TẠO GIAO DIỆN NGƯỜI DÙNG###
def show_menu():
    print("\n--- Product Management ---")
    print("1. Display products")
    print("2. Add product")
    print("3. Search product by name")
    print("4. Update product price and amount")
    print("5. Delete product by ID")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            amount = int(input("Enter product amount: "))
            add_product(name, price, amount)
        elif choice == '3':
            name = input("Enter product name to search: ")
            search_product_by_name(name)
        elif choice == '4':
            id = int(input("Enter product ID to update: "))
            price = float(input("Enter new price: "))
            amount = int(input("Enter new amount: "))
            update_product(id, price, amount)
        elif choice == '5':
            id = int(input("Enter product ID to delete: "))
            delete_product(id)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

#CHẠY CHƯƠNG TRÌNH  
if __name__ == "__main__":
    main()

    
    

