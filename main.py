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
    return render_template('sales.html')

# stocks route 

@app.route('/stock')
def stock():
    return render_template('stock.html')

app.run()