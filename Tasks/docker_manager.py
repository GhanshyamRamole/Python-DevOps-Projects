import os
import docker

def build_and_push_image(image_name):
    os.system(f"docker build -t {image_name} .")
    os.system(f"docker push {image_name}")

if __name__ == "__main__":
    build_and_push_image("your-dockerhub-username/devops-automation:latest")



# view list containers

client = docker.from_env()
containers = client.containers.list()
for container in containers:
 print(container.name)
