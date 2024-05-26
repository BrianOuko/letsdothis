import os
directory_structure={
    'ChatbotProject':['data/raw','data/processed', 'data/scripts',
        'models/trained',
        'models/scripts',
        'notebooks/eda',
        'notebooks/experiments',
        'src/bot/api',
        'src/bot/core',
        'src/bot/responses',
        'src/utils',
        'config',
        'logs',
        'tests',
        'docs',
        'docker',
        'environment'
    ]
}

def create_directories(base_path, directories):
    for dir_path in directories:
        full_path=os.path.join(base_path, dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f'Created: {full_path}')

if __name__ == '__main__':
    base_path=os.getcwd()
    project_name='ChatbotProject'

project_path=os.path.join(base_path, project_name)
os.makedirs(project_path, exist_ok=True)
print(f'Created project root directory: {project_path}')

create_directories(project_path, directory_structure[project_name])

common_files= [
    'README.md',
    'config/config.yaml',
    'config/credentials.json',
    'docker/Dockerfile',
    'docker/docker-compose.yml',
    'environment/requirements.txt',
    'environment/environment.yml'
]

for file_path in common_files:
    full_file_path = os.path.join(project_path, file_path)
    with open(full_file_path,'w') as f:
        f.write('')
    print(f'created file:{full_file_path}')
