from ubidots import ApiClient
import random

#Create an API object
api = ApiClient("f4a44b0bbbfdc25207c5841ba91ada2c2bc9235c")

#Create Variable objects - Humidity and Temperature
humidity_value = api.get_variable("555a4777762542487814e5a6")
temperature_value = api.get_variable("555a47c07625424af45b924e")

#Create random values for testing
rand_humidity = random.randint(1,100)
rand_temperature = random.randint(29,120)

#Write the values to variables on Ubidots
humidity_value.save_value({'value':rand_humidity})
temperature_value.save_value({'value':rand_temperature})

