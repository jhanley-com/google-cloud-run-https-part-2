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

""" This module implents HTML page builder functions.
"""
def build_body_top():
	""" build the page top HTML """

	page_title = 'Google Cloud Run - Sample Python Flask Example | John Hanley'

	body = '<!DOCTYPE html>\n'
	body += '<html lang="en">\n'
	body += '<head>\n'
	body += '    <meta charset="utf-8">\n'
	body += '    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
	body += '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
	body += '    <title>' + page_title + '</title>'
	body += '    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />\n'
	body += '    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.11.2.js"></script>\n'
	body += '    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'
	body += '    <style>\n'
	body += '        table { width: 100%; }\n'
	body += '        table, th, td {border: 1px solid black;}\n'
	body += '        table {border-collapse: collapse;}\n'
	body += '        th, td {border: 1px solid #ddd; padding 8px;}\n'
	body += '        th {padding-top: 12px; padding-bottom: 12px;\n'
	body += '        text-align: left; background-color: #4CAF50;color: white;}\n'
	body += '        tr:nth-child(even){background-color: #f2f2f2;}\n'
	body += '        tr:hover {background-color: #ddd;}\n'
	body += '    </style>\n'
	body += '</head>\n'
	body += '<body>\n'

	body += '<section class="container">\n'
	body += '<div class="row">\n'
	return body

def build_table_top():
	""" build the table top HTML """
	body = '<table>\n'
	body += '<thead>\n'
	body += '<tr>\n'
	body += '<th>Key</th>\n'
	body += '<th>Value</th>\n'
	body += '</tr>\n'
	body += '</thead>\n'
	body += '<tbody>\n'
	return body

def build_table_bottom():
	""" build the table bottom HTML """
	body = '</tbody>\n'
	body += '</table>\n'
	return body

def build_body_bottom():
	""" build the page bottom HTML """
	body = ''
	body += '</div>	<!-- row -->\n'
	body += '</section>\n'
	body += '</body></html>'
	return body

def add_row(key, value):
	""" Add a row to the HTML table """

	body = '<td>' + key + '</td>\n'
	body += '<td>' + str(value) + '</td>\n'
	body += '</tr>\n'

	return body
