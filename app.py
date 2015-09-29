# Adding a comment here so that I can check it in to the repo...

from flask import Flask, render_template, request, redirect, url_for, Markup
import jinja2

import requests
from datetime import datetime

import numpy as np
import pandas as pd

# For Visualization
from bokeh.plotting import figure, gridplot, output_file, show, save
from bokeh.embed import components
from bokeh.charts import Bar

from sklearn.naive_bayes import GaussianNB
import dill


app = Flask(__name__)

app.vars={}

naivebayes = dill.load(open("./NB_Gauss_model.pkl"))


@app.route('/')
def main():
	return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('./index.html')
	else:
		#REQUEST WAS A POST
		app.vars['city'] = request.form['city']
		
		print app.vars['city']
		print type(app.vars['city'])


		if str(app.vars['city']) == "NYC":

			return redirect('nyc')

		else:
			return render_template('SF.html')

@app.route('/nyc',methods=['GET','POST'])
def nyc():
	if request.method == 'GET':
		return render_template('./nyc2.html')
	else:
		#REQUEST WAS A POST
		app.vars['complaint'] = request.form['complaint']
		
		print app.vars['complaint']
		print type(app.vars['complaint'])


		if str(app.vars['complaint']) == "BD":
			return render_template('NYC_BlockedDriveway_2015.html')

		elif str(app.vars['complaint']) == "HH":
			return render_template('NYC_HeatHotWater_2015.html')

		elif str(app.vars['complaint']) == "IP":
			return render_template('NYC_IllegalParking_2015.html')

		elif str(app.vars['complaint']) == "SC":
			return render_template('NYC_StreetCondition_2015.html')

		elif str(app.vars['complaint']) == "SLC":
			return render_template('NYC_StreetLightCondition_2015.html')

		elif str(app.vars['complaint']) == "UC":
			return render_template('NYC_UnsanitaryCondition_2015.html')

		elif str(app.vars['complaint']) == "WS":
			return render_template('NYC_WaterSystem_2015.html')

		elif str(app.vars['complaint']) == "PL":
			return render_template('NYC_Plumbing_2015.html')

		elif str(app.vars['complaint']) == "PP":
			return render_template('NYC_PaintPlaster_2015.html')

		elif str(app.vars['complaint']) == "NSS":
			return render_template('NYC_StreetNoise_2015.html')


		elif str(app.vars['complaint']) == "RATS":
			return render_template('NYC_Rodents_2015.html')

		elif str(app.vars['complaint']) == "Prediction":
			return redirect('nyc_predict')

@app.route('/nyc_predict',methods=['GET','POST'])
def nyc_predict():
	if request.method == 'GET':
		return render_template('./nyc3.html')
	else:
		#REQUEST WAS A POST
		app.vars['Month'] = request.form['Month']
		app.vars['Hour'] = request.form['Hour']
		app.vars['Borough'] = request.form['Borough']
		app.vars['Temp'] = request.form['Temp']
		app.vars['Pressure'] = request.form['Pressure']

		print "Month =", app.vars['Month']
		print "Hour =", app.vars['Hour']
		print "Borough =", app.vars['Borough']
		print "Temp =", app.vars['Temp']
		print "Pressure =", app.vars['Pressure']

		XPred = [int(app.vars['Borough']), int(app.vars['Hour']), int(app.vars['Temp']), int(app.vars['Pressure']), int(app.vars['Hour'])]

		print "XPred =", XPred
		prediction = int(naivebayes.predict(XPred))
		print "Prediction = ", prediction

		if prediction == 1:
			return render_template('NYC_BlockedDriveway_2015_2.html')

		elif prediction == 2:
			return render_template('NYC_HeatHotWater_2015_2.html')

		elif prediction == 3:
			return render_template('NYC_WaterSystem_2015_2.html')

		elif prediction == 4:
			return render_template('NYC_IllegalParking_2015_2.html')

		elif prediction == 5:
			return render_template('NYC_StreetNoise_2015_2.html')

		elif prediction == 6:
			return render_template('NYC_PaintPlaster_2015_2.html')

		elif prediction == 7:
			return render_template('NYC_Plumbing_2015_2.html')

		elif prediction == 8:
			return render_template('NYC_StreetCondition_2015_2.html')

		elif prediction == 9:
			return render_template('NYC_StreetLightCondition_20152.html')

		elif prediction == 10:
			return render_template('NYC_UnsanitaryCondition_2015_2.html')

		elif prediction == 11:
			return render_template('NYC_Other.html')



if __name__ == '__main__':
  app.run(port=33507)
