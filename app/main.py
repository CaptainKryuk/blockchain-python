from flask import Flask
from flask import render_template
from flask import request
from app import block

app = Flask(__name__)


@app.route('/', method=['POST', 'GET'])
def index():

    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        block.write_block(name=lender, amount=amount, to_whom=borrower)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)