# Michael Chen
# CS 361 microservice for Ian Hudson

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return ("/flight_time_limit?start_time=1234&flight_legs=1 for API.")


@app.route('/flight_time_limit', methods=['GET'])
def flight_time_limit_get():
    """Receives a GET request with query parameters:
    'start_time': #### (int),
    'flight_legs': # (int)
    Returns flight_time_limit (int)."""
    try:
        start_time = int(request.args['start_time'])
        flight_legs = int(request.args['flight_legs'])
    except:
        return ('Error: invalid parameters. Proper use: /flight_time_limit?start_time=1234&flight_legs=1', 400)

    time_table = {659:{1:9, 2:9, 3:8, 4:8},
             1159:{1:10, 2:10, 3:9, 4:9},
             1659:{1:11, 2:11, 3:10, 4:10},
             2159:{1:10, 2:10, 3:9, 4:9},
             2359:{1:9, 2:9, 3:8, 4:8}}

    if start_time < 0 or flight_legs not in {1, 2, 3, 4} or start_time > 2359:
        return ('Error: invalid parameters. Time in domain >0 and <2359. Flight legs domain = [1,2,3,4]', 400)
    elif start_time <= 659:
        return (str(time_table[659][flight_legs]), 200)
    elif start_time <= 1159:
        return (str(time_table[1159][flight_legs]), 200)
    elif start_time <= 1659:
        return (str(time_table[1659][flight_legs]), 200)
    elif start_time <= 2159:
        return (str(time_table[2159][flight_legs]), 200)
    elif start_time <= 2359:
        return (str(time_table[2359][flight_legs]), 200)
    else:
        return ('Error: invalid parameters', 400)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)