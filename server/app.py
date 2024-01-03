#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    mbkeries = [bk.to_dict() for bk in Bakery.query.all()];
    #mdict = dict(mbkeries);
    return mbkeries;

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    return Bakery.query.filter_by(id=id).first().to_dict();

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    mgds = [mg.to_dict() for mg in BakedGood.query.order_by(BakedGood.price.desc()).all()];
    return mgds;

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return BakedGood.query.order_by(BakedGood.price.desc()).first().to_dict();
    #return baked_goods_by_price()[0];#alternative acceptable answer

if __name__ == '__main__':
    app.run(port=5555, debug=True)
