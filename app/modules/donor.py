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

@donor_bp.route('/register', methods=["POST"])
def register():

    """
    # Register user
    call auth method
        register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate_on_submit():
        existing_user = User.query.filter_by(email=register_form.email.data).first()

        if existing_user is None:
            user = User(
                email=request.form.get('email'),
                password=request.form.get('password'),
                username=request.form.get('username')
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('manager.index'))

    flash('A user already exists with that email address')
    return redirect(url_for('auth.register'))
    """
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400

    # Register address
    # Validate and deserialize input
    try:
        address_data = AddressSchema(json_data)
    except ma.ValidationError as err:
        print(err.messages)
        return err.messages, 422

    address = Address(address_data)
    db.session.add(address)
    db.session.commit()
    id_address = AddressSchema().dump(Address.query.get(address.id))

    # register donor
    # Validate and deserialize input
    try:
        donor_data = DonorSchema(json_data)
        donor_data['address'] = id_address
    except ma.ValidationError as err:
        print(err.messages)
        return err.messages, 422

    donor = Donor(donor_data)
    db.session.add(donor)
    db.session.commit()
    id_donor = DonorSchema().dump(donor.query.get(donor.id))

    return {"message": "Donor user registered.", "id": id_donor}, 200
