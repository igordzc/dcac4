import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonacci():
  prox = 1
  ant = 0
  lim = 50
  found = 0
  resp = "0, "
  while (found < lim):
    temp = prox
    prox = prox + ant
    ant = temp
    found = found + 1
    resp += str(prox) + ", "


  return resp

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
