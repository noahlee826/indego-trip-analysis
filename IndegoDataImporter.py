import  csv, urllib, urllib.request, requests

class Trip:
    def __init__(self, trip_id, duration):
        self.trip_id    # Locally unique integer that identifies the trip
        self.duration = duration      # Length of trip in minutes

##################################

csv_filepath = 'tiny-indego-trips.csv'

##################################

trips = {}

first_trip_id = ''

print ('Starting...')

with open(csv_filepath) as csvfile:
    dictreader = csv.DictReader(csvfile)

    for row in dictreader:
        trips[row['trip_id']] = row

    print ('Done!')
    
for key in trips:
    first_trip_id = key if not first_trip_id else first_trip_id

my_trip = trips[first_trip_id]
params = urllib.parse.urlencode((('fromPlace' , str(my_trip['start_lat']) + ',' + str(my_trip['start_lon'])),
                           ('toPlace' , str(my_trip['end_lat']) + ',' + str(my_trip['end_lon'])),
                           ('time', '4:20pm'),
                           ('date', '10-14-2018'),
                           ('mode' , 'BICYCLE'))).encode("utf-8")

param_dict = {'fromPlace' : str(my_trip['start_lat']) + ',' + str(my_trip['start_lon']),
                           'toPlace' : str(my_trip['end_lat']) + ',' + str(my_trip['end_lon']),
                           'time': '4:20pm',
                           'date': '10-14-2018',
                           'mode': 'BICYCLE'}

r = requests.get("http://localhost:8080/otp/routers/default/plan", param_dict)
print(r.text)

#print ('http://localhost:8080/otp/routers/default/plan?' + params)

#req = urllib.request.Request("http://localhost:8080/otp/routers/default/plan", params, {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.36'})

#response = urllib.request.urlopen(req)

#html = response.read()
#print(html)
                           
