from flask import Flask, render_template, request
from decouple import config
from opentok import Client

opentok_api= config('OPENTOK_API')
opentok_secret= config('OPENTOK_SECRET')

client = Client(opentok_api, opentok_secret)
session_id= Client.create_session().session_id

app=Flask(_name_,static_url_path='')

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        
    return "hello homepage!"
@app.route('/admin')
def index():
    return "hello admin!"
@app.route('/join')
def index():
    return "hello join!"

app.debug= True
app.run()
