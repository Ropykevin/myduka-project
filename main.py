from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    return render_template('products.html')

# Sales route 


@app.route('/sales')
def sales():
    return 'My sales'

# stocks route 

@app.route('/stock')
def stock():
    return 'My stock'

app.run()