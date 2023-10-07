def choose_clothing(temperature):
    clothing_suggestions = {
        (40, float('inf')): "停止户外作业，对老弱病幼人群采取保护措施",
        (35, 39): "天气闷热，适宜夏季服装",
        (25, 34): "天气热，适宜夏季轻薄服装",
        (18, 24): "天气温和，适宜春秋过渡装",
        (10, 17): "天气凉爽，适宜春秋服装",
        (-float('inf'), 9): "天气寒冷，建议穿温暖的冬季服装"
    }

    for temperature_range, suggestion in clothing_suggestions.items():
        if temperature >= temperature_range[0] and temperature <= temperature_range[1]:
            return suggestion

    return "无穿着建议"



if __name__ == '__main__':
    temperature = 25
    suggestion = choose_clothing(temperature)
    print(suggestion)