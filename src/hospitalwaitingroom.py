
"""
Key Points

4 Beds - patients stay in bed for 10 minutes
severity must be 4 or higher to be admitted
Otherwise sent home

If there are multiple people waiting then the person with the highest severity is admitted first
"""

import ScenarioData

def hospital_status(list1, list2) :
    #is the hospital closed or open
    return len(list1) + len(list2) != 0

def patient_arrives (scenario_list, time, waitingroom, output) :
    scenario_patients = scenario_list.copy()
    for patient in scenario_patients:

        if patient["arrival_time"] == time :
            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            arrival_time = time
            arrived_patient = {"patient_id": patient_id, "severity": patient_severity, "arrival_time": arrival_time}
            output_dict = {"time": arrival_time, "action": "Arrived", "patient_id":patient_id, "severity": patient_severity}
            print(f"00:{arrival_time:02d}\t[Arrive]\tPatient {patient_id} has arrived with a severity of {patient_severity}")
            waitingroom.append(arrived_patient)
            output.append(output_dict)

def filter_patients (waitingroom, time, output) :
    for patient in waitingroom.copy() :
        if patient["severity"] < 4 :
            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            time = time
            output_dict = {"time": time, "action": "Sent Home", "patient_id": patient_id, "severity": patient_severity}
            print(f"00:{time:02d}\t[Deny]\t\tPatient {patient_id} with a severity of {patient_severity} has been sent home")
            waitingroom.remove(patient)
            output.append(output_dict)

def admit_patient(waitingroom, beds, time, output) :
    sorted_waitingroom = sorted(waitingroom, key=lambda k: k['severity'], reverse=True)

    for patient in sorted_waitingroom :
        if beds == None or len(beds) < 4 :

            patient_id = patient["patient_id"]
            patient_severity = patient["severity"]
            patient_admit_time = time

            admit_patient = {"admit_patient_id": patient_id,"admit_patient_severity": patient_severity,"admit_patient_time": patient_admit_time}
            output_dict = {"time": patient_admit_time, "action": "Admitted", "patient_id": patient_id, "severity": patient_severity}

            beds.append(admit_patient)
            waitingroom.remove(patient)
            output.append(output_dict)
            print(f"00:{patient_admit_time:02d}\t[Admit]\t\tAdmitted patient {patient_id} with a severity of {patient_severity}")

def bed_tracker(beds, time, output) :
    if len(beds) > 0 :
        for patient in beds.copy() :
            if time - patient["admit_patient_time"] >= 10 :
                patient_id = patient["admit_patient_id"]
                patient_severity = patient["admit_patient_severity"]

                output_dict = {"time": time, "action": "Vacated", "patient_id": patient_id, "severity": patient_severity}

                print(f"00:{time:02d}\t[Vacate]\tPatient {patient_id} has vacated bed")
                beds.remove(patient)
                output.append(output_dict)

def run_scenario(scenario_list) :
    time = 0
    scenario_patients = scenario_list.copy()
    beds = []
    waitingroom = []
    output = []

    patient_arrives(scenario_patients, 0, waitingroom, output)

    while hospital_status(waitingroom, beds) :
        filter_patients(waitingroom, time, output)
        bed_tracker(beds, time, output)
        admit_patient(waitingroom, beds, time, output)

        time += 1
        patient_arrives(scenario_patients, time, waitingroom, output)
        if time > 100:
            break

    print("\nHospital has closed\n")

    return output
