from flask import Flask, redirect, url_for
from google.appengine.api import taskqueue
from google.appengine.ext import ndb
from datetime import datetime 
import numpy as np
import logging
import time

app = Flask(__name__)

class HelloWorld(ndb.Model):
	# https://cloud.google.com/appengine/docs/standard/python/ndb/
	Date = ndb.DateTimeProperty(indexed=True)
	Text = ndb.StringProperty(indexed=True)
	Integer = ndb.IntegerProperty(indexed=True)
	Float = ndb.FloatProperty(indexed=True)

@app.route('/')
def hello_world():
	return "Hello World!"

@app.route('/insert')
def insert_datastore():

	now = datetime.now()
	hello_data = HelloWorld(Date = now,
							Text='hello world!',
							Integer= now.hour,
							Float=np.random.rand(1)[0])
	hello_data.put()
	return 'Data inserted to datastore at {}'.format(now), 200

@app.route('/queue')
def queue_task():
	queue = taskqueue.Queue(name='happyqueue')
	task = taskqueue.Task(
	    url="/delay_insert",
	    method="GET",
	    target="neurotic")
	    # payload=json.dumps(payload))
	rpc = queue.add_async(task)
	task = rpc.get_result()
	logging.info(task)
	return "queue"

@app.route('/delay_insert')
def delay():
	now = datetime.now()
	time.sleep(5)
	logging.info('task queue at time {}'.format(now.isoformat()))
	hello_data = HelloWorld(Date = now,
							Text='queued hello world!',
							Integer= now.hour,
							Float=np.random.rand(1)[0])
	hello_data.put()
	return 'Data inserted from queue to datastore at {}'.format(now), 200

if __name__=='__main__':
	app.run()
