from flask import Flask, jsonify
from monitor.monitor import Monitor
from monitor.address import Address
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

monitor = Monitor([
    Address("vps-8f5796f3.vps.ovh.net", 2303),
])

@app.get("/v1/api/serverQuery")
def get_servers():
    return jsonify(monitor.fetch())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
    