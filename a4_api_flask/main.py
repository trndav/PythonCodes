# Simple API in Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Bob Rock",
        "email": "bob@rock.com"
    }

    extra = request.args.get("extra") # http://127.0.0.1:5000/get-user/232?extra="Bum"
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user/", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify("Recieved data is: ", data), 201


if __name__ == "__main__":
    app.run(debug=True)