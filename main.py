from flask import Flask, render_template, request, redirect, url_for,flash,session
from dbservice import fetch_data, insert_products, insert_sales, product_profit, sales_day, insert_users, check_email,update_prod
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key='dfghkjhgfhhjgfgjhgf'

@app.route('/')
def home():
    return render_template('index.html')

# products route



@app.route('/products')
def prods():
    if 'email' in session:
        prods = fetch_data('products')
    else:
        flash('login to access this page ', 'danger')
        return redirect(url_for('login'))
    return render_template('products.html', prods=prods)

# add products


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        pname = request.form['name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        new_product = (pname, bp, sp)
        insert_products(new_product)
        flash('product added','success')
        return redirect(url_for('prods'))
    return redirect(url_for('prods'))

# route to update products
@app.route('/update_product',methods=['GET','POST'])
def update_product():
    if request.method=='POST':
        id=request.form['id']
        pname = request.form['name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        update_prod(pname,bp,sp,id)
        flash('product updated')
        return redirect(url_for('prods'))
    return redirect(url_for('prods'))

# Sales route

@app.route('/sales')
def sales():
    if 'email' in session:
        sales = fetch_data('sales')
        # fetch products to display on select
        products = fetch_data('products')
    else:
        flash('login to access this page ', 'danger')
        return redirect(url_for('login'))
    return render_template('sales.html', sales=sales, products=products)

# make sale route


@app.route('/make_sales', methods=['GET', 'POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        qty = request.form['qty']

        new_sale = (pid, qty)
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
    stock = fetch_data('stock')
    return render_template('stock.html', stock=stock)

# dashboard


@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        profits = product_profit()
        # print(profits)
        product_names = []
        product_profits = []
        for i in profits:
            product_names.append(i[0])
            product_profits.append(float(i[1]))
        # print(product_names)
        # print(product_profits)

        psales = sales_day()
        # print(psales)
        dates = []
        dsales = []
        for i in psales:
            dates.append(str(i[0]))
            dsales.append(float(i[1]))
    else:
        flash('login to access this page','danger')
        return redirect(url_for('login'))

    return render_template('dashboard.html', product_names=product_names, product_profits=product_profits, dates=dates, dsales=dsales)


# register

@app.route('/register', methods=['GET', 'POST'])
def register():
    # check the method
    if request.method == 'POST':
        # get form data
        fname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        # hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = (fname, email, hashed_password)
        check=check_email(email)
        if check==None:
            insert_users(new_user)
            flash('account created successfully you canow login','succes')
            return redirect (url_for('login'))
        else:
            flash('Email already exist Login or use a different email','danger')

            return redirect(url_for('register'))
        
    return render_template('register.html')

# login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        
        check=check_email(email)
        if check==None:
            flash('account not found register')
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(check[-1],password):
            # if password==check[3]:
                session['email']=email
                flash('login successfully' ,'success')
                return redirect(url_for('dashboard'))
            else:
                # flash('incorrect password or email try again','error')
                flash('Invalid password provided', 'danger')
                return redirect (url_for ('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email')
    flash('Youve been logged out', 'success')
    return redirect(url_for('login'))

# id,name,email,password
app.run(debug=True)
