from functions.storage_functions import *
from functions.sleeper_functions import *
from functions.ff_stats import *
from functions.logsheets import *
import http.client, urllib.request, urllib.parse
from datetime import datetime
import numpy as np
import sys

## User League Spider

start = datetime.now()

seconds = int(sys.argv[1])
sample = int(sys.argv[2])
#seconds = 600
#sample = 1200

ul_spider(seconds, sample)