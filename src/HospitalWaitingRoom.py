
import ScenarioData

def hospital_open(pending_patients, waitingroom, beds) :
    return len(pending_patients) + len(waitingroom) + len(beds) != 0

def new_output_dict(time, action, p_id, severity) :
    return {"time": time, "action": action, "patient_id":p_id, "severity": severity}

def new_hospital_action_dict(time, p_id, severity) :
    return {"action_time": time, "patient_id":p_id, "severity": severity}

def patient_arrives (scenario_list, time, waitingroom, output) :
    scenario_patients = scenario_list.copy()
    for patient in scenario_patients:
        if patient["arrival_time"] == time :
            arrived_patient = new_hospital_action_dict(time, patient["patient_id"], patient["severity"])
            output_dict = new_output_dict(time, "Arrived", patient["patient_id"], patient["severity"])
            waitingroom.append(arrived_patient)
            output.append(output_dict)
            scenario_list.remove(patient)

def filter_patients (waitingroom, time, output) :
    for patient in waitingroom.copy() :
        if patient["severity"] < 4 :
            output_dict = new_output_dict(time, "Sent Home", patient["patient_id"], patient["severity"])
            output.append(output_dict)
            waitingroom.remove(patient)

def admit_patient(waitingroom, beds, time, output) :
    sorted_waitingroom = sorted(waitingroom, key=lambda k: k['severity'], reverse=True)

    for patient in sorted_waitingroom :
        if beds == None or len(beds) < 4 :
            admit_patient = new_hospital_action_dict(time, patient["patient_id"], patient["severity"])
            output_dict = new_output_dict(time, "Admitted", patient["patient_id"], patient["severity"])
            beds.append(admit_patient)
            output.append(output_dict)
            waitingroom.remove(patient)

def bed_tracker(beds, time, output) :
    if len(beds) > 0 :
        for patient in beds.copy() :
            if time - patient["action_time"] >= 10 :
                output_dict = new_output_dict(time, "Vacated", patient["patient_id"], patient["severity"])
                output.append(output_dict)
                beds.remove(patient)

def run_scenario(scenario_list) :
    time = 0
    pending_patients = scenario_list.copy()
    beds = []
    waitingroom = []
    output = []

    patient_arrives(pending_patients, 0, waitingroom, output)

    while hospital_open(pending_patients, waitingroom, beds) :
        filter_patients(waitingroom, time, output)
        bed_tracker(beds, time, output)
        admit_patient(waitingroom, beds, time, output)

        time += 1
        patient_arrives(pending_patients, time, waitingroom, output)
    return output
