from flask import jsonify, Blueprint, request

from data.datastore import orders, ratings

order_bp=Blueprint("orders", __name__)
@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.get_json()
    order={
        "id":len(orders)+1,
        "user_id":data["user_id"],
        "restaurant_id":data["restaurant_id"],
        "dishes":data["dishes"],
        "status":"Placed"
    }
    orders.append(order)
    return jsonify(order), 201
@order_bp.route("/api/v1/ratings", methods=["POST"])
def add_rating():
    data = request.get_json()
    rating={
        "order_id":data["order_id"],
        "rating":data["rating"],
        "comment":data.get("comment")
    }
    ratings.append(rating)
    return jsonify(rating), 201
@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def get_orders_by_restaurant_id(rid):
    result=[order for order in orders if order["restaurant_id"]==rid]
    return jsonify(result), 200
@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def get_orders_by_user(uid):
    result = [order for order in orders if order["user_id"] == uid]
    return jsonify(result), 200