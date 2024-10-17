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


client = DockerClient()
all_running_containers = client.container.list(filters={"status": "running"})
# print()


all_running_containers_list = [
    "obalkash-assemble-perf4-smc2210-1-09sa-hqt-service-1",
    "obalkash-assemble-perf4-smc2210-1-09sa-selenium-grid-1",
]

GRID_SERVICE = "selenium-grid-1"
HQT_SERVICE = "hqt-service-1"
hqt_containers = [container for container in all_running_containers_list if container.endswith(HQT_SERVICE)]
grid_containers = [container for container in all_running_containers_list if container.endswith(GRID_SERVICE)]

grid_containers.append("obalkash-assemble-perf-cds-node20-selenium-grid-1")


print(hqt_containers)
print(grid_containers)

grid_without_service = [
    grid_c
    for grid_c in grid_containers
    if all(grid_c.replace(GRID_SERVICE, HQT_SERVICE) != hqt_c for hqt_c in hqt_containers)
]


print(grid_without_service)
