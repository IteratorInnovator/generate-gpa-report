import unittest
import process_data as pd

class UnitTest_process_data(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    def test_calculate_semester_total(self):
        testcases = [[
            {
                "module": "Computational Thinking and Programming",
                "grade": "A-",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Computational Fundamentals",
                "grade": "B+",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Writing and Reasoning",
                "grade": "B+",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Economics and Society",
                "grade": "B+",
                "credit_unit": "1.0",
                "status": "Completed"
            }
        ], 
        [
            {
                "module": "Algorithms and Programming",
                "grade": "A",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Data Management",
                "grade": "A-",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Web Application Development I",
                "grade": "B+",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Big Questions - Happiness and Suffering",
                "grade": "B+",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Introduction to Statistics",
                "grade": "A-",
                "credit_unit": "1.0",
                "status": "Completed"
            },
        ],
        [
            {
                "module": "Enterprise Solution Development",
                "grade": "C-",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Enterprise Solution Management",
                "grade": "D+",
                "credit_unit": "1.0",
                "status": "Completed"
            },
            {
                "module": "Web Application Development II",
                "grade": "B-",
                "credit_unit": "1.0",
                "status": "Completed"
            }
        ],
        [
            {
                "module": "Management Communication",
                "grade": "C+",
                "credit_unit": "0.5",
                "status": "Completed"
            },
            {
                "module": "Software Project Management",
                "grade": "B",
                "credit_unit": "2.0",
                "status": "Completed"
            },
            {
                "module": "Object-Oriented Programming",
                "grade": "A+",
                "credit_unit": "1.5",
                "status": "Completed"
            }
        ],
        [
            
        ]]
        self.assertEqual(pd.calculate_semester_total(testcases[0]), (3.4, 4.0)) # Basic testcase
        self.assertEqual(pd.calculate_semester_total(testcases[1]), (3.6, 5.0)) # Basic testcase
        self.assertEqual(pd.calculate_semester_total(testcases[2]), (1.9, 3.0)) # Lower grade range testcase
        self.assertEqual(pd.calculate_semester_total(testcases[3]), (2.4, 4.0)) # Varying credit unit testcase
        self.assertEqual(pd.calculate_semester_total(testcases[4]), (0.0, 0.0)) # Zero modules testcase
    def test_calculate_cumulative_total(self):
        testcases = [
            [ (3.4, 4.0) ],
            [ (2.7, 5.0), (4.3, 4.0), (3.58, 5.0) ],
            [ (3.6, 4.0), (3.7, 4.0), (3.66, 5.0), (4.06, 5.0), (2.75, 4.0) ],
            []
        ]
        self.assertEqual(pd.calculate_cumulative_total(testcases[0]), (3.4, 4.0)) # 1 semester testcase
        self.assertEqual(pd.calculate_cumulative_total(testcases[1]), (3.47, 14.0)) # Mulitple semesters testcase
        self.assertEqual(pd.calculate_cumulative_total(testcases[2]), (3.58, 22.0)) # Multiple semesters testcase
        self.assertEqual(pd.calculate_cumulative_total(testcases[3]), (0.0, 0.0)) # Zero semester testcase


if __name__ == "__main__":
    unittest.main()