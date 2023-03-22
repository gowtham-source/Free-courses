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


def lightbutton(label, url, iconsize):
    button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                </svg>  
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
st.markdown("---")
icon_size = 20
st.write("##### --- NEW LAUNCH✨ ---")
st.info(
    "Get ready to level up your programming skills! CodeNight offers daily coding challenges to help students sharpen their skills and tackle complex problems with confidence. Join the challenge today! Click the below link... (A spcl launch by us! still in progress⚠️)")
button("CodeNight🌙", 'https://codenight.streamlit.app/', 22)
st.markdown("---")
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
button('Intro to Software Engineering(Cisco & Foorage)',
       'https://www.theforage.com/virtual-internships/prototype/kinDTvjiZRcYbwqLo/Intro-to-Software-Engineering', 22)
button('Advanced Software Engineering Virtual Experience (Walmart💚)',
       'https://www.theforage.com/virtual-internships/prototype/oX6f9BbCL9kJDJzfg/Advanced%20Software%20Engineering?ref=JZMAPpFQz7gLhKGLm&forceFastTrackV2=true', 22)
button('TCS & Forage - ESG',
       'https://www.theforage.com/virtual-internships/prototype/N8Muuhk6XsXgMTeu2/ESG?new=null', 22)
button('Suven Technologies-6+ internships',
       'https://internship.suvenconsultants.com/s/store', 22)
button('Cognizant - Artificial Intelligence',
       'https://www.theforage.com/virtual-internships/prototype/5N2ygyhzMWjKQmgCK/Cognizant-Artificial-Intelligence-Virtual-Experience-Program', 22)
st.write("### Internships with stipend💸")
button('Internshala - Analytics 📉',
       'https://internshala.com/internship/detail/analytics-work-from-home-job-internship-at-cleartax1678794610', 22)
button('indeed', 'https://in.indeed.com/q-free-internship-l-chennai,-tamil-nadu-jobs.html?vjk=8f8483643f5ffc08', 22)
button('Simply Hired', 'https://www.simplyhired.co.in/search?q=free+internship&l=chennai%2C+tamil+nadu&job=3WeyMWBedSQOuvurNEDs0zb7DHbMxDD3lriTATqfUAkB2d76NE74Lw', 22)
button('code-bind Technologies',
       'https://codebindtechnologies.com/free-internship-in-chennai/', 22)


image = (Image.open('course-ban.png'))
st.image(image)
st.write("### Free Courses")
button('Coursera📘', "https://docs.google.com/document/d/1UzEQcFOU8WiS6zYjpy2CLFnKFkyp_ZsTlh3YQHcb_JQ/edit?usp=sharing", 22)
button('Great Learning', "https://www.mygreatlearning.com/academy", 22)
button("INfosys Springboard♨️",
       "https://infyspringboard.onwingspan.com/web/en/page/home", 22)
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


file_ = open("content.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<center><img src="data:image/gif;base64,{data_url}" alt="cat gif"></center><br>',
    unsafe_allow_html=True,
)
st.write("### Tutorials")
tab1, tab2, tab3 = st.tabs(
    ["Web Developement", "Machine Learning", "Datascience"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        lightbutton('1) Simple Roadmap', 'https://youtu.be/ysEN5RaKOlA', 22)
        lightbutton('3) Full Stack', 'https://youtu.be/nu_pCVPKzTk', 22)


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
