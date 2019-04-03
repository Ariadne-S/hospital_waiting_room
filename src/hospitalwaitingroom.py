
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

def scenario(scenario_list) :
    print("Hello World")
    time = 0
    waitingroom = scenario_list.copy()
    beds = []

    while hospitalstatus(waitingroom, beds):

        print(time)

        for patient in waitingroom :
            if patient["severity"] < 4 :
                patient_id = patient["patient_id"]
                patient_severity = patient["severity"]
                print(f"Patient {patient_id} with a severity of {patient_severity} has been sent home")
                waitingroom.remove(patient)






        #if time > 300:
        time += 1
        break




def startup() :
    Greeting.greeting()
    print("Press enter to begin the scenario, or Q to quit.")
    if input() == "q" :
        exit()
    else :
        scenario(scenario1)






startup()