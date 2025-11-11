# import psycopg2
import sqlite3
# connect to the postgress database
# connect=psycopg2.connect(
#     host='localhost',
#     user='postgres',
#     port=5432,
#     dbname='myduka_db',
#     password='Kevin254!'
# )
connect = sqlite3.connect("mydatabase.db")
# declare cursor to perfom database operations
curr=connect.cursor()
# fetch products 

curr.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

curr.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    buying_price REAL NOT NULL,
    selling_price REAL NOT NULL
)
""")

curr.execute("""
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pid INTEGER NOT NULL,
    stock_quantity INTEGER NOT NULL,
    FOREIGN KEY (pid) REFERENCES products(id)
)
""")

curr.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pid INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (pid) REFERENCES products(id)
)
""")


# def fetch_products():
#     curr.execute('select * from products;')
#     prods = curr.fetchall()
#     return prods

# products=fetch_products()
# print(products)

# fetch sales

# def fetch_sales():
#     curr.execute('select * from sales;')
#     sales = curr.fetchall()
#     return sales
# sales = fetch_sales()
# print(sales )
# fetch stock

# def fetch_stock():
#     curr.execute('select * from stock;')
#     stock = curr.fetchall()
#     return stock

# stock1 = fetch_stock()
# print(stock1)

# fetch data in the database 
def fetch_data(table):
    query = f'select * from {table}'
    curr.execute(query)
    data=curr.fetchall()
    return data


# products=fetch_data('products')
# print(products)
# stock=fetch_data('stock')
# print(stock)
# sales=fetch_data('sales')
# print(sales)

# insert products 
# curr.execute("insert into products(name,buying_price,selling_price)values('Ginger',20,30);")
# connect.commit()

def insert_products(values):
    query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s);"
    curr.execute(query,values)
    connect.commit()

# new_product=('Avocados',50,70)
# insert_products(new_product)
# products = fetch_data('products')
# print(products)

# insert sales
def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    connect.commit()
    
# new_sale=(2,5)
# insert_sales(new_sale)
# sales = fetch_data('sales')
# print(sales)

# function to get profit per product 
def product_profit():
	query='Select p.name,sum((p.selling_price-p.buying_price)*s.quantity) as profit from sales as s inner join products as p on s.pid=p.id group by p.name;'
	curr.execute(query)
	profit=curr.fetchall()
	return profit

# myprofits=product_profit()
# print(f'my products profit {myprofits}')

# function to get sales per product 
def product_sale():
	query='Select p.name,p.id,sum(p.selling_price*s.quantity) as total_sales from sales as s inner join products as p on s.pid=p.id group by p.name,p.id;'
	curr.execute(query)
	sales=curr.fetchall()
	return sales

# mysales=product_sale()

# print(f'my products sales {mysales}')

# sales per day

def sales_day():
    query = 'Select date(s.created_at),sum(p.selling_price*s.quantity) as total_sales from sales as s inner join products as p on s.pid=p.id group by date(s.created_at);'
    curr.execute(query)
    data=curr.fetchall()
    return data

# profit per day


# def sales_day():
#     query = 'Select p.name,p.id,date(s.created_at),sum(p.selling_price*s.quantity) as total_sales from sales as s inner join products as p on s.pid=p.id group by p.name,p.id,date(s.created_at);'
#     curr.execute(query)
#     data = curr.fetchall()
#     return data 

# create a function that inserts users
# insert into users(columns)values() 

def insert_users(user_values):
    query='insert into users (full_name,email,password)values(%s,%s,%s);'
    curr.execute(query,user_values)
    connect.commit()

# check if user exist
def check_email(email):
    query='select * from users where email=%s'
    curr.execute(query,(email,))
    data=curr.fetchone()
    return data

# print(check_email('dan@mail.com'))