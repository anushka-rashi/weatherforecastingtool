#write a code to import the necessary libraries
import requests
import json
#write a code to get Api key from openweathermap.org
API_KEY = "17d59437ed32af4dce8429118c2d9b5d"  # Replace with your OpenWeatherMap API key
#write a code to get URL from openweathermap.org
def get_weather(city):
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response_current = requests.get(current_weather_url)
    response_forecast = requests.get(forecast_url)
#write a code to get response from openweathermap.org
    if response_current.status_code == 200 and response_forecast.status_code == 200:
        current_weather_data = json.loads(response_current.text)
        forecast_data = json.loads(response_forecast.text)
        return current_weather_data, forecast_data
    else:
        print(f"Error: {response_current.status_code} - {response_forecast.status_code}")
        return None, None
#write a code to get html content from openweathermap.org
def generate_html(current_weather, forecast):
    if current_weather is None or forecast is None:
        return
#write a code to get city name from openweathermap.org
    city = current_weather['name']
#write a code to get temperature from openweathermap.org
    temperature = current_weather['main']['temp']
#write a code to get humidity from openweathermap.org
    humidity = current_weather['main']['humidity']
#write a code to get description from openweathermap.org
    description = current_weather['weather'][0]['description']
#write a code to get html content from openweathermap.org
    html_content = f'''
    <html>
    <head>

        <style>
            .main {{
                margin-top: 50px;
            }}
            .weather-panel {{
                background-image: url("clear.jpg");
                background-size: cover;
                background-position: center;
                border-radius: 20px;
                box-shadow: 25px 25px 40px 0px rgba(0,0,0,0.33);
                color: #fff;
                overflow: hidden;
                position: relative;
            }}
            .weather-panel .header {{
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
                text-align: center;
            }}
            
            .weather-panel .forecast {{
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                padding: 20px;
            }}
            .weather-panel .forecast .day {{
                flex-basis: 100%;
                margin-bottom: 20px;
            }}
            .weather-panel .forecast .day .title {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
            .weather-panel .forecast .day .info {{
                font-size: 14px;
            }}
            .weather-panel .forecast .day .temperature {{
                font-size: 24px;
                font-weight: bold;
            }}
            .weather-panel .forecast .day .description {{
                font-size: 14px;
            }}
            .weather-panel .forecast .day .humidity {{
                font-size: 14px;
            }}
            .weather-panel .forecast .day .wind {{
                font-size: 14px;
            }}
            .weather-panel .forecast .day .icon {{
                width: 50px;
                height: 50px;
                position: absolute;
                right: 20px;
                top: 20px;
            }}
            
        </style>
    </head>
    <body>

        <div class="main">
            <div class="weather-panel">

                <div class="header">
                    <div class="city">{city}</div>
                    <div class="temperature">{temperature}</div>
                    <div class="description">{description}</div>
                    <div class="humidity">Humidity: {humidity}</div>
                </div>

                <div class="forecast">
                    <div class="day">
                        <div class="title">Day 1</div>
                        <div class="info">  
                            <div class="temperature">Temperature: {temperature}</div>
                            <div class="description">Description: {description}</div>
                            <div class="humidity">Humidity: {humidity}</div>

                        </div>

                    </div>
                    <div class="day">
                        <div class="title">Day 2</div>
                        <div class="info">
                            <div class="temperature">Temperature: {temperature}</div>
                            <div class="description">Description: {description}</div>
                            <div class="humidity">Humidity: {humidity}</div>

                        </div>

                    </div>
                      <div class="day">
                        <div class="title">Day 3</div>
                        <div class="info">
                            <div class="temperature">Temperature: {temperature}</div>
                            <div class="description">Description: {description}</div>
                            <div class="humidity">Humidity: {humidity}</div>

                        </div>

                    </div>

                      <div class="day">
                        <div class="title">Day 5</div>
                        <div class="info">
                            <div class="temperature">Temperature: {temperature}</div>
                            <div class="description">Description: {description}</div>
                            <div class="humidity">Humidity: {humidity}</div>

                        </div>

                    </div>

                      <div class="day">
                        <div class="title">Day 5</div>
                        <div class="info">
                            <div class="temperature">Temperature: {temperature}</div>
                            <div class="description">Description: {description}</div>
                            <div class="humidity">Humidity: {humidity}</div>

                        </div>

                    </div>

                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_content
#write a code to get html content from openweathermap.org
def save_html(html_content):
    with open("index.html", "w") as fp:
        fp.write(html_content)
#write a code to get html content from openweathermap.org
def main():
    city = "Mumbai"
    current_weather = None
    forecast = None
    html_content = generate_html(current_weather, forecast)
    save_html(html_content)
#write a code to get html content from openweathermap.org
if __name__ == "__main__":
    #take cityname from user
    city_name = input("Enter city name: ")
    current_weather_data, forecast_data = get_weather(city_name)
    html_content = generate_html(current_weather_data, forecast_data)
    save_html(html_content)
#print that html file is generated

    if current_weather_data and forecast_data:
        generate_html(current_weather_data, forecast_data)
        print("HTML file 'index.html' generated.")
    




       












































# import requests
# import json

# API_KEY = "17d59437ed32af4dce8429118c2d9b5d"  # Replace with your OpenWeatherMap API key

# def get_weather(city):
#     current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
#     response_current = requests.get(current_weather_url)
#     response_forecast = requests.get(forecast_url)

#     if response_current.status_code == 200 and response_forecast.status_code == 200:
#         current_weather_data = json.loads(response_current.text)
#         forecast_data = json.loads(response_forecast.text)
#         return current_weather_data, forecast_data
#     else:
#         print(f"Error: {response_current.status_code} - {response_forecast.status_code}")
#         return None, None

# def generate_html(current_weather, forecast):
#     if current_weather is None or forecast is None:
#         return

#     city = current_weather['name']
#     temperature = current_weather['main']['temp']
#     humidity = current_weather['main']['humidity']
#     description = current_weather['weather'][0]['description']

#     html_content = f'''
#     <html>
#     <head>
#         <style>
#             body {{
#                 font-family: Arial, sans-serif;
#                 width: 100vw;
#                 height: 1000vh;
#                 background-image: url('clear.jpg');
#                 background-repeat: no-repeat;
#                 background-size: cover;
#                 background-position: center;

#             }}
#             h1 {{
#                 color: red;
#             }}
#             .weather-card {{
#                 border: 1px solid #ccc;
#                 border-radius: 5px;
#                 padding: 20px;
#                 margin-bottom: 20px;
                
#             }}
#             .weather-card .title {{
#                 font-size: 24px;
#                 font-weight: bold;
#                 margin-bottom: 10px;
#                 color: red;
#             }}
#             .weather-card .info {{
#                 font-size: 16px;
#                 color: red;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="weather-card">
#             <h1>Current Weather Forecast for {city}</h1>
#             <div class="title">Temperature</div>
#             <div class="info">{temperature}°F</div>
#             <div class="title">Humidity</div>
#             <div class="info">{humidity}%</div>
#             <div class="title">Description</div>
#             <div class="info">{description}</div>
#         </div>
#         <div class="weather-card">
#             <h1>Forecasted Weather for the Next 5 Days in {city}</h1>
#     '''

#     for forecast_item in forecast['list']:
#         forecast_date = forecast_item['dt_txt']
#         forecast_temperature = forecast_item['main']['temp']
#         forecast_humidity = forecast_item['main']['humidity']
#         forecast_description = forecast_item['weather'][0]['description']

#         html_content += f'''
#         <div class="title">Date</div>
#         <div class="info">{forecast_date}</div>
#         <div class="title">Temperature</div>
#         <div class="info">{forecast_temperature}°F</div>
#         <div class="title">Humidity</div>
#         <div class="info">{forecast_humidity}%</div>
#         <div class="title">Description</div>
#         <div class="info">{forecast_description}</div>
#         <br>
#         '''

#     html_content += '''
#         </div>
#     </body>
#     </html>
#     '''

#     with open('weather_forecast.html', 'w') as file:
#         file.write(html_content)

# if __name__ == "__main__":
#     city_name = input("Enter city name: ")
#     current_weather_data, forecast_data = get_weather(city_name)

#     if current_weather_data and forecast_data:
#         generate_html(current_weather_data, forecast_data)
#         print("HTML file 'weather_forecast.html' generated.")
