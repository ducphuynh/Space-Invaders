#!C:\Users\Duc\Desktop\PycharmProjects\Alien_Invasion\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'surface==0.7.1','console_scripts','surface'
__requires__ = 'surface==0.7.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('surface==0.7.1', 'console_scripts', 'surface')()
    )
