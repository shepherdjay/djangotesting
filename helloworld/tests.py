from django.urls import resolve

from helloworld.views import home_page


# Create your tests here.
def test_root_url_resolves_to_home_page_view():
    found = resolve('/')
    assert found.func == home_page

def test_home_page_returns_correct_html(client):
    response = client.get('/')
    print(response.content)
