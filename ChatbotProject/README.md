# Automate Project Folder Xreation Script

This is a script to automatically generate a standardized directory structure, with the example of a chatbot project, in this case. The project's root directory will be created in the current working directory

## Directory Structure

The script will create the directory structure as a dictionary mappng the base project directory to a list of subdirectories

Additionally, the following common files will be created within the appropriate subdirectories:

- `README.md`
- `config/config.yaml`
- `config/credentials.json`
- `docker/Dockerfile`
- `docker/docker-compose.yml`
- `environment/requirements.txt`
- `environment/environment.yml`

## How to Use the Script

### Prerequisites

- Python 3.x installed on your machine

### Running the Script

1. Download the script and save it to a directory of your choice.
2. Open a terminal (or command prompt) and navigate to the directory where the script is saved.
3. Run the script by executing the following command:

   ```sh
   python auto-directories.py