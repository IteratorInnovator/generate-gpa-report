from process_data import *
from generate_report import *
from reportlab.platypus import SimpleDocTemplate, KeepTogether
from reportlab.lib.pagesizes import letter
from email_report import *

def create_gpa_pdf_report():
    pdf_report = SimpleDocTemplate("GPA_report.pdf", pagesize=letter)
    elements = []
    elements.append(create_header()) # Title
    
    # Add student demographic section
    elements.append(create_student_info_section("student_info.json"))
    elements.append(create_line_divider())
    semesters = load_json("semesters_data.json")
    
    # Add individual semester sections
    cumulative_data = []
    for semester in semesters:
        semester_table_data = generate_table_data(semester["modules"])
        semester_total = calculate_semester_total(semester["modules"])
        cumulative_data.append(semester_total)
        elements.append(Spacer(1,20))
        semester_section = [
            create_semester_header(semester), # header
            Spacer(0.5, 10), 
            create_table(semester_table_data), # table
            Spacer(0.5, 10),
            create_total_summary(semester_total) # summary
        ]
        
        # Wraps the entire semester section (heading, table, etc.) into a single flowable block.
        # Ensures the section is not split across pages.
        # If there isn’t enough space on the current page, the entire block moves to the next page.
        semester_section = KeepTogether(semester_section)
        elements.append(semester_section)
    elements.extend([create_line_divider(),Spacer(1,20)])
    
    # Add cumulative summary section
    cumulative_total = calculate_cumulative_total(cumulative_data)
    cumulative_summary_section = [
        create_cumulative_summary(cumulative_total[0], cumulative_total[1], cumulative_total[2]),
        Spacer(1,20)
    ]
    cumulative_summary_section = KeepTogether(cumulative_summary_section)
    elements.append(cumulative_summary_section)
    
    # Build the pdf report
    pdf_report.build(elements)
    
    
if __name__ == "__main__":
    create_gpa_pdf_report()
    email_gpa_pdf_report("GPA_report.pdf")
    