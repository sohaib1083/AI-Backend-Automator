

# TEST_FOR: /api/hello
def test_hello_positive(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, world!"}

def test_hello_negative(client):
    response = client.post('/api/hello')
    assert response.status_code == 405


# TEST_FOR: /api/add
def test_add_positive(client):
    response = client.post('/api/add', json={'num1': 2, 'num2': 3})
    assert response.status_code == 200
    assert response.json == {'result': 5}

def test_add_negative(client):
    response = client.post('/api/add', json={'num1': 'a', 'num2': 3})
    assert response.status_code == 400


# TEST_FOR: /api/subtract
def test_subtract_positive(client):
    response = client.post('/api/subtract', json={'num1': 10, 'num2': 5})
    assert response.status_code == 200
    assert response.json == {'result': 5}

def test_subtract_negative(client):
    response = client.post('/api/subtract', json={'num1': 'ten', 'num2': 5})
    assert response.status_code == 400


# TEST_FOR: /api/mult
def test_mult_positive(client):
    response = client.post('/api/mult', json={'num1': 2, 'num2': 3})
    assert response.status_code == 200
    assert response.json == {'result': 6}

def test_mult_negative(client):
    response = client.post('/api/mult', json={'num1': 'a', 'num2': 3})
    assert response.status_code == 400
