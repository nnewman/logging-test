import logging
from flask import Flask, render_template, jsonify
from raven.contrib.flask import Sentry

import settings

app = Flask(__name__)
sentry = Sentry(app,
                dsn=settings.SENTRY_DSN,
                logging=True,
                level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/warning')
def trigger_warning():
    app.logger.warning("Testing warning trigger")
    return jsonify(**{'message': 'warning'}), 200

@app.route('/error')
def trigger_error():
    app.logger.error("Testing error trigger")
    return jsonify(**{'message': 'error'}), 404

@app.route('/exception')
def trigger_exception():
    app.logger.exception("Testing exception trigger")
    raise Exception("THIS IS A TEST EXCEPTION")
    return jsonify(**{'message': 'exception'}), 500

@app.route('/success')
def trigger_normal():
    sentry.captureMessage("Testing info trigger")
    return jsonify(**{'message': 'ok'}), 200


if __name__ == '__main__':
    app.run()
