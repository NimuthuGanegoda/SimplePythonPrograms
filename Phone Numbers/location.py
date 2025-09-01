def show_details(phone_number):
	location = geocoder.description_for_number(phone_number, "en")
	country = phonenumbers.region_code_for_number(phone_number)
	timezones = timezone.time_zones_for_number(phone_number)
	provider = carrier.name_for_number(phone_number, "en")
	print(f"Number: {phone_number}")
	print(f"Country: {country}")
	print(f"Location (City/Region): {location}")
	print(f"Timezone(s): {', '.join(timezones)}")
	print(f"Carrier: {provider}")
	print("---------------------------")

if __name__ == "__main__":
	import phonenumbers
	from phonenumbers import geocoder, carrier, timezone
	print("\nPhone Number Location\n")
	numbers = input("Enter phone numbers separated by commas (with country code, e.g. +123456789): ").split(',')
	for num in numbers:
		num = num.strip()
		try:
			phone_number = phonenumbers.parse(num)
			show_details(phone_number)
		except Exception as e:
			print(f"Error parsing number {num}: {e}")
			print("---------------------------")

# LETS TRACK PHONE NUMBERS