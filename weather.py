import urllib.request
import json

key='1208628a847be972'
address=input('zip of where weather you want to see?\n')
condition='http://api.wunderground.com/api/'+key+'/conditions/q/BD/'+address+'.json'
forecast='http://api.wunderground.com/api/'+key+'/forecast/q/BD/'+address+'.json'
con = urllib.request.urlopen(condition)
fcr = urllib.request.urlopen(condition)
json_con=con.read()
json_fcr=fcr.read()

# print(json_string)
parsed_con=json.loads(json_con)
parsed_fcr=json.loads(json_fcr)
weather = parsed_con['current_observation']['weather']
temp = parsed_con['current_observation']['temperature_string']
# forecastday=['forecast'][0][0:7][5]
# for x in forecastday:
# 	print(forecastday)



print ('weather is  ' + weather.lower() +' and it\'s  '+temp + '  degrees')
con.close()
