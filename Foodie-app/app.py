from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated Database
db = {
    "restaurants": {},
    "dishes": {},
    "users": {},
    "orders": [],
    "feedback": []
}

# --- RESTAURANT MODULE ---
@app.route('/api/v1/restaurants', methods=['POST'])
def register_restaurant():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Bad Request"}), 400
    
    res_id = len(db["restaurants"]) + 1
    # Ensure data is treated as a dict to support item assignment
    data['id'] = res_id
    data['status'] = 'pending'
    db["restaurants"][res_id] = data
    return jsonify(data), 201

@app.route('/api/v1/restaurants/<int:res_id>', methods=['GET'])
def view_restaurant(res_id):
    res = db["restaurants"].get(res_id)
    return jsonify(res) if res else (jsonify({"error": "Not Found"}), 404)

# --- DISH MODULE ---
@app.route('/api/v1/restaurants/<int:res_id>/dishes', methods=['POST'])
def add_dish(res_id):
    if res_id not in db["restaurants"]:
        return jsonify({"error": "Restaurant not found"}), 404
    data = request.get_json()
    dish_id = len(db["dishes"]) + 1
    data['id'] = dish_id
    data['restaurant_id'] = res_id
    db["dishes"][dish_id] = data
    return jsonify(data), 201

@app.route('/api/v1/dishes/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    if dish_id in db["dishes"]:
        del db["dishes"][dish_id]
        return jsonify({"message": "Dish deleted"}), 200
    return jsonify({"error": "Not Found"}), 404

# --- USER & ORDER MODULE ---
@app.route('/api/v1/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = len(db["users"]) + 1
    db["users"][user_id] = data
    return jsonify({"id": user_id, "name": data['name']}), 201

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    db["orders"].append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)