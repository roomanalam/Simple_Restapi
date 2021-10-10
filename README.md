# Simple_Restapi
                                         Cafe & Wifi
Will render get requests of cafes in a certain location

GET   Get All Cafes
localhost:5000/all      
This route returns a json with the data from all cafes in the database.


GET  Get Random Cafe
localhost:5000/random      
Returns a random cafe from the database.


GET   Search Cafes By Location
localhost:5000/search?loc=Peckham    
The /search route will search the cafe database for a cafe that matches the location queried. Use the loc parameter to pass a location name.
Request Params
Location      Gurugram


POST Post New Cafe
localhost:5000/add?api-key=TopSecretAPIKey   
Adds a new cafe entry to the database. Requires authentication with api-key parameter.
Request Params
api-key  TopSecretAPIKey

Bodyurlencoded
name                Chai-Point
map_url             https://goo.gl/maps/wqCa2ao2x33SDGhw6
img_url             https://geo3.ggpht.com/cbk?panoid=dDQlwT5yA4CW69c5CzI_aA&output=thumbnail&cb_client=search.gws-prod.gps&thumb=2&w=408&h=240&yaw=211.9995&pitch=0&thumbfov=100    
location             Gurugram
seats                20-30
has_toilet           true/false
has_wifi             true/false
has_sockets          true/false
can_take_calls       true/false
coffee_price         150


PATCH    Update Coffee Price For Cafe
localhost:5000/update-price/21?new_price=$3.50  
Update the price of a black coffee at a particular cafe. Using the id and new_price parameters.
Request Params
api_key       TopSecretAPIKey

Bodyurlencoded
Coffee_new_price    $3.50


DEL   Delete a Cafe By Id
localhost:5000/report-closed/22?api_key=TopSecretAPIKey
Deletes a cafe from the database.You will need to provide the id of the cafe to delete as a route. You will also need to provide a valid API for this operation to be allowed.
Request Params
api_key       TopSecretAPIKey


requiment of pacakges
Flask 1.1.2
Flask-SQLAlchemy 2.3.2


