from flask import Flask,render_template
from database import fetch_data

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    return render_template('products.html',prods=prods)


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

app.run()

