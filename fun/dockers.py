import os

import docker
import gzip
import shutil

client = docker.from_env()

for image in client.images.list():
    print(image)

CADVISOR_VERSION = "v0.46.0"
CADVISOR_FILE = "cadvisor.tar"
CADVISOR_ARCHIVE = f"{CADVISOR_FILE}.gz"

image = client.images.pull(f"gcr.io/cadvisor/cadvisor:{CADVISOR_VERSION}")
with open(CADVISOR_FILE, "wb") as f:
    for chunk in image.save(named=True):
        f.write(chunk)

with open(CADVISOR_FILE, "rb") as f_in:
    with gzip.open(CADVISOR_ARCHIVE, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove(CADVISOR_FILE)
os.remove(CADVISOR_ARCHIVE)
