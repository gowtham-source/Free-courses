import streamlit as st
import streamlit.components.v1 as components
from st_functions import st_button, load_css
from PIL import Image
import base64

st.set_page_config(page_title='Gowtham M')


def redirect(url):
    html = f'<a href="{url}" target="_blank"></a>'
    components.html(html, height=1)


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("5397807.jpg")


def button(label, url, iconsize):
    button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    st.markdown(button_code,
                unsafe_allow_html=True,
                )


page_bg = f'''
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
}}

</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")
st.write("[![Instagram](https://img.shields.io/badge/Instagram-%40Gowtham-orange?logo=instagram)](https://www.instagram.com/mystical_boy_25/)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('my.png'))

st.header('Gowtham M, B Tech Ai & Ds✨')

st.info('"This page is intended for students who are seeking free courses and internships, as well as access to a variety of free educational resources."')
col4, col5, col6, col7 = st.columns(4)
with col4:
    st_button('instagram', 'https://www.instagram.com/mystical_boy_25/',
              'Follow me on', 22)
with col5:
    st_button('github', 'https://github.com/gowtham-source',
              'For projects', 22)
with col6:
    st_button('linkedin', 'https://www.linkedin.com/in/gowtham-m-956363205/',
              'check out My', 22)
with col7:
    st_button('cup', 'https://www.buymeacoffee.com/GowthamM',
              'Buy a Coffee', 22)
icon_size = 20
# st.info(
#     "Get ready to level up your programming skills! CodeNight offers daily coding challenges to help students sharpen their skills and tackle complex problems with confidence. Join the challenge today!")

# button("CodeNight", '')
st.write("### Free Internships")
button('Forage - Virtual Internships (200+ Self-Paced Internship)',
       'https://www.theforage.com/course-catalog', 22)
button('AICTE - GOOGLE SUPPORTED VIRTUAL INTERNSHIP',
       'https://internship.aicte-india.org/internship-details.php?uid=INTERNSHIP_1654499134629da73e88342&level=4', 22)
button('AICTE - IBM SKILLSBUILD INTERNSHIP CAMP - CLOUD COMPUTING',
       'https://internship.aicte-india.org/internship-details.php?uid=INTERNSHIP_165847255262da486823908&level=4', 22)
button('AICTE - IBM INTERNSHIP - ARTIFICIAL INTELLIGENCE & MACHINE LEARNING',
       'https://internship.aicte-india.org/internship-details.php?uid=INTERNSHIP_166003801862f22b826becb&level=4', 22)
button('AICTE - GOOGLE SUPPORTED VIRTUAL INTERNSHIP PROGRAM',
       "https://internship.aicte-india.org/internship-details.php?uid=INTERNSHIP_1654499134629da73e88342&level=4", 22)
button('MICROSOFT - Software Engineering Internship',
       "https://careers.microsoft.com/students/us/en/job/1132567/Software-Engineering-Full-time-Opportunities-for-University-Graduates", 22)
button('MICROSOFT - Computer Vision/Machine Learning (3-6 months)',
       "https://careers.microsoft.com/students/us/en/job/1521322/Internship-opportunities-Computer-Vision-Machine-Learning-3-6-months", 22)
button('NIT - Online Summer Internship',
       'https://www.nitt.edu/home/other/jobs/Call_for_Summer_Internship_NITT-MAR_2022.pdf', 22)
button('Internshala - Analytics 📉',
       'https://internshala.com/internship/detail/analytics-work-from-home-job-internship-at-cleartax1678794610', 22)


image = (Image.open('course-ban.png'))
st.image(image)
st.write("### Free Courses")

button('Coursera', "https://docs.google.com/document/d/1UzEQcFOU8WiS6zYjpy2CLFnKFkyp_ZsTlh3YQHcb_JQ/edit?usp=sharing", 22)
button('Great Learning', "https://www.mygreatlearning.com/academy", 22)
button('Linkedin Learning + Microsoft',
       "https://opportunity.linkedin.com/skills-for-in-demand-jobs", 22)
button('kaggle', 'https://www.kaggle.com/learn', 22)
button('Udemy', "https://www.udemy.com/courses/search/?src=ukw&q=free", 22)
button("Jovian - python & ML/DL", "https://jovian.com/learn", 22)
button("aws - Skill builder",
       "https://explore.skillbuilder.aws/learn?dt=sec&sec=fdt", 22)
button("Google - Digital Marketing",
       "https://learndigital.withgoogle.com/digitalgarage/courses", 22)

image1 = (Image.open('youtube.jpg'))
st.image(image1)
st.write("### Best Youtube Channels for Coding")
st_button('youtube',
          'https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', 'FreeCodeCamp🔥', 22)
st_button('youtube', 'https://www.youtube.com/@codebasics', 'CodeBasics👩‍💻', 22)
st_button('youtube', 'https://www.youtube.com/@2d3dai', '2d3d.ai🤖', 22)
st_button('youtube', 'https://www.youtube.com/@krishnaik06', 'KrishNaik⭐', 22)
st_button('youtube', 'https://www.youtube.com/@javascriptmastery',
          'Javascript Mastery🕸️', 22)
st_button('youtube', 'https://www.youtube.com/@sentdex', 'Sentdex😎', 22)
st_button('youtube', 'https://www.youtube.com/@TheCoderCoder', 'Coder Coder👧', 22)
st_button('youtube', 'https://www.youtube.com/channel/UC5DNytAJ6_FISueUfzZCVsw',
          'Code with Ania Kubów👩', 22)
st_button('youtube', 'https://www.youtube.com/@Fireship', 'Fireship🔥', 22)
st_button('youtube', 'https://www.youtube.com/@derekbanas', 'Derek Banas🍌', 22)
st_button('youtube', 'https://www.youtube.com/@NetNinja', 'The Net Ninja🥷', 22)
st_button('youtube', 'https://www.youtube.com/@programmingwithmosh',
          'Programming with Mosh👨‍🦲', 22)

# st_button('medium', 'https://data-professor.medium.com/',
#           'Read my Blogs', icon_size)
# st_button('twitter', 'https://twitter.com/thedataprof/',
#           'Follow me on Twitter', icon_size)
# st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/',
#           'Follow me on LinkedIn', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/',
#           'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/',
#           'Buy me a Coffee', icon_size)
