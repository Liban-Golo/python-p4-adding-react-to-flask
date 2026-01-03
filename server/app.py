from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from models import db, Message
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route("/messages", methods=["GET"])
def get_messages():
    messages = [m.to_dict() for m in Message.query.all()]
    return make_response(jsonify(messages), 200)


@app.route("/messages", methods=["POST"])
def create_message():
    data = request.get_json()
    new_message = Message(username=data.get("username"), body=data.get("body"))
    db.session.add(new_message)
    db.session.commit()
    return make_response(jsonify(new_message.to_dict()), 201)


@app.route("/messages/<int:id>", methods=["PATCH"])
def update_message(id):
    message = Message.query.get_or_404(id)
    data = request.get_json()
    if "body" in data:
        message.body = data["body"]
    db.session.commit()
    return make_response(jsonify(message.to_dict()), 200)


@app.route("/messages/<int:id>", methods=["DELETE"])
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return make_response("", 204)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
