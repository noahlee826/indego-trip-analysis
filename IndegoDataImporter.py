import  csv, urllib2, urllib

class Trip:
    def __init__(self, trip_id, duration):
        self.trip_id    # Locally unique integer that identifies the trip
        self.duration = duration      # Length of trip in minutes

##################################

csv_filepath = 'tiny-indego-trips.csv'

##################################

trips = {}

first_trip_id = ''

print 'Starting...'

with open(csv_filepath, 'rb') as csvfile:
    dictreader = csv.DictReader(csvfile)

    for row in dictreader:
        trips[row['trip_id']] = row

    print 'Done!'
    
for key in trips:
    first_trip_id = key if not first_trip_id else first_trip_id

my_trip = trips[first_trip_id]
params = urllib.urlencode((('fromPlace' , str(my_trip['start_lat']) + ',' + str(my_trip['start_lon'])),
                           ('toPlace' , str(my_trip['end_lat']) + ',' + str(my_trip['end_lon'])),
                           ('time', '4:20pm'),
                           ('date', '10-14-2018'),
                           ('mode' , 'BICYCLE')))
print 'http://localhost:8080/otp/routers/default/plan?' + params

f = urllib2.urlopen("http://localhost:8080/otp/routers/default/plan?", params)
print f.read()

                          
                           
