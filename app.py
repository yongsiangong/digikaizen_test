import os
import openai
import streamlit as st

st.header("DIGIKAIZEN")
st.write("Ask digikaizengpt any questions regarding our company and services!")
qn = st.text_input("Your question:")
if qn:
    os.environ["OPENAI_API_KEY"] = st.secrets.API
    openai.api_key = os.environ["OPENAI_API_KEY"]

    prompt_template = f"""
    You are now a customer service officer providing information for people who wish to use our service at Digikaizen.
    Do not provide any information that is irrelevant to the context. Keep the replies in bullet points if possible.
    Say 'I do not know' if you cannot find the answers. Do not make up any information.
    Keep your replies friendly.
    \n\nRelevant context: 
    WHY JOIN A DIGITAL MARKETING COURSE
    1. 94% Internet usage in Japan
    2. 81% Social Media Users in Japan
    Google is still the major search engine worldwide Digital Marketing is growing exponentially in Japan and businesses can no longer ignore it.
    If you are:
    1. A business owner looking to explore this domain
    2. Someone looking to switch careers into the IT Sector
    3. A fresh graduate looking for working in Digital Marketing
    Join our digital marketing courses, both online and offline, and start your journey now!
    Practical. Relevant. Fun!
    Our Courses
    1. SEO is a marathon.
    2. Google Paid Ads are a sprint. 
    3. Link both on Google Analytics
    Student Testimonials
    1. Pan W.Y.: Christopher is my Capstone mentor for a Digital Sales and Marketing course that I took with BCG. He is earnest and down-to-earth, and will try his very best to answer all the queries my team members and I have. During the process, he will also share his real-life experience in relation to digital sales and marketing. Christopher is very strong in Google SEO and SEM, ask him any questions in relation to that and he will try his very best to explain to the students.
    2. Tan S.M.: Christopher is a very detailed and passionate lecturer. His lessons have been engaging, useful, and he was very patient with everyone. His knowledge of digital and social media marketing was immensely helpful for our final capstone project. Most importantly, I also managed to apply what I have learnt into real world. I would highly recommend Christopher to anyone interested in digital marketing course.
    3. Choy A.: Christopher Puan was one of our lecturers and coach during my Digital Sales & Marketing course with Boston Consulting Group. Chris is a knowledgeable and passionate trainer, and his dedication to coaching us has resulted in our digital group project receiving Top Award and the digital strategies being considered by the client. 
    Also training at:
    1. Lithan Academy Pte Ltd
    2. Firstcom Academy Pte Ltd
    3. BCG RISE
    4. Emarsity Pte Ltd
    About Us
    The pandemic hit hard.
    Our founder, Chris Puan, lost his work in Japan and was forced to return to Singapore.
    This is not a sob story, but a story of rebirth.
    Embodying digital transformation and improvement (hence digital KaiZen), through up-skilling and transferring his current skills to new domains, he was able to use his past experience as a corporate trainer in a digital marketing agency and English teacher in Japan to shift into the Digital Marketing implementation and training sector.
    Following his personal experience in re-skilling and making a career switch, Chris started Digikaizen in Fukuoka so that we can address the shortfall of bilingual IT individuals, by providing:
    1. digital skills training in English
    2. customised English lessons to the company or industry
    Trainer's experience
    1. More than 200 courses taught in Japan and Singapore
    2. More than 1000 learners taught
    3. Honour's Degree from National University of Singapore
    4. Diploma in Digital Marketing from Lithan Academy
    5. Advanced Certificate in Learning and Performance from IAL Singapore
    6. Diploma in Design and Development of Learning for Performance from IAL Singapore
    7. MBA from Quantic School of Technology
    8. Final round candidate of CEO Audition JP
    9. Visa Sponsored by Fukuoka City Government
    Digikaizen's Core Values
    1. Equal opportunities for all: We recognise that not everyone will be financially able to pay for up-skilling. Please contact us regarding instalment based payment.
    2. Non Discrimination: Regardless of your race, religion, gender or sexual orientation, we treat everyone fairly and with manners.
    Courses offered:
    1. Google Search Engine Optimisation (launch in August 2023)
    - Your problem: Just started a website but nobody can find it? Don't know what is clogging up your website and making it slow and annoying?
    - Solution: Find out about SEO and how we can improve the website's health. Create content and get quality backlinks in order to get a better Search Engine Ranking Position (SERP) Learn about this here.
    digikaizen google SEM course. 
    2. Google Search Engine Marketing | Paid Ads (SEM)
    - Your problem: Can't get traction? You need to get the word out on your company fast? Your competitor's ads are constantly on top of the search results and you want to compete?
    - Solution: Use Google Ads to run brand awareness campaigns and follow up with re-targeting campaigns for conversion. Don't know how to? Join our course here.
    3. Google Analytics (launch in August 2023)
    - Your problems: Are you running your business on gut feeling? No idea what's wrong with your website or what visitors are doing on your website?
    - Solution: Google Analytics allows you to see where visitors are coming from, what they are doing, where they are dropping out and how they are converting or making a purchase.
    Process of signing up:
    - Contact us using the form on our Contact page
    - Register with your details
    - Make payment using bank transfer or Paypay
    - Turn up for lesson at Coworking Space Q
    - Learn and have fun!
    Digikaizen. Re-launch!
    It has been an eventful year from 2022 August to 2023 May since we moved from Singapore to Fukuoka, Japan.
    While we have built a good base in Singapore, we have decided to bring the Singapore Skillsfuture training system to Japan. The Skillsfuture style of training focuses on practical know how rather than theory.
    Digikaizen's courses, starting with the Digital Marketing domain, will therefore focus on practice and actual use in businesses.
    Examples of activities in courses include running of Google Campaigns, editing of websites to improve SEO, usage of tools like Chat GPT to assist with content creation and the report creation on Google Analytics.
    We have already secured a client in Yokohama (a Swiss Company!) with regular on-site and online lessons, focusing on English training with sales and marketing content supplementation.
    Digikaizen will continue to provide quality, practical but fun courses for the adult learner.
    It's a promise.
    Regards, 
    Chris Puan
    Fukuoka, Japan Office | Classroom
    Co-Working Space Q
    Email: chris.puan@digikaizen.org
    Directions:
    We're located in basement 1 of Hakata station.
    Take the escalator from the Hakata Airport Subway Line.
    Go up and find Peace Valley Street.
    Go down the corridor and find Coworking Space Q, we are part of the community.
    \n\nThe customer's question: {qn}"""

    gpt35_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_template},
        ],
        temperature=0,
    )
    st.subheader("digikanzengpt:")
    st.write(gpt35_response.choices[0]["message"]["content"])