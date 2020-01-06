# ============ Get data from NASA insight rover API as a JSON stream ==============
#     Your API key is: #############################################
#     You can start using this key to make web service requests. Simply pass your key in the URL when making a web request. Here's an example:
#    "https://api.nasa.gov/insight_weather/?api_key=#############################################"
# Variables to use from API documentation
# sol_keys, most_common, WD, Season, sols_checked,,PRE,HWS,AT
#
# #============ weather data returns 7 days from yesterday as the data may not be current yet. ===========

API_url = "https://api.nasa.gov/insight_weather/?api_key=#############################################"
API_data = requests.get(API_url).json()

# define weather data attributes

context = {'sol_keys': API_data["sol_keys"]}

def index(request):
    SOL_KEYS = API_data["sol_keys"]
    weather_data = []
    for key in SOL_KEYS:
        weather = dailyWeather()
        weather.pk = key
        if(API_data[key].get('AT')):
            weather.temp = API_data[key]['AT']['av']
            weather.temp_min = API_data[key]['AT']['mn']
            weather.temp_max = API_data[key]['AT']['mx']
        else:
            weather.temp = 0.0
        if(API_data[key].get('PRE')):
            weather.pressure = API_data[key]['PRE']['av']
        if(API_data[key].get('HWS')):
            weather.wind_speed= API_data[key]['HWS']['av']
            weather.wind_freq= API_data[key]['HWS']['ct']
        else:
            weather.wind_speed= 0.0
        weather.season = API_data[key]['Season']
        if(API_data[key]['WD'].get('most_common')):
            weather.wind_direction = API_data[key]['WD']['most_common']['compass_point']
            weather.wind_direction_deg = API_data[key]['WD']['most_common']['compass_degrees'] 
        weather.save()
        print(weather)
        weather_data.append(weather)
    print(weather_data)
    context = {"weather_data": weather_data}
    print(context["weather_data"])
    return render(request, 'mars_weather/weather.html', context)