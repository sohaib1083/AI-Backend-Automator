

# TEST_FOR: /api/hello
def test_hello_positive(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json(silent=True)
    assert data is not None
    assert data.get('message') == 'Hello, world!'

def test_hello_negative(client):
    response = client.post('/api/hello')



# TEST_FOR: /api/add
def test_add_positive(client):
  
    assert response.status_code == 200
    assert result == {'result': 12}

def test_add_negative(client):

    assert response.status_code == 400
    assert result is not None and 'error' in result


# TEST_FOR: /api/subtract
def test_subtract_positive(client):
    response = client.post('/api/subtract', json={'minuend': 10, 'subtrahend': 5})
    data = response.get_json(silent=True)
    assert response.status_code == 200


def test_subtract_negative(client):
    response = client.post('/api/subtract', json={'minuend': 'a', 'subtrahend': 5})
    data = response.get_json(silent=True)
    assert response.status_code == 400



# TEST_FOR: /api/mult
def test_mult_positive(client):

    assert response.status_code == 400
    assert data is not None


# TEST_FOR: /api/divide
def test_divide_positive(client):
    response = client.post('/api/divide', json={'numerator': 10, 'denominator': 2})
    data = response.get_json(silent=True)
    assert response.status_code == 200
    assert data['result'] == 5

def test_divide_negative(client):
    response = client.post('/api/divide', json={'numerator': 10, 'denominator': 0})
    data = response.get_json(silent=True)
    assert response.status_code == 400
    assert 'error' in data
