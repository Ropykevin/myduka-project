import psycopg2

conn=psycopg2.connect(
    host='localhost',
    user='postgres',
    dbname='myduka_db',
    password='Kevin254!',
    port=5432
)

curr=conn.cursor()


# function to fetch products 
# def fetch_products():
#     curr.execute('select * from products;')
#     products=curr.fetchall()
#     return products

# products=fetch_products()
# print('My Products')
# print(products)

# function to fetch sales
# def fetch_sales():
#     curr.execute('select * from sales;')
#     sales=curr.fetchall()
#     return sales

# sales=fetch_sales()
# print('My sales')
# print(sales)

# # function to fetch stock

# def fetch_stock():
#     curr.execute('select * from stock;')
#     stock = curr.fetchall()
#     return stock

# stock=fetch_stock()
# print('My Stock')
# print(stock)


# fetch data

def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data=curr.fetchall()
    return data

products=fetch_data('products')
print(products)
sales=fetch_data('sales')
print(sales)
stock=fetch_data('stock')
print(stock)

# insert product

def insert_products(values):
    query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s);"
    curr.execute(query,values)
    conn.commit()
new_product = ('garlic', 150, 170)
# insert_products(new_product)
products = fetch_data('products')
print(products)

# insert sales 

def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    conn.commit()
    
new_sale=(5,10)
insert_sales(new_sale)
sales=fetch_data('sales')
print(sales)

# insert stock










