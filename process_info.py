# This script contains functions that processes and format data from modules.json, converting it to table data

#!/usr/bin/env python3

import json
from reportlab.platypus import Table
from reportlab.pdfgen import canvas

grade_to_points = {
    "A+": 4.3,  # Highest grade
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0,  # Fail
}

def load_modules(json_file):
    with open(json_file,'r') as file:
        return json.load(file)

def calculate_semester_gpa(current_sem_modules):
    total_sem_grade_points = []
    total_sem_credit_units = []
    for module in current_sem_modules:
        grade = module["grade"]
        if grade in grade_to_points:
            total_sem_grade_points.append(grade_to_points[grade])
            total_sem_credit_units.append(module["credit_unit"])
    return sum(total_sem_grade_points) / sum(total_sem_credit_units)
    
def generate_table_data(current_sem_modules):
    pass

sem = load_modules("modules.json")
print(calculate_semester_gpa(sem[0]["modules"]))