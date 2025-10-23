import psycopg2
# connect to the postgress database
connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5432,
    dbname='myduka_db',
    password='Kevin254!'
)

# declare cursor to perfom database operations
curr=connect.cursor()

# fetch products 


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


products=fetch_data('products')
print(products)
stock=fetch_data('stock')
print(stock)
sales=fetch_data('sales')
print(sales)

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
    
new_sale=(2,5)
insert_sales(new_sale)
sales = fetch_data('sales')
print(sales)

# function to get profit per product 
def product_profit():
	query='Select p.name,p.id,sum((p.selling_price-p.buying_price)*s.quantity) as profit from sales as s inner join products as p on s.pid=p.id group by p.name,p.id;'
	curr.execute(query)
	profit=curr.fetchall()
	return profit

myprofits=product_profit()
print(f'my products profit {myprofits}')

# function to get sales per product 
def product_sale():
	query='Select p.name,p.id,sum(p.selling_price*s.quantity) as total_sales from sales as s inner join products as p on s.pid=p.id group by p.name,p.id;'
	curr.execute(query)
	sales=curr.fetchall()
	return sales
mysales=product_sale()

print(f'my products sales {mysales}')
