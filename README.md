# 📊 GPA Report Generator

A Python-based project designed to process JSON files containing module, grade and student information and generate a professional PDF report of your curriculum and GPA.

## 🌟 Features

- 🔄 **Accurate GPA Calculation**: Seamlessly calculates your GPA based on the provided JSON file.
- 📄 **Professional PDF Report**: Generates a detailed PDF report summarizing your academic progress.
- ✉️ **Email Functionality**: Sends the generated PDF report to a specified email address using SMTP, allowing you to conveniently share or access your results.
- ✅ **Unit Testing**: Ensures the accuracy of GPA and credit calculations with robust unit tests implemented using Python's unittest module.

## 🚀 Getting Started

Follow these steps to set up and run the project:

### 1️⃣ Prerequisites

Ensure you have the following installed:

- 🐍 Python 3.7 or higher
- 📦 Required Python libraries (install via `requirements.txt`)

### 2️⃣ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/IteratorInnovator/generate-gpa-report.git
cd generate-gpa-report
pip install -r requirements.txt
python3 main.py
```
 ### Notes

Ensure that your curriculum data follows the semester_data.json file. 
If you would like to keep the email functionality, do create a .env file that stores the sender's email and app password, and the recipient email(s).

