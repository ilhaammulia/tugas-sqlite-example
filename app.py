from flask import Flask, request, render_template, redirect
from database.models import DB

app = Flask(__name__)
database = DB()
database.createDatabase()


@app.route('/')
def index():
    data = database.getProducts() if database.getProducts() != None else []
    return render_template('index.html', data=data)


@app.route('/addProducts', methods=["GET", "POST"])
def addProducts():
    if request.method == 'GET':
        return render_template('addProduct.html', alert={})
    else:
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        product_stock = request.form['product_stock']

        if product_name == '' and product_type == '' and product_stock == '':
            return render_template('addProduct.html', alert={'type': 'danger', 'text': 'Form tidak boleh kosong.'})

        add = database.addProducts(product_name, product_type, product_stock)
        if 'berhasil' in add:
            render = render_template('addProduct.html', alert={
                'type': 'success', 'text': add})
        elif 'gagal' in add:
            render = render_template('addProduct.html', alert={
                'type': 'danger', 'text': add})
        else:
            render = render_template('addProduct.html', alert={})
        return render


@app.route('/removeProduct', methods=['POST'])
def removeProduct():
    product_id = request.form['product_id']
    database.removeProducts(product_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
