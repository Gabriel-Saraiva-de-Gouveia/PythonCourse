from pygeocoder import Geocoder
endereco = 'avenida londrina, sarandi pr' #-> no case sensitive
resultado = Geocoder('#chave api...').reverse_geocode('#COODERNADAS')
    #Geocoder('#chave api google geocoding').geocode(endereco) # .state .postal_code .coutry .coordinates
print(resultado)
