"""add docker compose file to run program"""

from python_on_whales import DockerClient

client1 = DockerClient(compose_files=["docker-compose.yaml"], compose_project_name="my_name1")
client2 = DockerClient(compose_files=["docker-compose2.yaml"], compose_project_name="my_name2")

client1.compose.up(detach=True)
containers = [container for container in client1.compose.ps() if "nginx" in container.name]
print(containers)
print([container.name for container in client1.compose.ps()])
print([container.id for container in client1.compose.ps()])

client2.compose.up(detach=True)
containers2 = [container for container in client2.compose.ps() if "nginx" in container.name]
print(containers2)
print([container.name for container in client2.compose.ps()])
print([container.id for container in client2.compose.ps()])

client1.compose.down()
client2.compose.down()
