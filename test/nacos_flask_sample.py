# -*- coding=utf-8 -*-
from flask import Flask
import nacos

PORT = 777
HOST = "127.0.0.1"
app = Flask(__name__)

client = nacos.NacosClient(server_addresses="localhost:8848")
result = client.add_naming_instance(service_name="flask-service",
                                    ip=HOST,
                                    port=PORT,
                                    metadata={"version": "1.0"},
                                    )
print(result)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
