country_capitals={"USA" : "Washington, D.C.", "France" : "Paris", "Germany" : "Berlin", "Japan" : "Tokyo", "UK" : "London"}

user_key=input("Enter the country: ")
if user_key in country_capitals:
    print(f"The capital of {user_key} is {country_capitals[user_key]}")
else:
    print("Capital not found.")





