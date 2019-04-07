import HospitalWaitingRoom
import ScenarioData

import unittest

class TestScenarios(unittest.TestCase) :


    def test_scenario1(self) :
        scenario_data = ScenarioData.scenario1["arrivals"]
        results = HospitalWaitingRoom.run_scenario(scenario_data)
        expectations = [
            {'time': 0, 'action': 'Arrived', 'patient_id': 'a', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'b', 'severity': 3},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'c', 'severity': 5},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'd', 'severity': 1},
            {'time': 0, 'action': 'Sent Home', 'patient_id': 'b', 'severity': 3},
            {'time': 0, 'action': 'Sent Home', 'patient_id': 'd', 'severity': 1},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'a', 'severity': 6},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'c', 'severity': 5},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'a', 'severity': 6},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'c', 'severity': 5}
        ]

        self.assertListEqual(results, expectations)

    def test_scenario2(self) :
        scenario_data = ScenarioData.scenario2["arrivals"]
        results = HospitalWaitingRoom.run_scenario(scenario_data)
        expectations = [
            {'time': 0, 'action': 'Arrived', 'patient_id': 'e', 'severity': 7},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'f', 'severity': 3},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'g', 'severity': 8},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'h', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'i', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'j', 'severity': 5},
            {'time': 0, 'action': 'Sent Home', 'patient_id': 'f', 'severity': 3},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'g', 'severity': 8},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'e', 'severity': 7},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'h', 'severity': 6},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'i', 'severity': 6},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'g', 'severity': 8},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'e', 'severity': 7},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'h', 'severity': 6},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'i', 'severity': 6},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'j', 'severity': 5},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'j', 'severity': 5},
        ]

        self.assertListEqual(results, expectations)

    def test_scenario3(self) :
        scenario_data = ScenarioData.scenario3["arrivals"]
        results = HospitalWaitingRoom.run_scenario(scenario_data)
        expectations = [
            {'time': 0, 'action': 'Arrived', 'patient_id': 'k', 'severity': 7},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'l', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'm', 'severity': 2},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'n', 'severity': 7},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'o', 'severity': 6},
            {'time': 0, 'action': 'Sent Home', 'patient_id': 'm', 'severity': 2},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'k', 'severity': 7},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'n', 'severity': 7},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'l', 'severity': 6},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'o', 'severity': 6},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'p', 'severity': 6},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'q', 'severity': 9},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'k', 'severity': 7},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'n', 'severity': 7},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'l', 'severity': 6},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'o', 'severity': 6},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'q', 'severity': 9},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'p', 'severity': 6},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'q', 'severity': 9},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'p', 'severity': 6},
        ]

        self.assertListEqual(results, expectations)

    def test_scenario4(self) :
        scenario_data = ScenarioData.scenario4["arrivals"]
        results = HospitalWaitingRoom.run_scenario(scenario_data)
        expectations = [
            {'time': 0, 'action': 'Arrived', 'patient_id': 'r', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 's', 'severity': 3},
            {'time': 0, 'action': 'Arrived', 'patient_id': 't', 'severity': 7},
            {'time': 0, 'action': 'Sent Home', 'patient_id': 's', 'severity': 3},
            {'time': 0, 'action': 'Admitted', 'patient_id': 't', 'severity': 7},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'r', 'severity': 6},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'u', 'severity': 7},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'v', 'severity': 8},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'w', 'severity': 4},
            {'time': 5, 'action': 'Admitted', 'patient_id': 'v', 'severity': 8},
            {'time': 5, 'action': 'Admitted', 'patient_id': 'u', 'severity': 7},
            {'time': 10, 'action': 'Vacated', 'patient_id': 't', 'severity': 7},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'r', 'severity': 6},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'w', 'severity': 4},
            {'time': 15, 'action': 'Vacated', 'patient_id': 'v', 'severity': 8},
            {'time': 15, 'action': 'Vacated', 'patient_id': 'u', 'severity': 7},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'w', 'severity': 4},
        ]

        self.assertListEqual(results, expectations)

    def test_scenario5(self) :
        scenario_data = ScenarioData.scenario5["arrivals"]
        results = HospitalWaitingRoom.run_scenario(scenario_data)
        expectations = [
            {'time': 0, 'action': 'Arrived', 'patient_id': 'x', 'severity': 8},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'y', 'severity': 6},
            {'time': 0, 'action': 'Arrived', 'patient_id': 'z', 'severity': 4},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'x', 'severity': 8},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'y', 'severity': 6},
            {'time': 0, 'action': 'Admitted', 'patient_id': 'z', 'severity': 4},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'aa', 'severity': 7},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'ab', 'severity': 4},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'ac', 'severity': 2},
            {'time': 5, 'action': 'Arrived', 'patient_id': 'ad', 'severity': 8},
            {'time': 5, 'action': 'Sent Home', 'patient_id': 'ac', 'severity': 2},
            {'time': 5, 'action': 'Admitted', 'patient_id': 'ad', 'severity': 8},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'x', 'severity': 8},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'y', 'severity': 6},
            {'time': 10, 'action': 'Vacated', 'patient_id': 'z', 'severity': 4},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'aa', 'severity': 7},
            {'time': 10, 'action': 'Admitted', 'patient_id': 'ab', 'severity': 4},
            {'time': 12, 'action': 'Arrived', 'patient_id': 'ae', 'severity': 7},
            {'time': 12, 'action': 'Arrived', 'patient_id': 'af', 'severity': 3},
            {'time': 12, 'action': 'Arrived', 'patient_id': 'ag', 'severity': 5},
            {'time': 12, 'action': 'Arrived', 'patient_id': 'ah', 'severity': 8},
            {'time': 12, 'action': 'Arrived', 'patient_id': 'ai', 'severity': 2},
            {'time': 12, 'action': 'Sent Home', 'patient_id': 'af', 'severity': 3},
            {'time': 12, 'action': 'Sent Home', 'patient_id': 'ai', 'severity': 2},
            {'time': 12, 'action': 'Admitted', 'patient_id': 'ah', 'severity': 8},
            {'time': 15, 'action': 'Vacated', 'patient_id': 'ad', 'severity': 8},
            {'time': 15, 'action': 'Admitted', 'patient_id': 'ae', 'severity': 7},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'aa', 'severity': 7},
            {'time': 20, 'action': 'Vacated', 'patient_id': 'ab', 'severity': 4},
            {'time': 20, 'action': 'Admitted', 'patient_id': 'ag', 'severity': 5},
            {'time': 22, 'action': 'Vacated', 'patient_id': 'ah', 'severity': 8},
            {'time': 25, 'action': 'Vacated', 'patient_id': 'ae', 'severity': 7},
            {'time': 30, 'action': 'Vacated', 'patient_id': 'ag', 'severity': 5},
        ]

        self.assertListEqual(results, expectations)

if __name__ == '__main__':
    unittest.main()