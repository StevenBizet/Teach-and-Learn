def test_root_path():
    a = 1
    b = 0
    assert a == b

def test_root_path2():
    a = 1
    b = 1
    assert a == b

#def test_root_path3():
#    response = client.get('/', data=None, headers=None)
    
# On veut tester qu'on peut bien cliquer sur Accueil:

def test_button_ok():
    reponse = client.get('/', data=None

def test_app(client):
    assert client.get(url_for('/page_accueil.html')).status_code == 200

