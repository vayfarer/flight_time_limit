# flight_time_limit
Flask server microservice to return pilot flight time limits depending on starting time and number of flight legs.

# How to use:
1) Deploy the project on Google App Engine. 
2) Then access the microservice by sending HTTP GET requests to the project at: <br>
`http://<GAE project domain name>/flight_time_limit?start_time=<time in 2400 format>&flight_legs=<number of flight legs between 1 and 4 inclusive> `<br>
For example:<br>
`http://YOUR_PROJECT_ADDRESS.appspot.com/flight_time_limit?start_time=1234&flight_legs=2`<br>
The query parameters `start_time` and `flight_legs` are the input parameters. 
You may open the url on your web browser, which will return the flight time limit in the body of a HTTP response.

A means of accessing the microservice in python is provided as follows: 

```
import requests


def get_flight_time_limit(start_time: str, legs: str):
    """GET Request to username microservice."""
    url = "http://<YOUR_PROJECT>.uw.r.appspot.com/flight_time_limit"
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
```

# UML Sequence Diagram
![UML diagram](https://github.com/vayfarer/flight_time_limit/blob/master/uml_seq.jpg)
