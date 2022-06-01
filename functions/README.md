## Function Files

### 1. Sleeper Functions
These functions work primarily in the [Sleeper.app API](https://docs.sleeper.app/#players), augmented by other functions in files within the same folder.

#### update_players(path='Files/palyers.csv', manual=False, status='all'):
The Players API from Sleeper is heavy, so out of respect this function attempts to update data at most once per day. It checks the last-modified time of `Files/players.csv` and runs the function only if the file has not been updated `today`.