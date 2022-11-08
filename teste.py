import docker
import os
from dotenv import load_dotenv

load_dotenv()

DOCKER_TYPE = os.getenv("DOCKER_TYPE")
DOCKER_API_SERVER = os.getenv("DOCKER_API_SERVER")
DOCKER_API_PORT = os.getenv("DOCKER_API_PORT")

REGISTRY = os.getenv("REGISTRY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

REPOSITORY = os.getenv("REPOSITORY")
TAG = os.getenv("TAG")

IMAGE_PULL = "{0}/{1}:{2}".format(REGISTRY, REPOSITORY, TAG)
PORTS = {}

_PORTS = os.getenv("PORTS")
_PORTS_LIST = _PORTS.split(',')
for port in _PORTS_LIST:
    VAR = port.split(':')
    PORTS[int(VAR[0])] = int(VAR[1])

BASE_URL = "tcp://{0}:{1}".format(DOCKER_API_SERVER, DOCKER_API_PORT)

if DOCKER_TYPE.upper() == "UNIX":
    BASE_URL = 'unix://var/run/docker.sock'
else:
    BASE_URL = 'tcp://{0}:{1}'.format(DOCKER_API_SERVER, DOCKER_API_PORT)


client_docker = docker.DockerClient(base_url = BASE_URL)

print("docker login")
client_docker.login(
    registry = REGISTRY,
    username = USERNAME,
    password = PASSWORD)


print("docker pull")
client_docker.images.pull(IMAGE_PULL)


print("docker container run")

for container in client_docker.containers.list():
    print (container.name)
    if REPOSITORY in container.name:
        print ('Chegou aqui')
        container.stop()
        container.remove()
container = client_docker.containers.run(
        image = IMAGE_PULL,
        name = REPOSITORY,
        ports = PORTS,
        detach=True)
                