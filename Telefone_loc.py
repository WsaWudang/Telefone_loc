import phonenumbers
from phonenumbers import geocoder
import opencage
import folium
from pprint import pprint

#Ajustar telefone para usar o phonenumbers
numero = "Digite um Número"
numero_pesquisado = phonenumbers.parse(numero, "BR")
print(numero_pesquisado)

#Descobrir a localização do telefone (estado)
localizacao = geocoder.description_for_number(numero_pesquisado, "br")
print(f"Esse número  de telefone é do estado de: {localizacao}")

#Operadora do telefone 
from phonenumbers import carrier
servico = phonenumbers.parse(numero, "BR")
operadora = carrier.name_for_number(servico, "pt-br")
print(f"Esse número  de telefone é da operadora: {operadora}")

#Coordenadas Telefone
from opencage.geocoder import OpenCageGeocode

chave = "0747088136b14157a16fb12657c588d9"

geocoder = OpenCageGeocode(chave)
consulta = str(localizacao)
resultado = geocoder.geocode(consulta)

lat = resultado[0]["geometry"]["lat"]
lng = resultado[0]["geometry"]["lng"]

print(f"O centro da cidade do numero ({numero}) são as coordenadas: {lat, lng}")

#Atalho para abrir no navegador as coordenadas
meu_mapa = folium.Map(localizacao=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=localizacao).add_to(meu_mapa)

meu_mapa.save("meu_mapa.html")

#Descrição Detalhada das coordenadas
#resultado = geocoder.reverse_geocode(lat, lng)
#pprint(resultado)