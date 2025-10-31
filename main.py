from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,product_profit

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def prods():
    prods=fetch_data('products')
    return render_template('products.html',prods=prods)

# add products
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        pname = request.form['name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        
        new_product=(pname,bp,sp)
        insert_products(new_product)
        return redirect(url_for('prods'))
    return  redirect(url_for('prods'))
        


# Sales route 

@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    # fetch products to display on select
    products=fetch_data('products')
    return render_template('sales.html',sales=sales,products=products)

# make sale route

@app.route('/make_sales',methods=['GET','POST'])
def make_sale():
    if request.method=='POST':
        pid=request.form['pid']
        qty=request.form['qty']
        
        new_sale=(pid,qty)
        insert_sales(new_sale)
        return redirect(url_for('sales'))
    return redirect(url_for('sales')) 
# steps to make sale
# 1.modal with the form
# 2. > the  form should be able to display all the products on a select option
# 3.On the sales route fetch products to be displayed
# 4.add fetched products to render template function
# 5.loop the fetched products into the option element in the select element on sales.html
# 6.on value attribute pass the product id while btw the opening and the closing option tag have the product name
        
# stocks route 

@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    return render_template('stock.html',stock=stock)

# dashboard
@app.route('/dashboard')
def dashboard():
    profits=product_profit()
    # print(profits)
    product_names=[]
    product_profits=[]
    for i in profits:
        product_names.append(i[0])
        product_profits.append(float(i[1]))
    # print(product_names)
    # print(product_profits)
    return render_template('dashboard.html', product_names=product_names, product_profits=product_profits)

app.run(debug=True)

