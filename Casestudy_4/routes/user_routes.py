from flask import jsonify, request, Blueprint

from data.datastore import users, feedbacks

user_bp = Blueprint("user", __name__)
@user_bp.route("/api/v1/user/register", methods=["POST"])
def user_register():
    data = request.get_json()
    for user in users:
        if user["email"] == data["email"]:
            return jsonify({"error": "Email already registered"}), 409
    user={
        "id":len(users)+1,
        "name":data["name"],
        "email":data["email"],
        "password":data["password"],
    }
    users.append(user)
    return jsonify(user), 201
@user_bp.route("/api/v1/user/feedback", methods=["POST"])
def add_feedback():
    data = request.get_json()

    feedback = {
        "id": len(feedbacks) + 1,
        "user_id": data["user_id"],
        "order_id": data["order_id"],
        "rating": data["rating"],
        "comment": data["comment"]
    }

    feedbacks.append(feedback)
    return jsonify(feedback), 201