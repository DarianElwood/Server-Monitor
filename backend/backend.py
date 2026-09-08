from flask import Flask, jsonify
from monitor.monitor import Monitor
from monitor.address import Address

app = Flask(__name__)

monitor = Monitor([
    Address("vps-8f5796f3.vps.ovh.net", 2303),
])

@app.get("/servers")
def get_servers():
    return jsonify(monitor.fetch())

if __name__ == "__main__":
    app.run(debug=True)