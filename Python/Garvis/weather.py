from noaa_sdk import NOAA
n = NOAA()
res = n.get_forecasts('11365', 'US', type='forecastGridData')
print(res)