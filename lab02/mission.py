# Jamaal Dockery - CIS-109 - Lab 02

agent_name = input("Enter your agent name: ")
age = int(input("Enter your age: "))
training_years = int(input("How many years have you been training? "))
favorite_color = input("Enter your favorite color: ")
gadgets = int(input("How many gadgets are you carrying? "))
minutes = int(input("How many minutes do you have? "))

training_percentage = (training_years / age) * 100
gadget_density = gadgets / training_years
mission_seconds = minutes * 60
mission_time_remaining = minutes - 7

mission_code = (agent_name).upper() + "-" + favorite_color.upper() + "-" + str(age)
is_adult = age >= 18
has_many_gadgets = gadgets >= 5
has_training_experience = training_years > 0

print("Agent:", agent_name)
print("Mission Code:", mission_code)

print("Age:", age)
print("Training:", training_years, "years")
print(f"Training Percentage: {training_percentage:.2f}%")

print("Gadgets:", gadgets)
print(f"Gadget Density: {gadget_density:.2f} per training year")

print("Mission Time:", minutes, "minutes")
print("Mission Time Remaining:", mission_time_remaining, "minutes")
print("Mission Time in Seconds:", mission_seconds)

print("Adult Agent:", is_adult)
print("Many Gadgets:", has_many_gadgets)
print("Training Experience:", has_training_experience)