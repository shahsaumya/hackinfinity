import django

# Full path and name to your csv file
csv_filepathname="/home/saumya/Desktop/DAIICT/state_translator.csv"
# Full path to your django project directory
your_djangoproject_home="/home/saumya/Desktop/DAIICT/hack_infinity/hack_infinity"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
from app.models import State_translator

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',')

for row in dataReader:
 # Ignore the header row, import everything else
    state = State_translator()
    state.state_name = row[0]
    state.state_language = row[1]
    state.save()
    print('HI')