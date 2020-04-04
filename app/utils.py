import os
import sys

from pprint import pprint


def dd(variable):
    pprint(variable)
    sys.exit()


def upload_path():
    is_windows = os.name == 'nt'
    directory = os.path.abspath('/opt/SGDF')

    if is_windows:
        directory = os.path.abspath('C:\\SGDF')

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory
