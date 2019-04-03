
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

def filter_patients (waitingroom) :
    for patient in waitingroom.copy() :
        if patient["severity"] < 4 :
            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            print(f"Patient {patient_id} with a severity of {patient_severity} has been sent home")
            waitingroom.remove(patient)

def admitpatient(waitingroom, beds, time) :
    sorted_waitingroom = sorted(waitingroom, key=lambda k: k['severity'])

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
            print(f"Admitted patient {patient_id} with a severity of {patient_severity} at 00:00:{patient_admit_time}")

def bedtracker(beds, time) :
    for patient in beds.copy() :
        if time - patient["admit_patient_time"] >= 10 :
            admit_patient_id = patient["admit_patient_id"]
            admit_patient_time = patient["admit_patient_time"]

            print(f"Patient {admit_patient_id} has vacated bed as of 00:00:{time}")
            beds.remove(patient)

def scenario(scenario_list) :
    print("Welcome to ")
    time = 0
    waitingroom = scenario_list.copy()
    beds = []

    while hospitalstatus(waitingroom, beds) :

        filter_patients(waitingroom)
        admitpatient(waitingroom, beds, time)
        bedtracker(beds, time)

        time += 1
        if time > 100:
            break

    print("\nHospital has closed")

def startup() :
    Greeting.greeting()
    print("Press enter to begin the scenario, or Q to quit.")
    if input() == "q" :
        exit()
    else :
        scenario(ScenarioData.scenario1)






startup()