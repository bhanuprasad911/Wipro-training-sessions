from flask import Flask, request, jsonify   
app = Flask(__name__)
app.json.sort_keys = False
users =[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice.j@example.com",
    "role": "Admin",
    "active": True
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob.smith@example.com",
    "role": "User",
    "active": True
  },
  {
    "id": 3,
    "name": "Charlie Davis",
    "email": "charlie.d@example.com",
    "role": "User",
    "active": False
  },
  {
    "id": 4,
    "name": "Diana Prince",
    "email": "diana.p@example.com",
    "role": "Moderator",
    "active": True
  },
  {
    "id": 5,
    "name": "Ethan Hunt",
    "email": "ethan.h@example.com",
    "role": "User",
    "active": True
  },
  {
    "id": 6,
    "name": "Fiona Gallagher",
    "email": "fiona.g@example.com",
    "role": "User",
    "active": True
  },
  {
    "id": 7,
    "name": "George Miller",
    "email": "george.m@example.com",
    "role": "Admin",
    "active": False
  },
  {
    "id": 8,
    "name": "Hannah Abbott",
    "email": "hannah.a@example.com",
    "role": "User",
    "active": True
  },
  {
    "id": 9,
    "name": "Ian Malcolm",
    "email": "ian.m@example.com",
    "role": "Moderator",
    "active": True
  },
  {
    "id": 10,
    "name": "Julia Roberts",
    "email": "julia.r@example.com",
    "role": "User",
    "active": True
  }
]

@app.route("/")
def print1():
    return "Welcome to flask server"



@app.route("/users", methods=["GET", "POST"])
def sendUsers():
    if request.method == "GET":
        return jsonify(users)
    if request.method == "POST":
        payload = request.json
        new_entry={
            "id":len(users)+1,
            "name":payload.get("name"),
            "role":payload.get("role"),
            "email":payload.get("email"),
            "active":payload.get("active")
        }
        for i in users:
            if i['id']==new_entry['id']:
                return jsonify({"Message": f"User with id {new_entry['id']} already exists"}), 409
        users.append(new_entry)
        return jsonify({
            "Message":"User added successfully",
            "New_user":new_entry
        }), 201
@app.route('/users/<int:user_id>', methods = ["GET"])
def getUserById(user_id):
    for i in users:
        if i['id'] == user_id:
            return jsonify(i), 200

                 

    
    

if __name__ == "__main__":
    app.run(debug=True)