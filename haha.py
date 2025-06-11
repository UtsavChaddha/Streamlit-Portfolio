import streamlit as st
from PIL import Image
import os  # Import the os module
import requests  # Import requests
from io import BytesIO

# --- Basic Setup ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded", # Keep sidebar open by default
)

# --- Custom CSS for a clean look ---
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        color: #333;
        background-color: #f4f4f4;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: #ecf0f1;
    }
    .st-emotion-cache-10pw50 div[data-testid="stVerticalBlock"] > div:first-child {
        padding-top: 2rem !important;
    }
    .st-emotion-cache-1w0pu67 {
        padding: 2rem 1rem !important;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stTabs div[data-testid="stVerticalBlock"]{
        gap: 0 !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #3498db;
        color: white;
    }
    .stTabs [data-baseweb="tab-list"] button {
        background-color: #ecf0f1;
        color: #2c3e50;
        border-bottom: none;
        border-radius: 8px 8px 0 0; /* Rounded corners for tabs */
        margin-right: 2px; /* Add space between tabs */
    }
     .stTabs [data-baseweb="tab-list"] button:hover {
        background-color: #bdc3c7; /* Light gray hover effect */
        color: #2c3e50;
    }
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid #ddd; /* Add a border below the tabs */
        padding-bottom: 0px;
        margin-bottom: 0px;
    }
    .st-expander {
        border: 1px solid #ddd;
        border-radius: 8px;
        margin-bottom: 10px;
        background-color: #ffffff;
    }
    .st-expander-header {
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
    }
    .st-expander-content {
        padding-top: 0;
    }
    #sidebar{
        width: 250px;
    }

    [data-testid="stVerticalBlock"]{
        width: 75%;
    }
    #menu-font {
        font-size: 24px;
    }
    .icon-link {
        display: inline-block;
        transition: transform 0.2s ease-in-out; /* Smooth transition */
    }
    .icon-link:hover {
        transform: scale(1.2); /* Enlarge on hover */
    }
    .sidebar-text-icon-container {
        display: flex;
        align-items: center; /* Vertically center icon and text */
        gap: 15px; /* Adjust the gap as needed */
        margin-bottom: 20px;
    }
    .sidebar-text-icon-container a {
        font-size: 18px; /* Increase font size of link text */
        color: #ecf0f1;  /* Keep the text color the same */
        text-decoration: none; /* Remove underline if you want */
    }
    .display-flex{
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 20px;
    }
    .header-text{
        font-size: 26px; /* Increased font size by 10% (24 * 1.1 = 26.4, rounded down) */
        font-weight: bold;
    }
    .bio-text{
        margin-top: 0px;
    }
    .profile-container {
        display: flex;
        align-items: flex-start; /* Changed to flex-start */
        gap: 20px; /* Adjust as needed for spacing between image and text */
        margin-bottom: 20px; /* Add some margin below the whole section */
    }
    .profile-text-container {
        flex: 1; /* Allows the text container to take up remaining space */
    }
    .skills-container {
        display: flex;
        gap: 20px; /* Adjust as needed for spacing between skill items */
        align-items: center; /* Vertically center items if needed */
    }
    .image-text-container { /* New class for image and text alignment */
        display: flex;
        align-items: center; /* Vertically align image and text */
        gap: 20px; /* Adjust spacing between image and text */
    }
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /* Responsive grid layout */
        gap: 20px; /* Adjust gap as needed */
        align-items: center; /* Vertically align items */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# --- Helper function for image display with caching ---
@st.cache_resource
def load_and_resize_image(image_path, width):
    """
    Loads an image from the given path, resizes it, and returns the image object.
    Caches the result to improve performance.
    """
    try:
        # Check if the image path is a URL or a local file
        if image_path.startswith("http://") or image_path.startswith("https://"):
            # It's a URL, Streamlit can handle it directly
            response = requests.get(image_path)
            img = Image.open(BytesIO(response.content))
        else:
            # If it's a local file, check if it exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Error: Image not found at {image_path}")
            img = Image.open(image_path)  # open image
        img = img.resize((width, int(img.height * (width / img.width))))
        return img
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}. Please make sure the image file exists and the path is correct.  The file should be in the same directory as the script, or you need to provide the full path.")
        return None
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# --- Sidebar (Navigation) ---
with st.sidebar:
    st.markdown('<p id="menu-font">Menu</p>', unsafe_allow_html=True)
    menu_items = ["Home", "Work Samples", "Experience"]
    selected_menu_item = st.sidebar.radio("", menu_items)
    st.write("---")
    st.markdown('<p id="menu-font">Links</p>', unsafe_allow_html=True)
    linkedin_icon = "https://img.icons8.com/?size=96&id=13930&format=png"
    email_icon = "https://img.icons8.com/?size=96&id=P7UIlhbpWzZm&format=png"
    resume_icon = "https://cdn-icons-png.flaticon.com/128/4470/4470351.png"
    #st.image(linkedin_icon, width=50)
    st.markdown(f'<div class="sidebar-text-icon-container"><a href="https://www.linkedin.com/in/utsavchaddha/" class="icon-link"><img src="{linkedin_icon}" width="50"></a></div>', unsafe_allow_html=True)
    #st.markdown("[LinkedIn](https://www.linkedin.com/in/utsavchaddha/)")
    #st.image(email_icon, width=50)
    st.markdown(f'<div class="sidebar-text-icon-container"><a href="mailto:utsav.chaddha17@gmail.com" class="icon-link"><img src="{email_icon}" width="50"></a></div>', unsafe_allow_html=True)
    #st.markdown("[Email](mailto:utsav.chaddha17@gmail.com)")
    #st.image(resume_icon, width=50)
    st.markdown(f'<div class="sidebar-text-icon-container"><a href="https://drive.google.com/file/d/1de24diZ5q5kpALK0vxU9o_YmAR2Rpr-O/view?usp=sharing" class="icon-link"><img src="{resume_icon}" width="50"></a></div>', unsafe_allow_html=True)
    #st.markdown("[Resume](https://drive.google.com/file/d/1de24diZ5q5kpALK0vxU9o_YmAR2Rpr-O/view?usp=sharing")



# --- Main Content ---
if selected_menu_item == "Home":
    # Load and resize the image using the helper function
    profile_image = None # Removed profile image
    #st.title("Utsav Chaddha") # changed title , removed emoji - moved to profile container
    if profile_image:
        #st.image(profile_image,  width=250) # added image
        #st.markdown('<div class="display-flex">', unsafe_allow_html=True)
        #st.image(profile_image, width=250)
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        st.markdown(
            """
            
                <h1 class="header-text">Utsav Chaddha</h1>
                <h3 class="header-text">Sports Partnerships | Strategic, Data Based Marketing Solutions.</h3>
                <p class = "bio-text">Motivated and results-driven Sport Management postgraduate with diverse experience across partnerships, marketing, and live event operations. Skilled in managing cross-functional projects, creating data-driven marketing strategies, and supporting high-pressure sporting events. Passionate about enhancing fan engagement and operational efficiency within sports and entertainment industries.</p>
            
            """,
            unsafe_allow_html=True,
        )
        #st.image(profile_image, width=250) #  image
        st.markdown('</div>', unsafe_allow_html=True)


    else:
        st.markdown(
            """
            <h1 class="header-text">Utsav Chaddha</h1>
            <h3 class="header-text">Sports Partnerships | Strategic, Data Based Marketing Solutions.</h3>
            <p class = "bio-text">Motivated and results-driven Sport Management postgraduate with diverse experience across partnerships, marketing, and live event operations. Skilled in managing cross-functional projects, creating data-driven marketing strategies, and supporting high-pressure sporting events. Passionate about enhancing fan engagement and operational efficiency within sports and entertainment industries.</p>
            """,
            unsafe_allow_html=True # ADDED THIS LINE
        )
    st.write("---")
    st.subheader("Skills")
    #cols = st.columns(3) # create 3 columns
    skills_data = {
        "Excel": ("https://img.icons8.com/?size=96&id=13654&format=png", "https://docs.google.com/spreadsheets/d/1PGnoqlvvfRMmtCcbGnXQsZMQpg6PbkBkw5aYzSJziV0/edit?usp=share_link"),
        "SPSS": ("https://digitalresearch.bsu.edu/studentsymposium2021/files/original/0819f70bc2e7a72233fa0c02fb8b77cc.png", "https://drive.google.com/file/d/1Ea1RiGEhBgcnopNQtrpr63BJQwfsG5zX/view?usp=share_link"),
        "Canva": ("https://img.icons8.com/?size=96&id=iWw83PVcBpLw&format=png", "https://www.instagram.com/fanatikkind/?hl=en"),
        "Adobe Premiere Pro": ("https://img.icons8.com/?size=96&id=e57Y1CnsOasB&format=png", "https://fb.watch/cuwzYKYBnp/"),
    }
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    st.markdown('<div class="skills-grid">', unsafe_allow_html=True) # Start of skills grid
    for skill_name, (skill_icon, skill_link) in skills_data.items():
        if skill_link:
            st.markdown(
                f'<a href="{skill_link}" class="icon-link" style="display:inline-flex; flex-direction:column; align-items:center;">'
                f'<img src="{skill_icon}" width="75" style="margin-bottom:5px;">'
                f'</a>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div style="display:inline-flex; flex-direction:column; align-items:center;">'
                f'<img src="{skill_icon}" width="75" style="margin-bottom:5px;">'
                f'</div>',
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True) # End of skills grid
    st.markdown('</div>', unsafe_allow_html=True)
    


elif selected_menu_item == "Work Samples":
    st.header("My Work Samples")

    with st.expander("Projects", expanded=False):
        #st.write("Here are some of my development projects:") # Removed
        # Add your projects here, using markdown or st.write
        st.markdown(
            """
            **[Analysing Social Media Habits of Gen Z English Premier League Fans](https://drive.google.com/file/d/1Ea1RiGEhBgcnopNQtrpr63BJQwfsG5zX/view?usp=share_link)**
            -   Examines the social media habits of Generation Z English Premier League fans.
            -   Utilises a mixed-methods approach combining primary quantitative and secondary qualitative content analysis.
            -   Identifies a preference among Gen Z EPL fans for visual-first social media platforms like Instagram.
            -   Highlights the common practice of using phones during matches for live social media updates and interactions.
            -   Reveals that Gen Z fan engagement is driven by a desire for social connection and real-time information.
            -   Suggests strategies for EPL teams and sports marketers to foster fan loyalty through interactive social media experiences.
            -   Emphasises the importance of visually appealing and tailored content for engaging this demographic.
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            **[Content calendar example](https://drive.google.com/drive/folders/19Ab5DKU57-aEjoyfL6Q9dMuQFdc6SJKT?usp=share_link)**
            -   Details content planning for Eden Hazard, including collaboration ideas with influencers and brands. It suggests consistent posting on Instagram (3-4 times per week) and content such as football challenges and mini-vlogs.
            -   A social media planner for a game called Animera includes details on planet features, gameplay snippets, and weekly contests.
            -   Discusses digital marketing, covering topics like SEO, keywords, anchor tags, sitemaps, and canonical tags. It also explains how digital marketing can help sales and outlines steps to create campaigns on Google Ads.
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            [Analysis of the Esports market in India](https://docs.google.com/presentation/d/1fGlaxAAlzxmhjNy6jCVMm79r8djlc8Qa3xT8z-4RzW8/edit?usp=share_link)
            -   The audience has increased from 387.8 million in 2019 to 474 million in 2021 and is projected to reach 577.2 million by 2024.
            -   India's e-sports industry is expected to surpass the biggest sport franchise in India in terms of prize money, offering a total prize pool of INR 1B by FY2025.
            -   The majority of Indian gamers are male (84%), but this is expected to shift to 70% male and 30% female by 2025.
            -   The number of online gamers using smartphones increased by 60% when pre-COVID and lockdown statistics are compared.
            -   Key revenue streams include tournament revenues, streaming media revenues, and prize pools.
            -   The gaming sector in India attracted $544 million in investments between August 2020 and January 2021.
            """,
            unsafe_allow_html=True
        )

    with st.expander("Video Edits", expanded=False):
        #st.write("Here are some of my video edits:") # Removed
        # Add your video edits here, using markdown or st.write
        st.markdown(
            """
            **[Video Edit 1](https://fb.watch/cuwxiA705i/)**
            -   Views: 4.6 Million
            -   Reactions: 155k
            -   Comments: 597
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            **[Video Edit 2](https://fb.watch/cuwzYKYBnp/)**
            -   Views: 9.5 Million
            -   Reactions: 132k
            -   Comments: 3.4k
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            **[Video Edit 3](https://fb.watch/cuwFkxY3KM/)**
            -   Views: 19 Million
            -   Reactions: 18k
            -   Comments: 1.3k
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            **[Video Edit 4](https://fb.watch/cuwU5cLXQP/)**
            -   Views: 2.9 Million
            -   Reactions: 7k
            -   Comments: 917
            """,
            unsafe_allow_html=True
        )

    with st.expander("Social media management", expanded=False):
        st.markdown(
            """
            - [UNREEL](https://www.instagram.com/extremeofficial?utm_medium=copy_link)
            - [Auto AllStars](https://www.instagram.com/autoallstars?utm_medium=copy_link)
            - [Fantasy Dangal](https://www.instagram.com/fantasydangal/)
            - [Dangal Games](https://www.instagram.com/dangalgames/)
            - [Poker Dangal](https://www.instagram.com/pokerdangal/)
            """,
            unsafe_allow_html=True
        )

    with st.expander("Podcast", expanded=False):
        #st.write("Here are some of my Podcasts:") # Removed
        # Add your Podcasts here, using markdown or st.write
        st.markdown(
            """
            **[Offside](https://www.instagram.com/offside.epl/)**
            - Initiated a side project during my undergraduate studies to explore content creation
            - Managed all aspects of production, including video editing, graphic design, and caption writing
            - Achieved over 10,000 views collectively on YouTube and Instagram
            """,
            unsafe_allow_html=True
        )

elif selected_menu_item == "Experience":
    st.header("My Experience")

    with st.expander("Sports Marketing", expanded=False):
        st.markdown(
            """
            **Apex Digital - UAE (remote)**
            Partnership Executive, 07/2022 – 11/2022
            -   Managed multiple projects simultaneously while serving as Head of Partnerships for the game Search for Animera.
            -   Initiated and maintained client relationships, effectively communicating the company’s vision and coordinating internal team meetings.
            -   Identified and secured strategic partnerships within the Web3 space, targeting relevant collaborators to drive growth.
            -   Collaborated closely with content and design teams, ensuring partnership deliverables aligned with brand goals and maximised impact.

            **Dangal Games - Delhi, India**
            Copywriter 04/2022 – 07/2022
            -   Oversaw the post-ideation phase of multiple social media accounts, developing engaging and brand-aligned advertising campaigns.
            -   Crafted promotional copy and researched market trends to inform and refine content strategy.
            -   Managed end-to-end social media content creation, briefing the design team to ensure alignment with the digital strategy.
            -   Supported the implementation of data-driven marketing solutions to enhance campaign effectiveness and audience targeting.

            **EXTREME International - United Kingdom (remote)**
            Content Editor 10/2021 – 04/2022
            -   Carried out in-depth content research and coordinated outreach with athletes and content creators to source engaging material.
            -   Edited and compiled high-performing videos using Adobe Premiere Pro, resulting in over 36 million views, 300,000 likes, and 6,000 comments.
            -   Managed daily content scheduling, including Reels, for Instagram accounts with 1.5M+ followers, contributing to revenue generation exceeding $2,000.

            **Engage Digital Partners - India (remote)**
            Social Media Analyst, 03/2021 – 08/2021
            -   Utilised analytical tools to extract insights from client social media accounts, identifying trends and performance metrics.
            -   Supported the development of tailored social media campaigns in collaboration with clients such as Spektacom and FC Bengaluru United.
            -   Designed and presented compelling pitch decks and client presentations, including a targeted proposal for the post-pandemic eSports market.
            """,
            unsafe_allow_html=True
        )

    with st.expander("Events & Operations", expanded=False):
        st.markdown(
            """
            **Leicester City Football Club - Leicester, UK**
            Logistics Assistant, March 2024 –Present
            -   Supervise match day equipment for the safety team, ensuring all items are operational and accounted for.
            -   Coordinate the arrangement, tracking, and logging of equipment, maintaining accurate inventory records.

            **Loughborough Coach & Volunteering Academy - Loughborough, UK**
            Events Assistant, Nov 2023 –Sep 2024
            -   Assisted with event setup and operations across multiple rugby and athletics tournaments, including the British Athletics Indoor Championships and BUCS.
            -   Responsible for ticketing, crowd management, scoreboard operation, digital scoring, and jump camera management for long and triple jump events.
            -   Supported the smooth execution of matches by ensuring efficient game flow and on-site coordination.

            **Birchfield Harriers - Birmingham, UK**
            Operations Assistant, May 2024 –August 2024
            -   Provided operational support during athletics meets at Alexander Stadium in collaboration with UK Athletics officials.
            -   Managed on-field logistics and digital systems, including live scoring and camera setup for event monitoring.

            **Alan march sports - Loughborough University, UK**
            Production Assistant, 	Jan 2024 –June 2024
            -   Provided technical support for Netball Super League matches, assisting with lighting, scoring, and music operations.
            -   Contributed to the smooth delivery of the season by offering reliable logistical and event-day support.
            """,
            unsafe_allow_html=True
        )

    st.subheader("Education")
    with st.expander("Master of Science in Sport Management | Loughborough University", expanded=False): # changed to false
        st.write("Oct 2023 - Oct 2024")
        st.markdown(
            """
            - Course Representative for the biggest sport management cohort.
            - Winner of Athena Swan Silver Award for Outstanding Volunteer of the year
            - My thesis focused on analysing trends in Gen Z consumer behaviour on social media, utilising a mixed methods approach with both numerical and theoretical data, and employing statistical tools like SPSS to gather and analyse the data.
            - Grade: Merit | 2:1
            """,
            unsafe_allow_html=True
        )

    with st.expander("Bachelor in Sport Management | University of Mumbai"):
        st.write("July 2018 - August 2021")
        st.markdown(
            """
            - Developed management and research skills in sports and marketing.
            - Did multiple internships and hosted successful Sports festivals.
            - Grade: O (Outstanding) | 7.63/10
            """
        )

# --- Footer ---
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #777;">© 2025 Your Name. All rights reserved.</p>',
    unsafe_allow_html=True,
)


          
