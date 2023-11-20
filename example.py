import requests


def get_flight_time_limit(start_time: str, legs: str):
    """GET Request to username microservice."""
    url = "http://<YOUR PROJECT>.uw.r.appspot.com/flight_time_limit"
    url += f"?start_time={start_time}&flight_legs={legs}"
    print(url)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.ConnectionError as error:
        return error
    except requests.exceptions.HTTPError as error:
        return error
    return response.text


if __name__ == '__main__':
    print(get_flight_time_limit("1200", "2"))
    # expected result "11"
