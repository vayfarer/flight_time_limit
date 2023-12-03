# Michael Chen
# CS 361 microservice for Ian Hudson

from flask import Flask, request
import datetime
from google.cloud import datastore

client = datastore.Client()

app = Flask(__name__)


class Log:
    def __init__(self):
        """Stores the last ten visit data."""

    def log_visit(self, flight_start_time, flight_legs):
        """Adds an item to q which includes most recent visits data. """
        time = datetime.datetime.now(tz=datetime.timezone.utc)

        text = ('request time:' + str(time) + '; start_time: ' +
                 str(flight_start_time) + '; flight_legs: ' + str(flight_legs))
        entity = datastore.Entity(key=client.key("visit"))
        entity.update({"text": text})

        client.put(entity)


    def html_list(self):
        """Returns an html list of the last 10 visits."""
        html_out = "<ol>"

        query = client.query(kind="visit")
        query.order = ["-text"]
        visits = query.fetch()
        n = 0
        for visit in visits:
            n += 1
            if n <= 10:
                html_out += ("<li>"+visit['text'] +"</li>")
            else:
                client.delete(visit.key)

        html_out += "</ol>"
        return html_out


visitor_log = Log()


@app.route('/')
def index():
    return ("/flight_time_limit?start_time=1234&flight_legs=1 for API. <br>"
            + "recent uses of service: <br>" + visitor_log.html_list())


@app.route('/flight_time_limit', methods=['GET'])
def flight_time_limit_get():
    """Receives a GET request with query parameters:
    'start_time': #### (int),
    'flight_legs': # (int)
    Returns flight_time_limit (int)."""
    try:
        start_time = int(request.args['start_time'])
        flight_legs = int(request.args['flight_legs'])
        visitor_log.log_visit(start_time, flight_legs)
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