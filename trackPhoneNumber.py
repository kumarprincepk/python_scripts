import phonenumbers
from phonenumbers import timezone,carrier,geocoder
mob_num = input("Enter the Phone number for finding location and add +91 : ")
phoneNumber = phonenumbers.parse(mob_num)
time_zone = timezone.time_zones_for_geographical_number(phoneNumber)
carr_ier = carrier.name_for_number(phoneNumber, "en")
location = geocoder.description_for_number(phoneNumber, "en")
print(phoneNumber)
print(time_zone)
print(carr_ier)
print(location)