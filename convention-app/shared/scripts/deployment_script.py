import os
import subprocess

def deploy():
    # Example: Build and run Docker containers
    print("Building Docker containers...")
    subprocess.run(["docker-compose", "build"])
    
    print("Starting Docker containers...")
    subprocess.run(["docker-compose", "up", "-d"])
    
    print("Deployment completed successfully.")

if __name__ == "__main__":
    deploy()