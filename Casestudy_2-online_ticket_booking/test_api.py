import requests

baseurl='http://127.0.0.1:5000'

def test_get_all_movies():
    response =requests.get(f"{baseurl}/movies")
    assert response.status_code == 200
    assert response.headers['content-type']=="application/json"
    

def test_get_movies_by_id():
    valid_response= requests.get(f"{baseurl}/movies/101")
    assert valid_response.status_code == 200
    valid_json = valid_response.json()
    assert 'id' in valid_json
    assert "movie_name" in valid_json
    assert "price" in valid_json
    
    invalid_response = requests.get(f"{baseurl}/movies/1000")
    assert invalid_response.status_code==404
    invalid_json = invalid_response.json()
    assert 'message'in invalid_json
    assert invalid_json['message']=="Movie not found"
    
    
def test_add_movie():
    new_movie={
        "movie_name":"TestMovie",
        "language":"telugu",
        "price":"200",
        "duration":"2h 54m"
    }
    invalid_movie={
        "movie_name":"invalid_movie"
    }
    empty_movie = {}
    valid_response=requests.post(f"{baseurl}/movies", json=new_movie)
    assert valid_response.status_code == 201
    valid_json = valid_response.json()
    assert 'id' in valid_json
    assert 'movie_name' in valid_json
    assert 'price' in valid_json
    
    invalid_response = requests.post(f"{baseurl}/movies", json=invalid_movie)
    assert invalid_response.status_code == 400
    invalid_json = invalid_response.json()
    assert 'message' in invalid_json
    assert invalid_json['message'] == "Missing required fields"
    
    empty_response = requests.post(f"{baseurl}/movies", json=empty_movie)
    assert empty_response.status_code == 400
    empty_json = empty_response.json()
    assert 'message' in empty_json
    assert empty_json['message'] == "Input data is empty"
    
    no_json_response = requests.post(f"{baseurl}/movies")
    no_json_json = no_json_response.json()
    assert no_json_response.status_code == 500
    assert 'message' in no_json_json
    assert no_json_json['message'] == "Error while adding movie, contact administrator"

def test_delete_movie():
    valid_response = requests.delete(f"{baseurl}/movies/107")
    assert valid_response.status_code==200
    valid_json = valid_response.json()
    assert "message" in valid_json
    assert valid_json['message']== "Movie deleted successfully"
    
    invalid_response = requests.delete(f"{baseurl}/movies/1")
    assert invalid_response.status_code == 404
    invalid_json=invalid_response.json()
    assert "message" in invalid_json
    assert invalid_json['message']== "Movie not found"

def test_book_ticket():
    valid_data ={
        "movie_id":101,
        "user_name":"Bhanu",
        "seats":2
    }
    invalid_data = {
        "movie_id":1001,
        "user_name":"Bhanu",
        "seats":2
    }
    missing_data={
        "user_name":"bhanu",
        "seats":2
    }
    empty_data = {}
    valid_response = requests.post(f"{baseurl}/book", json=valid_data)
    assert valid_response.status_code == 201
    valid_json = valid_response.json()
    assert 'message' in valid_json
    assert valid_json['message'] == "Ticket booked successfully"
    assert 'booking_id' in valid_json['data']
    assert 'movie_id' in valid_json['data']

        
    invalid_response = requests.post(f"{baseurl}/book", json=invalid_data)
    assert invalid_response.status_code == 404
    invalid_json = invalid_response.json()
    assert 'message' in invalid_json
    assert invalid_json['message'] == "Movie not found"
    
    
    missing_response = requests.post(f"{baseurl}/book", json=missing_data)
    assert missing_response.status_code == 400
    missing_json = missing_response.json()
    assert 'message' in missing_json
    assert missing_json['message'] == "movie_id, user_name and seats are required"
    
    
    empty_response = requests.post(f"{baseurl}/book", json=empty_data)
    assert empty_response.status_code == 400
    empty_json= empty_response.json()
    assert 'message' in empty_json
    assert empty_json['message'] == "Request body is missing"
    
    not_json_response = requests.post(f"{baseurl}/book")
    assert not_json_response.status_code == 500
    not_json = not_json_response.json()
    assert "message" in not_json
    assert not_json['message'] == "Error while booking ticket, please contact administrator"
    

def test_update_movie():
    movie_id = 101

    update_data = {
        "movie_name": "Interstellar Updated",
        "price": 300
    }

    valid_response = requests.put(f"{baseurl}/movies/{movie_id}", json=update_data)
    assert valid_response.status_code == 200
    valid_json = valid_response.json()
    assert valid_json["id"] == movie_id
    assert valid_json["movie_name"] == "Interstellar Updated"
    assert valid_json["price"] == 300
    assert "language" in valid_json
    assert "duration" in valid_json


    invalid_response = requests.put(f"{baseurl}/movies/9999", json=update_data)
    assert invalid_response.status_code == 404
    invalid_json = invalid_response.json()
    assert "message" in invalid_json
    assert invalid_json["message"] == "Movie not found"


    partial_update = {"language": "Hindi"}
    partial_response = requests.put(f"{baseurl}/movies/{movie_id}", json=partial_update)
    assert partial_response.status_code == 200
    partial_json = partial_response.json()
    assert partial_json["language"] == "Hindi"


    empty_response = requests.put(f"{baseurl}/movies/{movie_id}", json={})
    assert empty_response.status_code == 200
    

    no_json_response = requests.put(f"{baseurl}/movies/{movie_id}")
    assert no_json_response.status_code == 500
    no_json= no_json_response.json()
    assert 'message' in no_json
    assert no_json['message'] == "Error while updating movie, please contact administrator"