"""
Simple Flask web site 
"""

import flask
from flask import render_template
from flask import request  # Data from a submitted form
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging
import pre

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key  # Should allow using session variables

###
# Pages
###

@app.route('/')
@app.route('/index')
def index():
    if True:
    #if 'locations' not in flask.session:
        app.logger.debug("Processing locations file")
        raw = CONFIG.locations
        location_data = pre.process(raw)
        #flask.session['locations'] = location_data
        app.logger.debug(location_data)

    return flask.render_template('maps.html', locations=json.dumps(location_data))

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html')

#############

if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    #FIXME:  Debug cgi interface 
    app.debug=False

