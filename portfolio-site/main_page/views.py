from django.shortcuts import render
import datetime
current_year = datetime.datetime.now().year
years_working = current_year - 2017

# Create your views here.
context_dict = {
    "name":"Marcos Garcia Vega",
    "short_bio": "A Finance Analyst who enjoys coding.",
    "short_bio2":"",
    "banner_title":"About Me",
    "banner_summary":f"Over {years_working} years of work experience.",
    "banner_text":"Hello there, I'm Marcos! I'm a finance analyst and have been exposed to roles in finance, operations and pricing. I've been programming since 2019 when I started learning Python online. I really enjoy data analysis, data visualization, and presenting on the data I analyze.",
    "banner_text2":"This site was created using Python + Django. I used the template Read Only by HTML5 UP. Check out html5up.net for other templates!",
    "section_1":"Short Summary",
    "section_2":"Skills",
    "section_2_text":"My roles have involved me using several tools and skills. Here's a quick summary of the skills I've picked up:",
    "section_2_a":"SQL",
    "section_2_b":"Python",
    "section_2_c": "Presenting to Leadership",
    "section_2_d": "Microsoft Office",
    "section_2_e": "Tableau Data Visualizations",
    "section_2_f": "Data Analysis",
    "section_3":"Work History",
    "section_3_text":f"With {years_working} years working, I've been exposed to many roles and experiences. Here are some highlights of my work experience:",
    "section_3_a":"Current role: DLP® Finance Analyst at Texas Instruments",
    "section_3_a_2":"In my current role, I own the P&L forecast process for 3 product lines in DLP® that produce ~$1B of revenue annually. I track $50M of yearly R&D spend and present our financials to senior leadership to provide insight on our business performance. I've worked on several projects including a project to create a dashboard to visualize revenue, gross margin, and sales trends using SQL, Python and TIBCO Spotfire®.",
    "section_3_b":"Data Science Fellowship at Data Science For All (Oct 2021 - Apr 2022)",
    "section_3_b_2":"In 2021, I was selected to participate in a data science fellowship that trained us on data analysis, visualizations, A/B testing, statistical modeling, and several other data science concepts using real world cases. Tools and skills we learned include Python, SQL, Tableau, Github, working with a team of five, and project management. My group at DS4A created a project that analyzed current obesity trends to understand what factors impact obesity.",
    "section_3_c":"Finance and Operations Rotations at Texas Instruments (Jan 2017 - July 2020)",
    "section_3_c_2":"I started my career at Texas Instruments in their finance and operations rotation program. I rotated through 3 roles in 3 years learning about TI's manufacturing process, supply chain and the pricing of TI's products. During this time, I was exposed to working with leadership to forecast our manufacturing spend, working with product line managers to understand supply chain gaps, and working with sales to win market share for TI. It was in the rotation program that I learned many of my skills, including Excel, SQL, and presenting to leadership",
    "section_4":"Contact Me",
    "section_4_a":"Want to get in contact with me? Send me an email!",
    "year":str(datetime.datetime.now().year)
}

def index(request):
    return render(request, "main_page/index.html", context=context_dict)
