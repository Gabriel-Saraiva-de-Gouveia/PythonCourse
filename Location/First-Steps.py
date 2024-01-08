from pygeocoder import Geocoder
endereco = '552, Machado de Assis, Sarandi, PR'
print(Geocoder('AIzaSyChn_ezkAEL7_AYyReDCP9cyCnAJsRbyN0').geocode(endereco).coordinates)