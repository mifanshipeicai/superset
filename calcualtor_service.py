from flask import Flask, jsonify, request
import re

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

# 简单模拟
resp = "[{	\"cob_date\": \"2022-12-30 00:00:00\",	\"riskclass\": \"FX\",	\"underlying\": \"GBP\",	\"fx weight sensi\": \"1111.000\"}, {	\"cob_date\": \"2022-12-30 00:00:00\",	\"riskclass\": \"FX\",	\"underlying\": \"EUR\",	\"fx weight sensi\": \"2222.000\"}, {	\"cob_date\": \"2022-12-30 00:00:00\",	\"riskclass\": \"FX\",	\"underlying\": \"USD\",	\"fx weight sensi\": \"3333.000\"}]"

@app.route("/calculate", methods=["GET"])
def get_all_users():
    return resp


if __name__ == '__main__':
    app.run(host="localhost", port="8081", debug=True)
