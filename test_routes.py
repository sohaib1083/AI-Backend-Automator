

# TEST_FOR: /api/hello
def test_hello_positive(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, world!"}

def test_hello_negative(client):
    response = client.post('/api/hello')
    assert response.status_code == 405  # Method Not Allowed
    assert 'message' not in response.json or response.json['message'] != "Hello, world!"


# TEST_FOR: /api/add
def test_add_positive(client):
    response = client.post('/api/add', json={'num1': 5, 'num2': 7})
    assert response.status_code == 200
    assert response.get_json()['result'] == 12

def test_add_negative(client):
    response = client.post('/api/add', json={'num1': 'a', 'num2': 7})
    assert response.status_code == 400
    assert 'error' in response.get_json()


# TEST_FOR: /api/subtract
def test_subtract_positive(client):
    response = client.post('/api/subtract', json={'minuend': 10, 'subtrahend': 5})
    assert response.status_code == 200
    assert response.json == {'result': 5}

def test_subtract_negative(client):
    response = client.post('/api/subtract', json={'minuend': 'ten', 'subtrahend': 5})
    assert response.status_code == 400
    assert 'error' in response.json


# TEST_FOR: /api/mult
def test_mult_positive(client):
    response = client.post('/api/mult', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.get_json() == {'result': 6}

def test_mult_negative(client):
    response = client.post('/api/mult', json={'a': 'x', 'b': 3})
    assert response.status_code == 400
    assert 'error' in response.get_json()
