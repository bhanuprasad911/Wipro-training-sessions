from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated Database
db = {
    "restaurants": {},
    "dishes": {},
    "users": {},
    "orders": [],
    "feedback": [],
    "ratings": []
}

# --- 1. RESTAURANT MODULE ---

@app.route('/api/v1/restaurants', methods=['POST'])
def register_restaurant():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Bad Request"}), 400
    
    res_id = len(db["restaurants"]) + 1
    data['id'] = res_id
    data['status'] = 'pending'  # Requirement 9/10: Admin must approve
    data['enabled'] = True      # Requirement 3: Can be disabled
    db["restaurants"][res_id] = data
    return jsonify(data), 201

@app.route('/api/v1/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant_details(restaurant_id):
    if restaurant_id in db["restaurants"]:
        update_data = request.get_json()
        db["restaurants"][restaurant_id].update(update_data)
        return jsonify(db["restaurants"][restaurant_id]), 200
    return jsonify({"message": "Restaurant not found"}), 404

@app.route('/api/v1/restaurants/<int:restaurant_id>/disable', methods=['PUT'])
def disable_restaurant(restaurant_id):
    if restaurant_id in db["restaurants"]:
        db["restaurants"][restaurant_id]['enabled'] = False
        return jsonify({"message": "Restaurant disabled"}), 200
    return jsonify({"message": "Restaurant not found"}), 404

@app.route('/api/v1/restaurants/<int:res_id>', methods=['GET'])
def view_restaurant(res_id):
    res = db["restaurants"].get(res_id)
    return jsonify(res) if res else (jsonify({"error": "Not Found"}), 404)

# --- 2. DISH MODULE ---

@app.route('/api/v1/restaurants/<int:res_id>/dishes', methods=['POST'])
def add_dish(res_id):
    if res_id not in db["restaurants"]:
        return jsonify({"error": "Restaurant not found"}), 404
    data = request.get_json()
    dish_id = len(db["dishes"]) + 1
    data['id'] = dish_id
    data['restaurant_id'] = res_id
    data['enabled'] = True # Requirement 7: For Enable/Disable
    db["dishes"][dish_id] = data
    return jsonify(data), 201

@app.route('/api/v1/dishes/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    if dish_id in db["dishes"]:
        update_data = request.get_json()
        db["dishes"][dish_id].update(update_data)
        return jsonify(db["dishes"][dish_id]), 200
    return jsonify({"error": "Not Found"}), 404

@app.route('/api/v1/dishes/<int:dish_id>/status', methods=['PUT'])
def toggle_dish_status(dish_id):
    if dish_id in db["dishes"]:
        data = request.get_json()
        db["dishes"][dish_id]['enabled'] = data.get('enabled', True)
        return jsonify({"message": f"Dish status updated to {db['dishes'][dish_id]['enabled']}"}), 200
    return jsonify({"error": "Not Found"}), 404

@app.route('/api/v1/dishes/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    if dish_id in db["dishes"]:
        del db["dishes"][dish_id]
        return jsonify({"message": "Dish deleted"}), 200
    return jsonify({"error": "Not Found"}), 404

# --- 3. ADMIN MODULE ---

@app.route('/api/v1/admin/restaurants/<int:restaurant_id>/approve', methods=['PUT'])
def approve_restaurant(restaurant_id):
    if restaurant_id in db["restaurants"]:
        db["restaurants"][restaurant_id]['status'] = 'approved'
        return jsonify({"message": "Restaurant approved"}), 200
    return jsonify({"message": "Not Found"}), 404

@app.route('/api/v1/admin/feedback', methods=['GET'])
def view_feedback():
    return jsonify(db["feedback"]), 200

@app.route('/api/v1/admin/orders', methods=['GET'])
def view_all_orders():
    return jsonify(db["orders"]), 200

# --- 4. USER & SEARCH MODULE ---

@app.route('/api/v1/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = len(db["users"]) + 1
    db["users"][user_id] = data
    return jsonify({"id": user_id, "name": data['name']}), 201

@app.route('/api/v1/restaurants/search', methods=['GET'])
def search_restaurants():
    # Requirement 14: Search by name, location, etc.
    name = request.args.get('name', '').lower()
    location = request.args.get('location', '').lower()
    
    results = [
        res for res in db["restaurants"].values() 
        if name in res['name'].lower() and location in res['location'].lower()
    ]
    return jsonify(results), 200

@app.route('/api/v1/ratings', methods=['POST'])
def give_rating():
    data = request.get_json()
    db["ratings"].append(data)
    # Also add to feedback for Admin Requirement 11
    db["feedback"].append({"order_id": data['order_id'], "comment": data['comment']})
    return jsonify(data), 201

# --- 5. ORDER MODULE ---

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    order_id = len(db["orders"]) + 1
    data['id'] = order_id
    db["orders"].append(data)
    return jsonify(data), 201

@app.route('/api/v1/restaurants/<int:restaurant_id>/orders', methods=['GET'])
def get_restaurant_orders(restaurant_id):
    res_orders = [o for o in db["orders"] if o.get('restaurant_id') == restaurant_id]
    return jsonify(res_orders), 200

@app.route('/api/v1/users/<int:user_id>/orders', methods=['GET'])
def get_user_orders(user_id):
    user_orders = [o for o in db["orders"] if o.get('user_id') == user_id]
    return jsonify(user_orders), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)