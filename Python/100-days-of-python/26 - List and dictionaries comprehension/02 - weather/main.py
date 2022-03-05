from data import weather_c
print(weather_c)

def far_to_cel(temp):
    return temp * 9/5 + 32

c_data = {day:far_to_cel(weather_c[day]) for (day, temp) in weather_c.items()}

print(weather_c) # {'Monday': 12, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 21, 'Saturday': 22, 'Sunday': 24}
print(c_data)    # {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}


