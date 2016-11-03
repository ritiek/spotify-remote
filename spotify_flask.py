#!/bin/python

from flask import Flask
from flask import request
from flask import redirect
import os
import sys

os.chdir(sys.path[0])
app = Flask(__name__)

@app.route('/')
def my_form():
	template = '''<html><head></head><body>
	<form action="." method="POST">
	<input type="submit" name="submit" value="Pause/Play" style="font-size:36pt;height:150px;width:480px;">
	<input type="submit" name="submit" value="Increase Vol." style="font-size:36pt;height:150px;width:480px;">
	<input type="submit" name="submit" value="Decrease Vol." style="font-size:36pt;height:150px;width:480px;">
	<input type="submit" name="submit" value="Song Up" style="font-size:36pt;height:150px;width:480px;">
	<input type="submit" name="submit" value="Song Down" style="font-size:36pt;height:150px;width:480px;">
	<input type="submit" name="submit" value="Toggle Repeat" style="font-size:36pt;height:150px;width:480px;">
	</form></body></html> '''
	return template
	#return render_template("flaskie.html")

@app.route('/', methods=['POST'])
def my_form_post():
	if request.form['submit'] == 'Pause/Play':
		os.system('spotify_args.exe play/pause')
	if request.form['submit'] == 'Increase Vol.':
		os.system('spotify_args.exe up')
	if request.form['submit'] == 'Decrease Vol.':
		os.system('spotify_args.exe down')
	if request.form['submit'] == 'Song Up':
		os.system('spotify_args.exe prev')
	if request.form['submit'] == 'Song Down':
		os.system('spotify_args.exe next')
	if request.form['submit'] == 'Toggle Repeat':
		os.system('spotify_args.exe repeat')
	return redirect("/", code=302)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=1080)