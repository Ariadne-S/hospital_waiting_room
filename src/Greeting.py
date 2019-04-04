import datetime
import getpass
import ScenarioData
import HospitalWaitingRoom

def dayportion(datetime) :
  hour = datetime.hour
  if hour < 12 :
    return "Good morning"
  elif hour >= 12 and hour < 16 :
    return "Good afternoon"
  else:
    return "Good evening"

def greeting() :
  welcome = dayportion(datetime.datetime.now())
  user = getpass.getuser().title()
  print(f"{welcome} {user}.")
  print()

def select_scenario() :
    print("Please input the corresponding key to enter a Scenario, or Q to quit.")
    for key, _ in ScenarioData.scenario_choice.items() :
        print(f"\t{key}:\tScenario {key}")

    selection = input()

    if selection == "q" :
        exit()
    elif int(selection) in ScenarioData.selection_options :
        scenario_data = ScenarioData.scenario_choice[int(selection)]
        print(f"\nWelcome to Scenario {selection}\n")
        output = HospitalWaitingRoom.run_scenario(scenario_data)
        print_hospital_activity(output)
        select_scenario()
    else :
        print("\nUnfortunately your selection was not valid, please try again.")
        select_scenario()

def startup() :
    greeting()
    select_scenario()

def print_hospital_activity(output) :
    for activity in output :
        time = activity["time"]
        action = activity["action"]
        patient_id = activity["patient_id"]
        severity = activity["severity"]
        description = "has" if (action == "Arrived" or action == "Vacated") else "has been"

        print(f"00:{time:02d}\t[{action}]\tPatient \"{patient_id}\" with a severity of {severity} {description} {action.lower()} ")
    print("\nHospital is closed\n")



startup()