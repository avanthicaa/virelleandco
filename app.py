from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
app.secret_key = 'change-this-secret'

DATA_FOLDER = 'data'

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)


def load_data(filename):
    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump([], f)

    with open(path, 'r') as f:
        return json.load(f)


def save_data(filename, data):
    path = os.path.join(DATA_FOLDER, filename)

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    products = load_data('products.json')
    return render_template('products.html', products=products)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = load_data('products.json')

    product = next((p for p in products if p['id'] == product_id), None)

    if not product:
        return redirect('/products')

    return render_template('product-details.html', product=product)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        users = load_data('users.json')

        users.append({
            'name': name,
            'email': email,
            'password': password
        })

        save_data('users.json', users)

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = load_data('users.json')

        user = next(
            (
                u for u in users
                if u['email'] == email and u['password'] == password
            ),
            None
        )

        if user:
            return redirect('/products')

    return render_template('login.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        address = request.form['address']
        payment_method = request.form['payment_method']
        total = request.form['total']

        orders = load_data('orders.json')

        orders.append({
            'customer_name': customer_name,
            'address': address,
            'payment_method': payment_method,
            'total': total
        })

        save_data('orders.json', orders)

        return redirect('/')

    return render_template('checkout.html')

@app.route('/how-to-use')
def how_to_use():
    return render_template('how-to-use.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/location')
def location():
    return render_template('location.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)