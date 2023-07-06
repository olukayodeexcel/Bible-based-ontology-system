from requests import get;

test_endpoint = "http://127.0.0.1:8000/";
def make_test_request():
    res = get(test_endpoint);
    print(res);
    print(res.json());


search_endpoint = "http://127.0.0.1:8000/semantic/web/biblical-ontology/real-life-scenario/search/";
def make_search_request(search_term: str):
    res = get(search_endpoint + search_term);
    print(res);
    data = res.json();
    print("API_RESPONSE ", data);
    return data;


