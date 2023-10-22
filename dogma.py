import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Run a Docker container and execute an application inside it.')
    parser.add_argument('container_name', help='Name of the Docker container to run')
    parser.add_argument('application_path', help='Path of the application to execute inside the container')

    args = parser.parse_args()

    # Grant X Server Access
    os.system("xhost +")

    # Start the Docker Container
    os.system(f"docker start {args.container_name}")

    # Run the Application within the Container
    os.system(f"docker exec -it {args.container_name} bash -c '{args.application_path}'")

    # Revoke X Server Access
    os.system("xhost -")

if __name__ == '__main__':
    main()
