Feel free to use any language you're comfortable in. 

**Hospital waiting room**

Our hospital has two rooms, the waiting room, where people wait to be triaged, and the emergency department. There are only **four beds** in the emergency department (it's a small hospital). The Triage nurse decides whether someone in the waiting room goes in to the emergency department, or if they are actually well enough to go home and see their doctor on Monday. If a person goes to the emergency department, they only stay there for **10 minutes**, which is how long it takes for a doctor to either treat them and send them home, or to admit them to the hospital.

Your job is to implement the triage nurse. They sit between the waiting room and the emergency department, and they decide if a person gets sent home straight away or if the person needs to be admitted to the emergency department. A person has a 'severity' rating between 1 and 10 that indicates how severe their condition is. The triage nurse will only admit somebody to the emergency department if their **severity rating is 4 or higher.** A person **can only be admitted if there is a bed available**, otherwise they have to wait, however a person that doesn't need to be admitted is sent away as soon as they present. If there are multiple people waiting, the person with the **highest severity rating is admitted first**.

Here are some scenarios that you should test. You should assume that the emergency department is empty at the start of the scenario. The scenario is complete when the emergency department is empty and there are no people in the waiting room.

1. Four people present to the triage nurse. Their severity ratings are 6, 3, 5 and 1.

2. Six people present to the triage nurse. Their severity ratings are 7, 3, 8, 6, 6 and 5.

3. Five people present to the triage nurse. Their severity ratings are 7, 6, 2, 7, and 6. Then after five minutes two more people present to the triage nurse, with severity ratings of 6 and 9.

4. Three people present to the triage nurse, with severity ratings of 6, 3 and 7. After five minutes three more people present, with severity ratings of 7, 8, and 4.

5. Three people present to the triage nurse, with severity ratings of 8, 6 and 4. After five minutes four more people present, with severity ratings of 7, 4, 2 and 8. After another seven minutes five more people present, with severity ratings of 7, 3, 5, 8, and 2.