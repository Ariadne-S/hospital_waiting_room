
"""
Key Points

4 Beds - patients stay in bed for 10 minutes
severity must be 4 or higher to be admitted
Otherwise sent home

If there are multiple people waiting then the person with the highest severity is admitted first
"""

import Greeting
import ScenarioData

def hospitalstatus(list1, list2) :
    #is the hospital closed or open
    return len(list1) + len(list2) != 0

def patientarrives (scenario_list, time, waitingroom) :
    scenario_patients = scenario_list.copy()
    for patient in scenario_patients:

        if patient["arrival_time"] == time :
            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            arrival_time = time
            arrived_patient = {"patient_id": patient_id, "severity": patient_severity, "arrival_time": arrival_time}
            print(f"Arrived: Patient {patient_id} has arrived with a severity of {patient_severity} at 00:00:{arrival_time}")
            waitingroom.append(arrived_patient)



def filter_patients (waitingroom) :
    for patient in waitingroom.copy() :
        if patient["severity"] < 4 :
            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            print(f"Deny: Patient {patient_id} with a severity of {patient_severity} has been sent home")
            waitingroom.remove(patient)

def admitpatient(waitingroom, beds, time) :
    sorted_waitingroom = sorted(waitingroom, key=lambda k: k['severity'], reverse=True)

    for patient in sorted_waitingroom :
        if beds == None or len(beds) < 4 :

            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            patient_admit_time = time

            admit_patient = {
                "admit_patient_id": patient_id,
                "admit_patient_severity": patient_severity,
                "admit_patient_time": patient_admit_time
            }

            beds.append(admit_patient)
            waitingroom.remove(patient)
            print(f"Admit: Admitted patient {patient_id} with a severity of {patient_severity} at 00:00:{patient_admit_time}")

def bedtracker(beds, time) :
    while len(beds) > 0 :
        for patient in beds.copy() :
            if time - patient["admit_patient_time"] >= 10 :
                admit_patient_id = patient["admit_patient_id"]

                print(f"Vacate: Patient {admit_patient_id} has vacated bed as of 00:00:{time}")
                beds.remove(patient)

def scenario(scenario_list) :
    time = 0
    scenario_patients = scenario_list.copy()
    beds = []
    waitingroom = []

    patientarrives (scenario_patients, 0, waitingroom)

    while hospitalstatus(waitingroom, beds) :
        filter_patients(waitingroom)
        bedtracker(beds, time)
        admitpatient(waitingroom, beds, time)

        time += 1
        patientarrives (scenario_patients, time, waitingroom)
        if time > 100:
            break

    print("\nHospital has closed\n")
    select_scenario()

def select_scenario() :
    print("Please input the corresponding key to enter a Scenario, or Q to quit.")
    for key, _ in ScenarioData.scenario_choice.items() :
        print(f"\t{key}:\tScenario {key}")

    selection = input()

    if selection == "q" :
        exit()
    elif int(selection) in ScenarioData.selection_options :
        scenariodata = ScenarioData.scenario_choice[int(selection)]
        print(f"\nWelcome to Scenario {selection}\n")
        scenario(scenariodata)
    else :
        print("\nUnfortunately your selection was not valid, please try again.")
        select_scenario()

def startup() :
    Greeting.greeting()
    select_scenario()





startup()