# This script contains functions that processes and format data from modules.json, converting it to table data

#!/usr/bin/env python3

from decimal import Decimal
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

def calculate_semester_total(current_sem_modules):
    list_of_sem_grade_points = []
    list_of_sem_credit_units = []
    for module in current_sem_modules:
        grade = module["grade"]
        if grade in grade_to_points:
            list_of_sem_grade_points.append(grade_to_points[grade])
            list_of_sem_credit_units.append(module["credit_unit"])
    total_sem_grade_points = sum(list_of_sem_grade_points)
    total_sem_credit_units = sum(list_of_sem_credit_units)
    semester_gpa = total_sem_grade_points / total_sem_credit_units
    return semester_gpa, total_sem_credit_units

# Take note returned value is a tuple consisting of semester gpa and total credit units of str type


def calculate_cumulative_total(list_of_semester_totals):
    cumulative_total_grade_points = 0
    cumulative_total_credits = 0
    for semester in list_of_semester_totals:
        cumulative_total_grade_points += semester[0] * semester[1]
        cumulative_total_credits += semester[1]
    cummulative_gpa = round(cumulative_total_grade_points / cumulative_total_credits, 2)
    return cummulative_gpa, cumulative_total_credits

# Take note returned value is a tuple consisting of cumulative gpa and total credit units of str type  


def generate_table_data(current_sem_modules):
    pass


sem = load_modules("semesters_data.json")
sems = [calculate_semester_total(module["modules"]) for module in sem]
print(calculate_cumulative_total(sems))