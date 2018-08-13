import os, sys
import pandas
import sqlite3
def offline_mode():
	conn = sqlite3.connect("db.sqlite3")
	#adding birdhit data to sqlite database
	df1 = pandas.read_csv("Bird_Hit_Report.csv")
	df1.to_sql("useraccount_bird_hit_form", conn, if_exists='append', index=False)
	#adding incident data to sqlite database
	df2 = pandas.read_csv("Incident_Report_Form.csv")
	df2.to_sql("useraccount_incident_form", conn, if_exists='append', index=False)
	#flush bird-hit csv file
	f = open("Bird_Hit_Report.csv", "w")
	f.truncate()
	f.close()
	#flush incident-hit csv file
	f = open("Incident_Report_Form.csv", "w")
	f.truncate()
	f.close()
	#reload bird-hit header into csv 
	target = 'Bird_Hit_Report.csv'
	src = 'bhr.csv'
	tf = open(target, 'a')
	tf.write(open(src).read())
	tf.close()
	#reload incident-hit header into csv 
	target = 'Incident_Report_Form.csv'
	src = 'ihr.csv'
	tf = open(target, 'a')
	tf.write(open(src).read())
	tf.close()
