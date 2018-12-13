import json
import requests


def getRequest(term, location):
    terms = "term=" + term
    locations = "location=" + location
    url = "https://api.yelp.com/v3/businesses/search?" + terms + "&" + locations
    api_key = "U8Y3ZTZht443oRyRcr5k6kwXhAJiVENziO1weyRZjUPuSzrgAcovrszf5hXtdTRY303DrfJtydbzmcYPjxriM_jJBlNIIZrcDIDQx0LDS2OP0GOmN7mzBo2w2S4JXHYx"
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    url_params = {}
    response = requests.request('GET', url, headers=headers, params=url_params)

    json_obj = json.loads(response.content.decode("utf-8"))

    results = json_obj.get("businesses")

    delkaPole = len(results)

    novePole = []

    for i in results:
        objekt = {}
        objekt["id"] = i.get("id")
        objekt["name"] = i.get("name")
        objekt["phone"] = i.get("phone")
        objekt["rating"] = i.get("rating")
        objekt["url"] = i.get("url")
        objekt["location"] = i.get("location")
        novePole.append(objekt)

    return results


if __name__ == '__main__':  # Main method
    terms = "gluten-free"
    locations = "Nove Mesto, Praha"
    print(getRequest(terms, locations))
