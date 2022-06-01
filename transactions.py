from functions.transaction_functions import *
from functions.sleeper_functions import *
import pandas as pd

# Update the Players and store into dataframe
players = update_players()


# Get transactions of recently active leagues

df = get_transactions(sample = 20, scoring_type = 'dynasty_2qb')

