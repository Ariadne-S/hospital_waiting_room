import ScenarioData
import Greeting

def create_new_scenario(scenario_choice) :
    print("\nThank you for choosing to create a new scenario")
    print("To begin, please type your scenario's name...")
    scenario_name = input()
    print("Follow the prompts to add your first patient")
    patient_arrivals = []
    add_new_patient(patient_arrivals)
    run_or_select_option(-1, patient_arrivals, scenario_name)

def add_new_patient(patient_arrivals) :
    patient_count = len(patient_arrivals) + 1
    patient_id = get_patient_id(patient_count)
    severity = get_patient_severity(patient_count)
    arrival_time = get_patient_arrival_time(patient_count)
    patient = {"patient_id": patient_id, "severity":severity, "arrival_time": arrival_time}
    patient_arrivals.append(patient)
    new_patient_option(patient_arrivals)

def get_patient_id(patient_count):
    print(f"{patient_count}.1:\tWhat is the id or name for this patient?")
    name_input = input()
    return name_input

def get_patient_severity(patient_count):
    print(f"{patient_count}.2:\tWhat is the patient's severity? [1 - 10]")
    severity_input = input()
    try:
        severity_input_int = int(severity_input)
        if severity_input_int in range(1,11) :
            return severity_input_int
        else:
            print("Your input must be a number bewteen 1 and 10, please try again.")
            return get_patient_severity(patient_count)
    except:
        print("Your input must be a number bewteen 1 and 10, please try again.")
        return get_patient_severity(patient_count)

def get_patient_arrival_time(patient_count):
    print(f"{patient_count}.3:\tWhat time does this patient arrive? [0 - 1440]")
    arrival_time_input = input()
    try:
        arrival_time_input_int = int(arrival_time_input)
        if arrival_time_input_int in range(0,1441) :
            return arrival_time_input_int
        else:
            print("Your input must be a number bewteen 1 and 1440, please try again.")
            return get_patient_arrival_time(patient_count)
    except:
        print("Your input must be a number +bewteen 1 and 1440, please try again.")
        return get_patient_arrival_time(patient_count)

def new_patient_option(patient_arrivals) :
    print("Do you want to add another patient? [Y/N]")
    selection = input().lower()
    if selection == "y" :
        add_new_patient(patient_arrivals)

def build_scenario(scenario_name, patient_arrivals) :
    scenario_dict = {"name": scenario_name, "arrivals": patient_arrivals}
    ScenarioData.scenario_choice.append(scenario_dict)

def run_or_select_option(senario_index, patient_arrivals, scenario_name) :
    print("What would you like to do next?\n\tA:\tAdd another patient\n\tR:\tRun scenario\n\tE:\tExit to main menu?")
    selection = input().lower()
    if selection == "r" :
        build_scenario(scenario_name, patient_arrivals)
        Greeting.start_run_scenario(senario_index)
    elif selection == "a":
        add_new_patient(patient_arrivals)
        run_or_select_option(senario_index, patient_arrivals, scenario_name)
    elif selection == "e":
        build_scenario(scenario_name, patient_arrivals)
        Greeting.select_scenario()
    elif selection == "q" :
        quit()
    else:
        print("The selection you have made is not valid. Please try again.")
        run_or_select_option(senario_index, patient_arrivals, scenario_name)
