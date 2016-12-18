
import config
from flask import Flask, render_template, jsonify, url_for
from novaclient import client


app = Flask(__name__)
nt = client.Client(config.VERSION, config.USER, config.PASSWORD, config.TENANT, config.AUTH_URL, insecure=True)

# print nt.flavors.list()


@app.route('/')
def index():
    instances = nt.servers.list()
    return render_template(
        'index.html', instances=instances)


@app.route('/instance/<instance_id>')
def instance_details(instance_id):
    instance = nt.servers.get(instance_id)
    # nt.volumes.get_server_volume()
    print nt.flavors.list()
    return render_template(
        'instance_details.html',
        instance=instance)


@app.route('/volumes/<instance_id>')
def volumes(instance_id):
    volumes_list = nt.volumes.get_server_volumes(instance_id)
    data = dict()

    for i in volumes_list[0]:
        print i
    # print dir(volumes_list)
    # for x in dir(volumes_list):
    #     # print x
    #     # data[x] = volumes_list
    #     data[x] = ''
    return jsonify(data)


app.run(debug=True)
