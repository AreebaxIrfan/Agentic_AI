import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Your Name | Portfolio", page_icon=":star:", layout="wide")

# Theme toggle function
def toggle_theme():
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

    if st.button('Toggle Dark Mode'):
        st.session_state.dark_mode = not st.session_state.dark_mode
    return st.session_state.dark_mode

# Home Section
def home_section():
    # Header
    st.title("Your Full Name")
    st.write("Welcome to my professional portfolio! Here's a little about me:")

    # Short Bio
    st.subheader("About Me")
    st.write("""
        I am a passionate web developer specializing in Next.js, Python, and AI technologies. I love creating
        beautiful, functional applications and am always eager to learn and explore new tech.
    """)

    # Add your image here (replace 'assets/photo.jpg' with your actual image file)
    image = Image.open("assets/photo.jpg")  # Put your image in the 'assets' folder
    st.image(image, width=200)

    # Optional: Social Media links
    st.write("[LinkedIn](https://www.linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourprofile)")

# About Section
def about_section():
    # Title
    st.title("About Me")
    
    # Skills and Technologies
    st.subheader("Skills & Tech Stack")
    st.write("""
        - Web Development: HTML, CSS, JavaScript, React, Next.js, Node.js
        - Backend: Python, Django, Flask, FastAPI
        - Databases: MongoDB, PostgreSQL, MySQL
        - Cloud: AWS, Google Cloud, Firebase
        - AI & Machine Learning: TensorFlow, Keras, scikit-learn
        - Tools: Git, Docker, Kubernetes
    """)
    
    # Education and Career Highlights
    st.subheader("Education & Career")
    st.write("""
        I have a background in computer science, having completed various courses and projects in full-stack web development.
        I have worked with top-tier mentors and developed multiple projects.
    """)

# Projects Section
def projects_section():
    # Title
    st.title("My Projects")

    # S-NIKY E-commerce
    st.subheader("S-NIKY E-commerce Platform")
    st.write("""
        S-NIKY is a full-featured e-commerce platform developed with Next.js, React, and integrated with a backend system.
        It includes user authentication, product management, shopping cart, and order processing.
    """)
    st.write("[GitHub Repository](https://github.com/yourprofile/sniky-ecommerce)")

    # Resume Builder
    st.subheader("Resume Builder")
    st.write("""
        A simple, intuitive resume builder app where users can create, edit, and download their resume as a PDF.
        Built with React, Next.js, and PDF generation libraries.
    """)
    st.write("[GitHub Repository](https://github.com/yourprofile/resume-builder)")

# Contact Section
def contact_section():
    # Title
    st.title("Contact Me")
    
    # Contact Form
    st.subheader("Get in Touch")
    st.write("Feel free to reach out to me via email or social media!")

    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Submit"):
        if email and message:
            st.success("Your message has been sent!")
        else:
            st.error("Please fill in both fields.")

# Main function to control the page layout
def main():
    dark_mode = toggle_theme()

    # Set dark or light theme based on toggle
    if dark_mode:
        st.markdown("""
            <style>
            body {
                background-color: #1a1a1a;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body {
                background-color: white;
                color: black;
            }
            </style>
            """, unsafe_allow_html=True)

    # Navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

    if menu == "Home":
        home_section()
    elif menu == "About":
        about_section()
    elif menu == "Projects":
        projects_section()
    elif menu == "Contact":
        contact_section()

if __name__ == "__main__":
    main()
