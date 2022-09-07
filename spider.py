from functions.storage_functions import *
from functions.sleeper_functions import *
from functions.ff_stats import *
from functions.logsheets import *
import http.client, urllib.request, urllib.parse
from datetime import datetime
import numpy as np
import sys

start = datetime.now()

spider = sys.argv[1].lower()
seconds = int(sys.argv[2])
sample = int(sys.argv[3])
#seconds = 600
#sample = 1200

if spider == 'true':
    print("-----SPIDER-----")
    ul_spider(seconds, sample)

print("-----DRAFT META-----")
update_draft_meta(update=True)

print("-----DRAFT RESULTS-----")
update_draft_results(limit = 5000, update = True)

print("-----PREP TABLEAU-----")
prep_tableau(days_back = 45)

end = datetime.now()
print('Finished: ' + str(end-start))