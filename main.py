from flask import Flask, request
import screen_brightness_control as sbc

app =  Flask(__name__)

@app.route('/brilho', methods=["POST"] )
def controlBrightness():
  body = request.get_json()
  sbc.set_brightness(body["value"])
  return body





app.run()