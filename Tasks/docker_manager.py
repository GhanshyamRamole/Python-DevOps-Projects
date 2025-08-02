import os

def build_and_push_image(image_name):
    os.system(f"docker build -t {image_name} .")
    os.system(f"docker push {image_name}")

if __name__ == "__main__":
    build_and_push_image("your-dockerhub-username/devops-automation:latest")

