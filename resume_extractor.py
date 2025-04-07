import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Test the function with a sample PDF
resume_path = r"C:/Users/rvmut/desktop/Resume_Analyzer/sample_resume.pdf"  # Change this to your actual resume file path
resume_text = extract_text_from_pdf(resume_path)

print("Extracted Resume Text:")
print(resume_text[:1000])  # Print only the first 1000 characters to check

import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces and newlines
    text = re.sub(r'[^a-zA-Z0-9@. ]', '', text)  # Remove special characters
    return text.strip()

# Example Usage
raw_text = "John Doe\n\n Email: johndoe@gmail.com\nPhone: 123-456-7890\n"
cleaned_text = clean_text(raw_text)
print(cleaned_text)

import re

def extract_name(text):
    lines = text.split("\n")
    return lines[0] if lines else None  # Assuming the name is the first line

def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_phone(text):
    phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{2,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{4}"
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None

# Example text (use the text from your extracted resume)
resume_text = "John Doe\njohndoe@example.com\n+1 234-567-8901\nSkills: Python, Machine Learning"

# Extracting information
name = extract_name(resume_text)
email = extract_email(resume_text)
phone = extract_phone(resume_text)

# Display extracted information
print("Name:", name)
print("Email:", email)
print("Phone:", phone)

import re

# Sample skillset (You can modify this as per your need)
skills_list = [
    "Python", "Machine Learning", "Deep Learning", "NLP", "Data Science",
    "TensorFlow", "PyTorch", "Excel", "SQL", "Java", "C++", "JavaScript"
]

def extract_skills(text, skills_list):
    extracted_skills = []
    for skill in skills_list:
        if re.search(rf"\b{skill}\b", text, re.IGNORECASE):
            extracted_skills.append(skill)
    return extracted_skills

# Example resume text (Replace with your extracted resume text)
resume_text = """John Doe
johndoe@example.com
+1 234-567-8901
Skills: Python, Machine Learning, SQL, JavaScript, C++
"""

# Extract skills
skills = extract_skills(resume_text, skills_list)

# Display extracted skills
print("Extracted Skills:", skills)

import re

def extract_education(text):
    education_patterns = [
        r"(Bachelor|Master|PhD|B\.Tech|M\.Tech|BSc|MSc|MBA|BE|ME|Diploma)\s*[^,\n]*",
        r"(Computer Science|Information Technology|Mechanical Engineering|Electrical Engineering|Business Administration|Data Science)",
        r"\b(?:[12][09][0-9]{2})\b"  # Matches years like 2015, 2020, etc.
    ]
    
    extracted_education = []
    for pattern in education_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        extracted_education.extend(matches)
    
    return extracted_education

# Example resume text (Replace with actual extracted resume text)
resume_text = """John Doe
Email: johndoe@example.com
Phone: +1 234-567-8901
Education: 
Bachelor of Computer Science, XYZ University, 2020
Master of Data Science, ABC University, 2023
"""

# Extract education details
education = extract_education(resume_text)

# Display extracted education details
print("Extracted Education:", education)

import re

def extract_experience(text):
    experience_pattern = r"(?:\b(?:Software Engineer|Data Analyst|Project Manager|Intern|Researcher|Developer)\b)[^,\n]*"
    company_pattern = r"(?:at|in|for)\s+([A-Z][a-zA-Z0-9& ]+)"
    year_pattern = r"\b(19|20)\d{2}\b"  # Matches years like 2015, 2020, etc.

    job_titles = re.findall(experience_pattern, text, re.IGNORECASE)
    companies = re.findall(company_pattern, text)
    years = re.findall(year_pattern, text)

    return {"Job Titles": job_titles, "Companies": companies, "Years": years}

# Example resume text (Replace with actual extracted resume text)
resume_text = """John Doe
Email: johndoe@example.com
Phone: +1 234-567-8901
Experience: 
Software Engineer at Google from 2018 to 2022
Data Scientist at Microsoft 2022 - Present
"""

# Extract work experience
experience = extract_experience(resume_text)

# Display extracted work experience details
print("Extracted Experience:", experience)

# Print extracted details instead of saving to Excel
print("Extracted Resume Details:")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", ", ".join(skills))
print("Education:", ", ".join(education))
print("Experience:", ", ".join(experience['Job Titles']))
print("Companies:", ", ".join(experience['Companies']))
print("Years:", ", ".join(experience['Years']))
