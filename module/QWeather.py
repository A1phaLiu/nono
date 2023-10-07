import requests
from geopy.geocoders import Nominatim

# 和风天气 nono-weather
KEY = 'a72aac38582149a2940283e65ad48a7f'    


def get_lookup_id(location):
    '''
    通过 lookup API 获取城市的 LocationID

    Parameters:
    - location: String, 需要查询地区的名称，支持文字、以英文逗号分隔的经度,\
                纬度坐标（十进制，最多支持小数点后两位）、LocationID或Adcode（仅限中国城市）。\
                例如 location=北京 或 location=116.41,39.92
    
    return:
    - String, LocationID
    '''
    url = f'https://geoapi.qweather.com/v2/city/lookup?location={location}&key={KEY}'
    response = requests.get(url).json()

    LocationID = response['location'][0]['id']
    return LocationID


def get_weather_now(location):
    '''
    获取城市的实时天气

    Parameters:
    - location: String, 需要查询地区的名称，支持文字、以英文逗号分隔的经度,\
                纬度坐标（十进制，最多支持小数点后两位）、LocationID或Adcode（仅限中国城市）。\
                例如 location=北京 或 location=116.41,39.92
    
    return:
    - json, 天气信息 https://dev.qweather.com/docs/api/weather/weather-now/
    '''
    LocationID = get_lookup_id(location)
    url = f'https://devapi.qweather.com/v7/weather/now?location={LocationID}&key={KEY}'

    response = requests.get(url).json()

    # 判断状态码
    code = response['code']
    if code == '200':
        return response
    else:
        return False    



def get_public_ip():
    response = requests.get("https://api.ipify.org/?format=text")
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "无法获取公共 IP 地址"



def get_address_from_ip(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}?lang=zh_CN')
    if response.status_code == 200:
        print(response.json())
    else:
        return "无法通过 IP 获取地址"
    


if __name__ == '__main__':
    get_address_from_ip(get_public_ip())