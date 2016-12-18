import config
from novaclient import client

nt = client.Client(config.VERSION, config.USER, config.PASSWORD, config.TENANT, config.AUTH_URL, insecure=True)

print nt.flavors.list()

print nt.servers.list()
# nt.servers
print nt.keypairs.list()

print nt.images.list()

print nt.quotas.get()
