############################################################
# Version 0.90
# Date Created: 2019-05-15
# Last Update:  2019-05-15
# https://www.jhanley.com
# Author: John J. Hanley
#
# No copyright. You may use this source code as is for any purpose.
# No warranty for any purpose express or implied.
# Use at your own risk.
# This is sample code that is not production quality.
############################################################

import os
import logging

from flask import Flask
from flask import request
from flask import redirect
from flask import send_from_directory

import myhtml

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

def handle_proxy_http_to_https():
	host = request.host

	if ':' in host:
		host = host.split(':')[0]

	for i in request.headers:
		if i[0].lower() == 'x-forwarded-proto':
			if i[1].lower() == 'http':
				url = 'https://' + host + request.path
				print('URL:', url)
				response = redirect(url, 301)
				print(response)

				return response
	return None

@app.route('/')
def home():
	response = handle_proxy_http_to_https()
	if response != None:
		return response

	body = myhtml.build_body_top()

	body += """
<h3>Hello Google Cloud Run World!</h3>
<p>
  <a href="https://cloud.google.com/run/" target="_blank">Google Cloud Run Website</a>
</p>
<p>
  <a href="/headers">Click to see request headers</a>
</p>
"""
	body += myhtml.build_body_bottom()

	return body
 
@app.route('/headers')
def my_headers():
	response = handle_proxy_http_to_https()
	if response != None:
		return response

	body = myhtml.build_body_top()

	body += myhtml.build_table_top()

	for i in request.headers:
		body += myhtml.add_row(i[0], i[1])

	body += myhtml.build_table_bottom()

	body += myhtml.build_body_bottom()

	return body

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
