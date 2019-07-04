from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate

import pymysql
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)


# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Pangolin2208@localhost:8537/fin_test_1'
app.config.from_object(Config)

@app.route('/')
def index():
    finance = Main.query.all()
    return render_template('index.html', finance=finance)


class Main(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tora_red = db.Column(db.String(120))
    direction = db.Column(db.String(120))
    sale = db.Column(db.String(120))
    buyer = db.Column(db.String(120))
    status_of_request=db.Column(db.String(120))
    blank_option_1 = db.Column(db.String(120))
    customer_name = db.Column(db.String(120))
    customer_accept_invoice_status = db.Column(db.String(120))
    customer_order_number = db.Column(db.String(120))
    customer_order_date = db.Column(db.DateTime)
    customer_order_monnth = db.Column(db.Integer)
    loading_place = db.Column(db.String(120))
    loading_date = db.Column(db.DateTime)
    cargo_character = db.Column(db.String(120))
    unloading_place = db.Column(db.String(120))
    unloading_date = db.Column(db.DateTime)
    supplier_name = db.Column(db.String(120))
    s_invoice_number = db.Column(db.String(120))
    ttn_cmr_available = db.Column(db.String(120))
    s_inv_date = db.Column(db.DateTime)
    s_inv_amount = db.Column(db.Integer)
    s_inv_vat = db.Column(db.Integer)
    s_inv_currency = db.Column(db.String(120))
    s_prepaid_amount = db.Column(db.Integer)
    s_prepaid_data = db.Column(db.DateTime)
    cost_with_vat = db.Column(db.Integer)
    cost_pochta = db.Column(db.Integer)
    cost_final = db.Column(db.Integer)
    cost_we_still_need_pay = db.Column(db.Integer)

    s_inv_status_payment = db.Column(db.String(120))
    s_inv_credit_terms = db.Column(db.Integer)
    s_credit_terms_scan_org = db.Column(db.String(120))
    s_inv_pay_intill_data = db.Column(db.DateTime)
    s_inv_status = db.Column(db.String(120)) # ЗНАЧ!!!
    blank_option_2 = db.Column(db.String(120))

    s_inv_act_date_payment = db.Column(db.DateTime)
    s_invoice_transit_name = db.Column(db.String(120))
    c_inv_number = db.Column(db.String(120))
    c_invoice_date = db.Column(db.DateTime)
    c_inv_amount = db.Column(db.String(120))
    c_inv_currency = db.Column(db.String(120))
    c_invfacture_number = db.Column(db.String(120))
    c_invfacture_data = db.Column(db.DateTime)
    c_inv_issue = db.Column(db.String(120))#42
    c_ems_tracking = db.Column(db.String(120))
    c_inv_post_send_data = db.Column(db.DateTime)
    c_inv_plan_pay = db.Column(db.DateTime)
    c_inv_week_plan_pay = db.Column(db.Integer)
    c_inv_status_payment = db.Column(db.String(120))
    c_inv_act_pay_date = db.Column(db.DateTime)
    profit = db.Column(db.Integer)
    month_number = db.Column(db.Integer)
    comments = db.Column(db.Text)
    s_inv_put_reestr = db.Column(db.Integer)
    s_np_ati = db.Column(db.String(120))
    s_inv_part_payment_16wk = db.Column(db.Integer)
    s_inv_part_pay_issue = db.Column(db.String(120))

    s_inv_part_payment_17wk = db.Column(db.Integer)
    s_inv_part_payment_18wk_2019= db.Column(db.Integer)
    s_inv_part_payment_20wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_21wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_22wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_23wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_24wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_25wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_26wk_2019 = db.Column(db.Integer)
    s_inv_part_payment_27wk_2019= db.Column(db.Integer)
    s_inv_part_payment_28wk_2019= db.Column(db.Integer)
    blank_option_3 = db.Column(db.String(120))
    s_inv_part_payment_29wk_2019 = db.Column(db.Integer)
    blank_option_4 = db.Column(db.String(120))
    s_inv_part_march_2019 = db.Column(db.Integer)
    blank_option_5 = db.Column(db.String(120))
    blank_option_6 = db.Column(db.String(120))

    posts = db.relationship('Post', backref='fin')
    user = db.relationship('User', backref='user')




#exi
#
#
#

class Post(db.Model):

    __tablename__='post'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Text)
    fin_id = db.Column(db.Integer, db.ForeignKey('main.id'))


class User(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    fin_id = db.Column(db.Integer, db.ForeignKey('main.id'))

    def __repr__(self):
        return '<User {}>'.format(self.name)


@app.shell_context_processor
def make_shell_context():
    return{
        'db':db,
        'User':User,
        'Post':Post,
        'Main':Main,
    }

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    print(name)
    if name:
        new = Main(customer_name=name)
        db.session.add(new)
        db.session.commit()
        return jsonify({'name': new.customer_name})
    return jsonify({'error':'Missing data'})
































































if __name__=='__main__':
    app.run(debug=True, port=1010)

