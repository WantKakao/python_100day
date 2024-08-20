from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import func

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=True)
    location: Mapped[str] = mapped_column(String(250), nullable=True)
    seats: Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=True)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


# with app.app_context():
#     db.create_all()


def to_dict(self):
    # Method 1.
    dictionary = {}
    # Loop through each column in the data record
    for column in self.__table__.columns:
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary

    # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # Method 1
    # cafes = db.session.query(Cafe).all()
    # random_cafe = random.choice(cafes)

    # Method 2
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(cafe=to_dict(random_cafe))


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    # Method 1
    cafes_list = [to_dict(cafe) for cafe in all_cafes]
    return jsonify(cafes=cafes_list)

    # Method 2 With list comprehension
    # return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])


@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url") or '',
        location=request.form.get("loc") or '',
        has_sockets=request.form.get("sockets") == 'true' if request.form.get("sockets") is not None else False,
        has_toilet=request.form.get("toilet") == 'true' if request.form.get("toilet") is not None else False,
        has_wifi=request.form.get("wifi") == 'true' if request.form.get("wifi") is not None else False,
        can_take_calls=request.form.get("calls") == 'true' if request.form.get("calls") is not None else False,
        seats=request.form.get("seats") or None,
        coffee_price=request.form.get("coffee_price") or None,
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def change_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    if new_price is None:
        return jsonify({'error': 'No coffee price provided'}), 404

    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def cafe_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify({'error': "Sorry, that's not allowed. Make sure you have correct api_key."}), 403

    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify({'success': 'Successfully deleted.'})


if __name__ == '__main__':
    app.run(debug=True)
