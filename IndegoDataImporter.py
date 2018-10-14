import csv

class Trip:
    def __init__(self, trip_id, duration):
        self.trip_id    # Locally unique integer that identifies the trip
        self.duration = duration      # Length of trip in minutes

##################################

csv_filepath = 'tiny-indego-trips.csv'

##################################

trips = {}

count = 0;
print 'Starting...'

with open(csv_filepath, 'rb') as csvfile:
    dictreader = csv.DictReader(csvfile)
    trips = dictreader

    for row in csvfile:
        count += 1
        if count % 10000 == 0:
            print count

print 'Done! Final count:', str(count);

print size(trips)
