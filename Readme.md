# DoGMA - Docker GUI Management Application

## Features

- Grants and revokes X Server access for GUI applications
- Starts a Docker container
- Attaches to a running Docker container
- Executes a GUI application inside the container

## Prerequisites

- Docker
- Docker Compose
- Python 3.x

## Directory Structure

dogma/  
├── Dockerfile: Defines the Docker container including the necessary dependencies  
├── docker-compose.yml: Docker Compose configuration file  
├── dogma.py: Script to manage the Docker container and run the application  
  
## Getting Started

1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/williamblair333/dogma.git
    cd dogma
    ```
2. **Run the script:**
    ```bash
    python dogma.py <container_name> <application_path>
    python3 dogma.py gpt4all-gpt4all-1 /root/gpt4all/bin/chat
    ```
## Notes, Security

- X Server access is granted temporarily and revoked immediately after running the application

## Notes, General

- Ensure you have all prerequisites installed before running the script

## Test image and container

A Docker image using a specified distro is attached for convenience to illustrate/test the features.

## Anything else relevant to each specific project

- Make sure to customize the Dockerfile and docker-compose.yml as per your project requirements.
