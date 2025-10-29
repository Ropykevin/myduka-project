from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products

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
    return render_template('sales.html',sales=sales)

# stocks route 

@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    return render_template('stock.html',stock=stock)



app.run(debug=True)

