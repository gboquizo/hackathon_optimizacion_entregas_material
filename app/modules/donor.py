"""Routes for donor."""
from app import csrf
from app.models import Donor, Product, StockDonor
from flask import Blueprint, request
from flask_login import login_required
from flask import jsonify

# Blueprint Configuration
donor_bp = Blueprint('donor', __name__)

@donor_bp.route('/api/v1/donor', methods=['GET'])
def get_donors():
    donors = [ donor.json() for donor in Donor.query.all() ]
    return jsonify({'donors': donors })

@donor_bp.route('/api/v1/donor/stock', methods=['GET'])
def get_stocks():
    stocks = [ stock.serialize for stock in StockDonor.query.all() ]
    return jsonify({'stocks': stocks })

@csrf.exempt
@donor_bp.route('/api/v1/donor/<id>/stock/', methods=['POST'])
def create_donor_stock(id):
    json = request.get_json(force=True)
    donor = Donor.query.filter_by(id=id).first()
    product = Product.query.filter_by(id=json['product_id']).first()
    if donor is None:
        return jsonify({'message': 'Donor does not exists'}), 404
    
    if product is None:
        return jsonify({'message': 'Product does not exits'}), 404

    stock = StockDonor.create(json['donor_id'], json['product_id'], json['quantity'])

    return jsonify({'stock': stock.serialize})

@donor_bp.route('/api/v1/donor/<id>/stock', methods=['GET'])
def get_donor_stock(id):
    donor_stock = [ stock.serialize for stock in StockDonor.query.filter_by(donor_id=id).all() ]
    return jsonify({'donor_stock': donor_stock })

@csrf.exempt
@donor_bp.route('/api/v1/donor/stock/<id>', methods=['PUT'])
def update_stock(id):
    stock = StockDonor.query.filter_by(id=id).first()
    json = request.get_json(force=True)
    stock.quantity = json['quantity']
    stock.update()
    return jsonify({'stock': stock.serialize })

@csrf.exempt
@donor_bp.route('/api/v1/donor/stock/<id>', methods=['DELETE'])
def delete_stock(id):
    stock = StockDonor.query.filter_by(id=id).first()
    if stock is None:
        return jsonify({'message': 'Stock does not exists'}), 404

    stock.delete()

    return jsonify({'stock': stock.serialize })