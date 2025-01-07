# This script contains functions that processes and format data from modules.json, converting it to table data

#!/usr/bin/env python3

import json

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


def calculate_semester_total(current_sem_modules):
    list_of_sem_grade_points = []
    list_of_sem_credit_units = []
    for module in current_sem_modules:
        grade = module["grade"]
        if grade in grade_to_points:
            list_of_sem_grade_points.append(grade_to_points[grade])
            list_of_sem_credit_units.append(float(module["credit_unit"]))
    total_sem_grade_points = sum(list_of_sem_grade_points)
    total_sem_credit_units = sum(list_of_sem_credit_units)
    semester_gpa = total_sem_grade_points / total_sem_credit_units
    return semester_gpa, total_sem_credit_units


def calculate_cumulative_total(list_of_semester_totals):
    cumulative_total_grade_points = 0
    cumulative_total_credits = 0
    for semester in list_of_semester_totals: 
        cumulative_total_grade_points += semester[0] * semester[1]
        cumulative_total_credits += semester[1]
    cummulative_gpa = round(cumulative_total_grade_points / cumulative_total_credits, 2)
    return cummulative_gpa, cumulative_total_credits


def generate_table_data(current_sem_modules):
    keys = ["module","grade","credit_unit","status"]
    table_data = [list(module[key] for key in keys) for module in current_sem_modules]
    table_data.insert(0,["Course","Grade","Credit Unit(s) Earned","Status"])
    return table_data



sem = load_modules("semesters_data.json")
# print(sem)
# print(calculate_cumulative_total([calculate_semester_total(sem[0]["modules"])]))
print(generate_table_data(sem[0]["modules"]))