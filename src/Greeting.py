import datetime
import getpass
import ScenarioData
import HospitalWaitingRoom
import CreateScenario

scenario_choice = ScenarioData.scenario_choice

def startup() :
    greeting()
    select_scenario()

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
    print("Please input the corresponding key to enter a scenario, or Q to quit.")
    options = len(scenario_choice)
    i = 1
    for scenario in scenario_choice:
        name = scenario["name"]
        print(f"\t{str(i)}:\t{name}")
        i += 1
    print("\tn:\tBuild you own scenario")
    selection = input().lower()

    if selection == "q" :
        exit()
    elif selection =="n":
        CreateScenario.create_new_scenario(scenario_choice)
    elif int(selection) in range(options + 1) :
        scenario_index = int(selection) - 1
        start_run_scenario(scenario_index)
    else :
        print("\nUnfortunately your selection was not valid, please try again.")
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

def start_run_scenario(scenario_index) :
    scenario_data = scenario_choice[scenario_index]["arrivals"]
    scenario_name = scenario_choice[scenario_index]["name"]
    print(f"\nWelcome to scenario: {scenario_name}\n")
    output = HospitalWaitingRoom.run_scenario(scenario_data)
    print_hospital_activity(output)
    select_scenario()


