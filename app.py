from pathlib import Path

import streamlit as st
from PIL import Image

#------Path Settings-----

current_dir = Path(__file__).parent if '__file__'in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'Hina Naz - Resume for Data Analyst.pdf'
#css_file = current_dir / 'styles' / 'main.css'

#----General Settings---

Page_Title = "Resume - Hina Naz"
Page_Icon = ':wave:'
Name = 'Hina Naz'
Description = """
Data Analyst and Visualizer | Web Developer
"""
email = 'hina.hrm87@gmail.com'
social_media = {
	'GitHub': 'https://github.com/hinanaz87',
	'LinkedIn': 'https://www.linkedin.com/in/hina-naz',
	'Facebook': 'https://www.facebook.com/WordPressDesignsbyHina',
}

projects = {
	'Employee Churn - ML App': 'https://employee-churn-app.streamlit.app/',
        'Machine Learning Spot Website': 'https://machinelearningspot.com/machine-learning-guide/',
	'ML News Website': 'https://mlnews.dev/',
	'React Ecommerce Website':'https://eccomerce-mg.netlify.app/',
	'Portfolio Website': 'https://portfolio-hina.netlify.app/',
	'IOTA-Clone': 'https://hinanaz5.github.io/IOTA-Clone/',
	'Resume Maker': 'https://hinanaz5.github.io/cv-maker/',
}

st.set_page_config(page_title = Page_Title, page_icon = Page_Icon)

#-----LOAD CSS, PDF and Profile Image----

with open(css_file) as f:
	st.markdown("<style>{}<style/>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
	PDFbyte = pdf_file.read()
#PDFbyte = Image.open(profile_pic)

#----- HERO SECTION---

col1, col2 = st.columns(2, gap = 'small')

#with col1:
	#st.image(profile_pic, width=230)

with col2:
	st.title(Name)
	st.write(Description)
	st.download_button(
		label='Download Resume',
		data=PDFbyte,
		file_name = resume_file.name,
		mime='application/octet-stream'
	)
	st.write('✉️ Contact me at: ',email)

#---SOCIAL LINKS---

#st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
	cols[index].write(f'[{platform}]({link})')

#----Qualification----

#st.write('#')
st.subheader('Qualification')
st.write(
"""
- **Masters in Public Administration** - University of Karachi
- **2010**
"""
)

#----Professional Certifications----

#st.write('#')
st.subheader('Certifications and Courses')
st.write(
"""
- ✔️ **Data Analyst** - Karachi AI
- ✔️ **Website Development** - Saylani Mass IT Training
- ✔️ **WordPress Development** - Digital Institute of Pakistan
"""
)

#----EXPERIENCE AND QUALIFICATION----

#st.write('#')
st.subheader('Work Experience')
st.write(
"""
- ✔️ **The Speed Train** - Web Developer and Website Maintenance
- ✔️ **Windoors Ventures** - Web Developer and Project Lead
"""
)

st.subheader ('Duties and Responsibilities:')
st.write(
"""
**Web Developer and Project Lead**
- ✔️ Developing and maintaining websites
- ✔️ Leading the Team
"""
)

#--- SKILLS---
st.subheader("Hard Skills")
st.write(
"""
**💻 Programming:**
- Python (Scikit-learn, Pandas, Matplotlib)
- SQL (DML)
- React

**📊 Data Visualization**
- Excel
- Power BI
- Matplotlib

** 📈 Statistical Analysis**
- Descriptive Analysis
- Inferential Statistics

**🧮 Modeling**
- Linear Regtression
- Logistic Regression
- Decision Tree
- Random Forest
- K-Means

""")

#--- Projects---
st.write("---")
st.subheader('Projects')
#st.write ('#')
#st.write("---")
for project, link in projects.items():
	st.write(f"[{project}]({link})")