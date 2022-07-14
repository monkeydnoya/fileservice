import os 
from pathlib import Path

path = str(Path.home())

config = {
    'host':os.environ.get('host','localhost'),
    'port':os.environ.get('port','8000'),
    'directory_path':os.environ.get('directory_path',f'fileservice/filesave'),
}

