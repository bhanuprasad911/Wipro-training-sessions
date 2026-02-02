from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load data
with open('data.json', 'r') as data:
    movies_data = json.load(data)
with open('bookingdata.json', 'r') as f:
    bookings_data = json.load(f)


# Home Route
@app.route('/', methods=["GET"])
def home():
    return "Movie tickets server is live", 200


# Get All Movies
@app.route('/movies', methods=["GET"])
def get_movies():
    try:
        if len(movies_data) == 0:
            return jsonify({"message": "No movies available"}), 200
        return jsonify(movies_data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal server error"}), 500


# Add Movie
@app.route('/movies', methods=["POST"])
def add_movie():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Required details not found"}), 400

        if not all(k in data for k in ("movie_name", "duration", "language", "price")):
            return jsonify({"message": "Missing required fields"}), 400

        new_movie = {
            "id": 100+len(movies_data) + 1,
            "movie_name": data["movie_name"],
            "duration": data["duration"],
            "language": data["language"],
            "price": data["price"]
        }

        movies_data.append(new_movie)
        return jsonify(new_movie), 201

    except Exception as e:
        print(e)
        return jsonify({"message": "Error while adding the movie"}), 500


# Get Movie By ID
@app.route("/movies/<int:id>", methods=["GET"])
def get_movie_by_id(id):
    try:
        for movie in movies_data:
            if movie["id"] == id:
                return jsonify(movie), 200
        return jsonify({"message": "Movie not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Error while fetching movie"}), 500


# Update Movie
@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie_details(id):
    try:
        data = request.get_json()
        update_movie = None

        for movie in movies_data:
            if movie["id"] == id:
                update_movie = movie
                break

        if update_movie is None:
            return jsonify({"message": "Movie not found"}), 404

        update_movie["movie_name"] = data.get("movie_name", update_movie["movie_name"])
        update_movie["language"]   = data.get("language", update_movie["language"])
        update_movie["duration"]   = data.get("duration", update_movie["duration"])
        update_movie["price"]      = data.get("price", update_movie["price"])

        return jsonify(update_movie), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "Error while updating movie"}), 500


# Delete Movie
@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    try:
        for movie in movies_data:
            if movie["id"] == id:
                movies_data.remove(movie)
                return jsonify({"message": "Movie deleted successfully"}), 200
        return jsonify({"message": "Movie not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Error while deleting movie"}), 500


@app.route('/book', methods=["POST"])
def book_ticket():
    try:
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({"message": "Request body is missing"}), 400

        movie_id = data.get("movie_id")
        user_name = data.get("user_name")
        seats = data.get("seats")

        if not movie_id or not user_name or not seats:
            return jsonify({"message": "movie_id, user_name and seats are required"}), 400

        # Check if movie exists
        movie = next((m for m in movies_data if m["id"] == movie_id), None)
        if movie is None:
            return jsonify({"message": "Movie not found"}), 404

        total_price = movie["price"] * seats

        new_booking = {
            "booking_id": len(bookings_data) + 1,
            "movie_id": movie["id"],
            "movie_name": movie["movie_name"],
            "user_name": user_name,
            "seats": seats,
            "total_price": total_price
        }

        bookings_data.append(new_booking)

        return jsonify({
            "message": "Ticket booked successfully",
            "data": new_booking
        }), 201

    except Exception as e:
        print(e)
        return jsonify({"message": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
