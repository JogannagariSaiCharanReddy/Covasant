from flask import Flask,jsonify,request,Response,g
import random
from datetime import date
import datetime
import xml.etree.ElementTree as ET


app=Flask(__name__)

def get_next_10_days():
    td=date.today()
    return [(td + datetime.timedelta(days = day)).isoformat() for day in range(10)]

def get_forecast(today_date):
    codes={
    "23": ["Breezy", (25, 27), (17, 19)],
    "34": ["Mostly Sunny", (36, 38), (21, 22)],
    "28": ["Mostly Cloudy", (34, 36), (28, 29)],
    "30": ["Partly Cloudy", (32, 34), (28, 29)],
    "26": ["Cloudy", (36, 37), (28, 29)]
    }

    code=list(codes.keys())[random.randint(0,4)]
    text=codes[code][0]
    high=random.randint(*codes[code][1])
    low=random.randint(*codes[code][2])
    return dict(date=today_date,code=code,high=high,low=low,text=text)


def mock_weather_json(city):
    forecast=[get_forecast(today_date) for today_date in get_next_10_days()]
    template={ "query": {
  "count": 1,
  "created": "2025-04-21T04:49:55Z",
  "lang": "en-IN",
  "results": {
   "channel": {
    "units": {
     "distance": "mi",
     "pressure": "in",
     "speed": "mph",
     "temperature": "F"
    },
    "title": "Yahoo! Weather - mumbai, Unknown",
    "link": "http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2460286/",
    "description": "Yahoo! Weather for mumbai, Unknown",
    "language": "en-us",
    "lastBuildDate": "Mon, 21 Apr 2025 04:49 AM",
    "ttl": "60",
    "location": {
     "city": city,
     "country": "Unknown",
     "region": " Unknown"
    },
    "wind": {
     "chill": "3",
     "direction": "23",
     "speed": "22"
    },
    "atmosphere": {
     "humidity": "71",
     "pressure": "1007.0",
     "rising": "0",
     "visibility": "16.1"
    },
    "astronomy": {
     "sunrise": "7:6 am",
     "sunset": "10:56 pm"
    },
    "image": {
     "title": "Yahoo! Weather",
     "width": "142",
     "height": "18",
     "link": "http://weather.yahoo.com",
     "url": "http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif"
    },
    "item": {
     "title": f"Conditions for {city} , Unknown at 06:00 AM",
     "lat": "64.499474",
     "long": "-165.405792",
     "link": "http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2460286/",
     "pubDate": "Mon, 21 Apr 2025 04:49 AM",
     "condition": {
      "code": "31",
      "date": "Mon, 21 Apr 2025 04:49 AM",
      "temp": "17",
      "text": "Clear"
     }},
     "forecast":forecast
     }}}}
    
    return template
    



def mock_weather_xml(tag,data):
    tree=ET.Element(tag)
    
    for k,v in data.items():
        if type(v)==dict:
            tree.append(mock_weather_xml(k,v))
        elif type(v)==list:
            for i in v:
                tree.append(mock_weather_xml(k,i))
        else:
            ele=ET.Element(k)
            ele.text=str(v)
            
            tree.append(ele)
            
    print(tree)
    return tree
    
    


@app.route("/<string:city>", methods=['GET'])
@app.route("/<string:city>?<string:format>" ,methods=['GET'])
def weather(city:str,format:str="json"):
    if request.method=="GET":
        fcity = request.args.get('city', city)
        fformat = request.args.get('format', format)
        td=date.today()
        if fformat=="json":
            return mock_weather_json(city)
        elif fformat=="xml":
            return Response(ET.tostring(mock_weather_xml("resp",mock_weather_json(city))), content_type="application/xml")
        else:
            return "invalid format"
    
if __name__ == '__main__':
    app.run(debug=True)  
        
     
    
    