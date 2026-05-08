temperature = int(input("Enter current temperature: "))
previous_action = "OFF"
if temperature < 20:
    if previous_action != "ON":
        action = "Heater ON"
    else:
        action = previous_action

elif temperature > 25:
    if previous_action != "OFF":
        action = "Heater OFF"
    else:
        action = previous_action
else:
    action = "No change"
print("Action:", action)