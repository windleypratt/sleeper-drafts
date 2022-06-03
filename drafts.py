from functions.sleeper_functions import *

print("-----DRAFT META-----")
update_draft_meta(update=True)

print("-----DRAFT RESULTS-----")
update_draft_results(limit = 5000, update = True)

print("-----PREP TABLEAU-----")
prep_tableau(days_back = 45)