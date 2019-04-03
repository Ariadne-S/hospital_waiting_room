
"""
Key Points

4 Beds - patients stay in bed for 10 minutes
severity must be 4 or higher to be admitted
Otherwise sent home

If there are multiple people waiting then the person with the highest severity is admitted first
"""

import Greeting

scenario1 = [
    {"patient_id": "a", "severity":6, "arrival_time": 0},
    {"patient_id": "b", "severity":3, "arrival_time": 0},
    {"patient_id": "c", "severity":5, "arrival_time": 0},
    {"patient_id": "d", "severity":1, "arrival_time": 0},
]

scenario2 = [
    {"patient_id": "e", "severity":7, "arrival_time": 0},
    {"patient_id": "f", "severity":3, "arrival_time": 0},
    {"patient_id": "g", "severity":8, "arrival_time": 0},
    {"patient_id": "h", "severity":6, "arrival_time": 0},
    {"patient_id": "i", "severity":6, "arrival_time": 0},
    {"patient_id": "j", "severity":5, "arrival_time": 0},
    ]


scenario3 = [
    {"patient_id": "k", "severity":7, "arrival_time": 0},
    {"patient_id": "l", "severity":6, "arrival_time": 0},
    {"patient_id": "m", "severity":2, "arrival_time": 0},
    {"patient_id": "n", "severity":7, "arrival_time": 0},
    {"patient_id": "o", "severity":6, "arrival_time": 0},
    {"patient_id": "p", "severity":6, "arrival_time": 5},
    {"patient_id": "q", "severity":9, "arrival_time": 5},
    ]

scenario4 = [
    {"patient_id": "r", "severity":6, "arrival_time": 0},
    {"patient_id": "s", "severity":3, "arrival_time": 0},
    {"patient_id": "t", "severity":7, "arrival_time": 0},
    {"patient_id": "u", "severity":7, "arrival_time": 5},
    {"patient_id": "v", "severity":8, "arrival_time": 5},
    {"patient_id": "w", "severity":4, "arrival_time": 5},
    ]

scenario5 = [
    {"patient_id": "x", "severity":8, "arrival_time": 0},
    {"patient_id": "y", "severity":6, "arrival_time": 0},
    {"patient_id": "z", "severity":4, "arrival_time": 0},
    {"patient_id": "aa", "severity":7, "arrival_time": 5},
    {"patient_id": "ab", "severity":4, "arrival_time": 5},
    {"patient_id": "ac", "severity":2, "arrival_time": 5},
    {"patient_id": "ad", "severity":8, "arrival_time": 5},
    {"patient_id": "ae", "severity":7, "arrival_time": 12},
    {"patient_id": "af", "severity":3, "arrival_time": 12},
    {"patient_id": "ag", "severity":5, "arrival_time": 12},
    {"patient_id": "ah", "severity":8, "arrival_time": 12},
    {"patient_id": "ai", "severity":2, "arrival_time": 12},
    ]


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
    print("Hello World")
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




def startup() :
    Greeting.greeting()
    print("Press enter to begin the scenario, or Q to quit.")
    if input() == "q" :
        exit()
    else :
        scenario(scenario1)






startup()