from flask import Flask
from flask import send_from_directory as static
from flask import render_template as sendHTML

app = Flask(__name__)
@app.route('/static/<path:path>')
def staticSend(path):
    return static('static', path)

@app.route("/")
def index():
    return sendHTML("index.html", 
      BTN1="Home",
      BTN2="About us",
      BTN3="Contact us",
      COMPANY_NAME="Cheese HQ", 
      SPECIALIZATION="cheese creation",
      CSTMR_MSG="care greatly about our product quality, and we are committed to providing the best service possible. We are always looking for ways to improve our products and services",
      MSION_MSG1="we are looking for small businesses to expand our business",
      MSION_MSG2="have award winning cheese and customer support/service"
    )
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
