import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email credentials (use environment variables or a secrets manager in production)
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"

def send_email(name, email, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = "New Contact Form Submission"

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# Streamlit app
st.title("🚀 Welcome to My Portfolio!")

# Add an image to the sidebar
image_path = "pic.jpeg"
if os.path.exists(image_path):
    st.sidebar.image(image_path, use_column_width=True)
else:
    st.sidebar.error("Image not found. Please check the file path or upload an image.")
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.sidebar.image(uploaded_file, use_column_width=True)

# Add a larger panda emoji with text, centered
st.sidebar.markdown("<div style='text-align: center; font-size: 50px;'>🐼</div>", unsafe_allow_html=True)

# Rest of your Streamlit app code
st.sidebar.title("Navigation")
section = st.sidebar.radio("Select a section:", ["Introduction", "Education", "Skills", "Projects", "Contact Information"])

if section == "Introduction":
    st.header("Introduction")
    st.write("""
    Hello! I am [Your Name], a recent graduate with a passion for [Your Field]. 
    I am excited to start my career and contribute to innovative projects.
    """)
elif section == "Education":
    st.header("Education")
    st.write("""
    - **Bachelor of [Your Degree]**, [Your University] (Year-Year)
    - **High School Diploma**, [Your High School] (Year-Year)
    """)
elif section == "Skills":
    st.header("Skills")
    st.write("""
    - Programming Languages: Python, Java, C++
    - Web Development: HTML, CSS, JavaScript
    - Tools: Git, Docker, Kubernetes
    - Others: Data Analysis, Machine Learning
    """)
elif section == "Projects":
    st.header("Projects")
    st.write("""
    1. **Project Name 1**: Description of the project and technologies used.
    2. **Project Name 2**: Description of the project and technologies used.
    3. **Project Name 3**: Description of the project and technologies used.
    """)
elif section == "Contact Information":
    st.header("Contact Information")
    st.write("""
    - Email: [your.email@example.com](mailto:your.email@example.com)
    - LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/your-linkedin-profile)
    - GitHub: [Your GitHub Profile](https://github.com/your-github-profile)
    """)

    st.subheader("Contact Form")
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if send_email(name, email, message):
            st.success("Thank you for your message! I will get back to you soon.")
        else:
            st.error("There was an error sending your message. Please try again later.")
