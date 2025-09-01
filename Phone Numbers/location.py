import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+917294536271")
phone_number2 = phonenumbers.parse("+918878586271") 
phone_number3 = phonenumbers.parse("+94740294439")
phone_number4 = phonenumbers.parse("+201234567890")


print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));

# LETS TRACK PHONE NUMBERS
