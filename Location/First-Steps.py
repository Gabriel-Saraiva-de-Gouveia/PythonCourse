from pygeocoder import Geocoder
endereco = '20 W 34th St., New York, NY 10001, Estados Unidos'
print(Geocoder('AIzaSyChn_ezkAEL7_AYyReDCP9cyCnAJsRbyN0').geocode(endereco).coordinates)
