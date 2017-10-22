import json
import sys
import os
from pprint import pprint

out = 'Albums/'

if not os.path.exists(out):
    os.makedirs(out)

with open(sys.argv[1]) as data_file:    
    d = json.load(data_file)

for x in d:
  try:
    p = x['Name'] + '/'
    if not os.path.exists(out + p):
      os.makedirs(out + p)
    for i in x['Songs']:
      print('wget -c -q -U "TotallyLegit" -O "' + out + p + i['Name'] + '" "' + i['DownloadUrl'] + '"')
  except Exception as e:
    pass
