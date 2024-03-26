import streamlit as st
import pandas as pd

# PAGE SETTINGS
st.set_page_config(
  layout="centered", page_title="Portfolio Kristina Litau ", page_icon=":linked_paperclips:"
)
st.markdown("""
## Hello, welcome!
"""
)
col1, col2 = st.columns(2)
with col1:
  st.markdown("""
My name is Kristina Litau, I am a self-starting front-end developer and a life-time athlete based in Spokane, Washington.

As I'm in the early stage of a web development journey, I love learning about the front-end development, 
creating visually-appealing and user-friendly interfaces!

I have a strong technical background and passion for problem solving gained
through my Bachelor's in Industrial & Systems Engineering and 2 years of work with
data analysis and operations.

Constantly contributing to the community both at the university and in the city,
          I learned the importance of being an open-minded and curious person! If you'd like to talk more
here is my information to connect:

509-789-0848 | litaukk@gmail.com
 www.linkedin.com/in/kristina-litau/
  """
  )

  @st.cache_data
  def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_content = file.read()
    return pdf_content
  file_path = "Resume.pdf"
  resume = read_pdf(file_path)
  st.download_button("Download my Resume",data=resume,file_name='Kristina_Litau_Resume.pdf', mime=None)

with col2:
  st.image('profile_picture.jpeg', width=300)
st.divider()
st.header("My Projects")
st.markdown("""
  ### Open Gym Coordinating System - coming soon!
"""
)
st.markdown("""
  On a Friday night, everyone has one question: "Where are we going?"
  The same question pops up in mind of the Spokane volleyballer during the lively open gym session,
  where keeping up with the current court rotation is a hard thing to do.

  This website will help gym supervisors run volleyball open gyms smoothly,
  given the limited number of courts and time available, ensuring maximum plying and minimum sitting time for each team.
"""
)
st.divider()

st.markdown("""
  ### Tip-Tap Walking Tours
"""
)
col1, col2, col3, col4, col5  = st.columns(5)
col1.metric("HTML",'')
col2.metric("CSS",'')
col3.metric("JavaScript",'')
col4.metric("Bootstrap",'')
col5.metric("Google Maps API",'')
col1, col2 = st.columns(2)
with col1:
  st.markdown("""
      A responsive web application featuring my personal favorite coffee shops and walking tours for
              Spokane and Seattle.

      Built for people willing to go on the city crawl while traveling and/or working remotely,
      this platform offers walking self-tours with a well-connected mix of sightseeing spots,
      coffee shops, thrift stores, and other hidden gems. Each option comes with an approximate
              tour completion time and a bit of history for each location to enrich the experience!

      The tours feature is currently under development.
  """
  )
  st.markdown(
  """
  **Future implementations and iterations**:
   - perform rigorous and stress testing
   - more cities and place collections
   - SEO optimization
   - customization (build your own tours)
   - collaboration with influencers and businesses
   - moble app development
  """
  )
st.link_button("Tip-Tap website", "https://tip-tap.info")
st.link_button("GitHub page", "https://tip-tap.info")

with col2:
  st.image('tip-top-screenshot2.jpg', width=300)

st.divider()

  # Git and web site link
st.markdown("""
  ### User Interface for Amazon Transportation
"""
)
col1, col2, col3, col4  = st.columns(4)
col1.metric("Streamlit",'')
col2.metric("Python",'')
col3.metric("Data Vizualization",'')
col4.metric("UI Design",'')

col1, col2 = st.columns(2)
with col1:
  st.image('amazon-screenshot3.jpg', width=320)
with col2:
  st.markdown("""
    Working on the marketing segmentation model for Amazon Transportation as a capstone team, we
    quickly learned that the main user will have little to no technical background to interact with the raw Python code.

    To make life of the marketing and sales team easier, I built a user-friendly, functional web app that streamlines
    the back-end model outcomes to the data visuals and reports available for download.
  """
  )
