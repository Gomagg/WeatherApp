from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4e614bcd3a42dd8d8359354a95d6114d&units=metric').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + '' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'c',
            "pressure": str(json_data['main']['pressure'])+'N/m2',
            "humidity": str(json_data['main']['humidity'])+'g/m3',
        }
        
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})