from http import HTTPStatus  


def test_root_deve_retornar_ok_e_ola_mundo(client):  

    response = client.get('/')  

    assert response.status_code == HTTPStatus.OK  
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_deve_retornar_html_ola_mundo(client):   

    response = client.get('/html')  

    assert response.status_code == HTTPStatus.OK  
    assert response.headers["content-type"].startswith("text/html")
    assert "<h1>Olá Mundo!</h1>" in response.text


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username':'alice',
            'email':'alice@email.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@email.com',
        'id': 1
    }