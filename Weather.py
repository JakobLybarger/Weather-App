# Python program to find current weather

import requests
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


def get_weather(find_city):
    # get name of city to check weather
    city = find_city

    # The api key
    api_key = "e2ec846df8e223f8a179d7f1d197048d"

    # url to retrieve data
    url = "http://api.openweathermap.org/data/2.5/weather?q="

    data = []

    try:
        data.append(city)

        # concatenating final url, requesting and getting json file
        final_url = url + city + "&appid=" + api_key
        response = requests.get(final_url)
        x = response.json()

        # The state of the weather (ex: clear, cloudy, rain)
        weather = x["weather"][0]["description"]
        data.append(weather)

        # The humidity of the area
        humidity = x["main"]["humidity"]
        data.append(humidity)

        # The current temperature. Retrieved in kelvin
        # and converted to fahrenheit
        temp_kelvin = x["main"]["temp"]
        temp_fahrenheit = (temp_kelvin - 273.15) * (9 / 5) + 32
        data.append(temp_fahrenheit)

        # The real feel temperature in kelvin and
        # converted to fahrenheit
        real_feel_kelvin = x["main"]["feels_like"]
        real_feel_fahrenheit = (real_feel_kelvin - 273.15) * (9 / 5) + 32
        data.append(real_feel_fahrenheit)

        # The daily high in kelvin and converted
        # to fahrenheit
        daily_high_kelvin = x["main"]["temp_max"]
        daily_high_fahrenheit = (daily_high_kelvin - 273.15) * (9 / 5) + 32
        data.append(daily_high_fahrenheit)

        # The daily low in kelvin and converted
        # to fahrenheit
        daily_low_kelvin = x["main"]["temp_min"]
        daily_low_fahrenheit = (daily_low_kelvin - 273.15) * (9 / 5) + 32
        data.append(daily_low_fahrenheit)

        #print("===================================")
        #print(
         #   "\nCondition: %s\nHumidity: %d\n\nCurrent Temp: %.1f°F\nReal Feel: %.1f°F\n\nLow: %.1f°F\nHigh: %.1f°F\n" %
          #  (weather, humidity, temp_fahrenheit, real_feel_fahrenheit, daily_low_fahrenheit, daily_high_fahrenheit))
        #print("===================================")

        return data

    except KeyError:
        pass

    return data


# main screen. asks user to input city
class FindWeatherWindow(Screen):
    city = ObjectProperty(None)

    def find_weather(self):
        weather_data = get_weather(self.city.text)
        show_popup(weather_data)

class MyLabel(Label):
    pass


class MyApp(App):
    def build(self):
        return FindWeatherWindow()


def show_popup(data):
    # The popup which will show on the screen
    popup = Popup(title=data[0] + " Weather", title_align="center", title_size=25, size_hint=(None, None), size=(400, 400))
    # Grid layout on which all the labels will appear
    layout = GridLayout(rows=7)
    # All the labels that will be in the grid
    popup_label1 = MyLabel(text="City: " + data[0], font_size=25, text_size=popup.size)
    popup_label2 = MyLabel(text="Condition: " + data[1], font_size=25, text_size=popup.size)
    popup_label3 = MyLabel(text="Humidity: " + str(data[2]), font_size=25, text_size=popup.size)
    popup_label4 = MyLabel(text="Current Temperature: " + str(int(data[3])), font_size=25, text_size=popup.size)
    popup_label5 = MyLabel(text="Feels Like: " + str(int(data[4])), font_size=25, text_size=popup.size)
    popup_label6 = MyLabel(text="High: " + str(int(data[5])), font_size=25, text_size=popup.size)
    popup_label7 = MyLabel(text="Low: " + str(int(data[6])), font_size=25, text_size=popup.size)

    # The adding of each label tot he grid
    #layout.add_widget(popup_label1)
    layout.add_widget(popup_label2)
    layout.add_widget(popup_label3)
    layout.add_widget(popup_label4)
    layout.add_widget(popup_label5)
    layout.add_widget(popup_label6)
    layout.add_widget(popup_label7)

    # Adding the GridLayout to the popup
    popup.content = layout
    # Opening the popup
    popup.open()


def invalid_city():
    popup = Popup(title="Error",text="Invalid city... Please try again", size_hint=(None, None), size=(200, 200))
    popup.open()


if __name__ == '__main__':
    MyApp().run()
