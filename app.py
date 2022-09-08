from flask import *
import requests
app = Flask(__name__)

@app.route('/')
def ppp():
  return render_template('home.html')
  
@app.route('/pop',methods=['POST'])
def index():
  data = None
  data = request.get_json()
  print(data)
  return jsonify(data), 200
  return {"status": "OK"},200
  
@app.route('/page',methods=['POST'])
def home():
  data = request.form
  print(data['fname'])
  print(data['contact'])    
  return jsonify(data), 200
      

if __name__ == "__main__":
  app.run(debug=True)