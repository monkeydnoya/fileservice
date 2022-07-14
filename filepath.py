import os
from datetime import date
from settings import config


def date_path_check():
    directoryPath = config['directory_path']


    today = date.today()

    filePath = os.path.join(directoryPath, str(today))

    isdir = os.path.isdir(filePath)

    return filePath, isdir
