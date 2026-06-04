from flask import Flask, render_template, request, redirect, session, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secretkey"

DB = SQLAlchemy(app)

# ---------------- USER MODEL ----------------

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(100), unique=True, nullable=False)
    password = DB.Column(DB.String(200), nullable=False)

# ---------------- EXPENSE MODEL ----------------

class Expense(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    amount = DB.Column(DB.Float, nullable=False)
    category = DB.Column(DB.String(100), nullable=False)
    description = DB.Column(DB.String(200))
    date = DB.Column(DB.DateTime, default=datetime.utcnow)

    user_id = DB.Column(
        DB.Integer,
        DB.ForeignKey('user.id'),
        nullable=False
        )
class Budget(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    amount = DB.Column(DB.Float, nullable=False)   

# ---------------- HOME ----------------

@app.route('/')
def index():

    if 'user_id' not in session:
        return redirect('/login')

    expenses = Expense.query.filter_by(
        user_id=session['user_id']
    ).all()

    current_month = datetime.now().month
    current_year = datetime.now().year

    monthly_expenses = Expense.query.filter(
        DB.extract('month', Expense.date) == current_month,
        DB.extract('year', Expense.date) == current_year,
        Expense.user_id == session['user_id']
    ).all()

    monthly_total = sum(exp.amount for exp in monthly_expenses)

    category_data = {}

    for exp in monthly_expenses:
        category_data[exp.category] = (
            category_data.get(exp.category, 0)
            + exp.amount
        )

    highest_category = (
        max(category_data, key=category_data.get)
        if category_data else "None"
    )

    budget_record = Budget.query.first()

    if budget_record:
        budget = budget_record.amount
    else:
        budget = 0

    savings = budget - monthly_total

    return render_template(
        'index.html',
        expenses=expenses,
        monthly_total=monthly_total,
        budget=budget,
        savings=savings,
        highest_category=highest_category,
        category_data=category_data
    )

# ---------------- SIGNUP ----------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            password=hashed_password
        )

        DB.session.add(user)
        DB.session.commit()

        return redirect('/login')

    return render_template('signup.html')

# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session['user_id'] = user.id
            return redirect('/')

    return render_template('login.html')

# ---------------- LOGOUT ----------------

@app.route('/logout')
def logout():

    session.clear()
    return redirect('/login')

# ---------------- ADD EXPENSE ----------------

@app.route('/add', methods=['GET', 'POST'])
def add_expense():

    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':

        expense = Expense(
            amount=float(request.form['amount']),
            category=request.form['category'],
            description=request.form['description'],
            user_id=session['user_id']
        )

        DB.session.add(expense)
        DB.session.commit()

        return redirect('/')

    return render_template('add_expense.html')

# ---------------- DELETE EXPENSE ----------------

@app.route('/delete/<int:id>')
def delete_expense(id):

    expense = Expense.query.get_or_404(id)

    DB.session.delete(expense)
    DB.session.commit()

    return redirect('/')

# ---------------- SET BUDGET ----------------

@app.route('/set_budget', methods=['POST'])
def set_budget():

    budget = float(request.form['budget'])

    budget_record = Budget.query.first()

    if budget_record:
        budget_record.amount = budget

    else:
        budget_record = Budget(amount=budget)
        DB.session.add(budget_record)

    DB.session.commit()

    return redirect('/')
# ---------------- EXPORT ---------------
@app.route('/export')
def export():

    if 'user_id' not in session:
        return redirect('/login')

    expenses = Expense.query.filter_by(
        user_id=session['user_id']
    ).all()

    data = []

    for exp in expenses:

        data.append({
            'Amount': exp.amount,
            'Category': exp.category,
            'Description': exp.description,
            'Date': exp.date.strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(data)

    file_path = "expenses.xlsx"

    df.to_excel(file_path, index=False)

    return send_file(file_path, as_attachment=True)

# ---------------- MAIN ----------------

if __name__ == '__main__':

    with app.app_context():
        DB.create_all()

    app.run(debug=True)
