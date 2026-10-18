import pandas as pd

df = pd.read_csv("weather.csv")

print("weather Data:")
print(df)

print("\nAveragge Temperature")
print(df["temperature"].mean())

print("\nAverage Humidity:")
print(df["humidity"].mean())
    




