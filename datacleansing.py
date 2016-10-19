# coding: utf-8

import numpy as np
import pandas as pd

# read in file
data = pd.read_excel('graduate_data.xlsx')

# change headings
data.columns = ['SID',
'Cohort',
'Year',
'Gender',
'Home Country',
'Home Country Region',
'Residency Status',
'Degree',
'Degree Level',
'Detailed level Group 1',
'Detailed level Group 2',
'Major 1',
'Major 2',
'Major 3',
'No. Majors',
'Employment status at completion',
'FT Job Title',
'FT Job Title (Simp.)',
'FT Employer',
'FT Employer (Simp.)',
'FT Country',
'FT Employer Size',
'FT Industry',
'FT Salary',
'FT Length',
'Current - Working PT/ Casual',
'Current - Seeking FT',
'Current - Seeking PT',
'Current - Studying further',
'Current - Not working',
'Current - Other',
'Current - Other (detail)',
'Graduate role',
'Grad Role Source',
'Grad Role Source - Other (specify)',
'Grad Role Source - All',
'Years of FT exp',
'Use CEO?',
'Receive CEO Newsletter?',
'IPP',
'IPP - Preparation',
'IPP - Skills',
'Degree - Preparation',
'Future Research Participation?',
'Testimonial',
'Alumni - Newsletter',
'Alumni - Presentations',
'Alumni - Research',
'Alumni - Forums',
'Alumni - Online Networking',
'Alumni - Reunions',
'Alumni - Cultural/ Sporting Events',
'Alumni - Mentor',
'Alumni - Mentee',
'Alumni - Mentoring activities',
'Alumni - Volunteering',
'Alumni - Career',
'Alumni - Prof. Networking',
'Alumni - Other',
'Alumni - Other 2',
'Alumni Pub - AusChina',
'Alumni Pub - Balanced Enterprise',
'Alumni Pub - Big Data',
'Alumni Pub - Business Health',
'Alumni Pub - Digital Disruption',
'Alumni Pub - Emerging Market Internationalisation',
'Alumni Pub - GFA',
'Alumni Pub - Innovation',
'Alumni Pub - Leadership',
'Alumni Pub - Poverty',
'Alumni Pub - Other',
'Alumni Pub - Other 2',
'LinkedIn',
'Other comments',
'Member - No',
'Member - ACS',
'Member - AHRI',
'Member - AMI',
'Member - CPA',
'Member - EA',
'Member - FINSIA',
'Member - ICAA',
'Member - Other',
'Member - Other 2',]


filter_alumni = [col for col in list(data) if col.startswith('Alumni -')]
filter_alumni_pub = [col for col in list(data) if col.startswith('Alumni Pub')]
filter_member = [col for col in list(data) if col.startswith('Member')]
filter_binary = filter_alumni + filter_alumni_pub + filter_member

# if data is not null, fill with 1
data[filter_binary] = data[filter_binary].applymap(lambda x: x if pd.isnull(x) else 1)
# if data is null, fill with 0
data[filter_binary]=data[filter_binary].fillna(0)

data.to_csv('datacorps_cleaned.csv')
