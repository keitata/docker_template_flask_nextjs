import datetime

from flask import Flask
from flask_cors import CORS

from db import Sample, SessionMaker

app = Flask(__name__)
# TODO : CORS
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ping")
def ping():
    with SessionMaker() as session:
        session.add(Sample(date=f"ping + {datetime.datetime.now()}"))
        session.commit()
    return {"status": "OK"}


@app.route("/samples")
def samples():
    sample_data_lst = []
    with SessionMaker() as session:
        sample_data_lst = [d.date for d in session.query(Sample).all()]
    return {"samples": sample_data_lst}
