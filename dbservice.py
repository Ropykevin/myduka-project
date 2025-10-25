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

# insert product

def insert_products(values):
    query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s);"
    curr.execute(query,values)
    conn.commit()


# insert sales 

def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    conn.commit()
    

# # insert stock




# write a function that gets proft per product

def product_profit():
    query='select p.name,p.id ,sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from products as p join sales as s on p.id=s.pid group by p.name,p.id;' 
    curr.execute(query)
    profit=curr.fetchall()
    return profit
    
# write a function that gets sales per product
def product_sales():
    query='select p.name,p.id ,sum(p.selling_price*s.quantity) as total_profit from products as p join sales as s on p.id=s.pid group by p.name,p.id;' 
    curr.execute(query)
    sales=curr.fetchall()
    return sales
    




