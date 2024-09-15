import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email credentials (use environment variables or a secrets manager in production)
EMAIL_ADDRESS = "sourabhsingh4800@gmail.com"
EMAIL_PASSWORD = "Gaurav1!"

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
st.title("🚀 Welcome to My Portfolio! 🌟")

# Add an image to the sidebar
image_path = "pic.png"
if os.path.exists(image_path):
    st.sidebar.image(image_path, use_column_width=True)
else:
    st.sidebar.error("Image not found. Please check the file path or upload an image.")
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.sidebar.image(uploaded_file, use_column_width=True)

# Add a larger panda emoji with text, centered, along with technology emojis
st.sidebar.markdown("<div style='text-align: center; font-size: 30px;'>💻🎯📊</div>", unsafe_allow_html=True)


# Rest of your Streamlit app code
st.sidebar.title("Sourabh Singh")
section = st.sidebar.radio("Select a section:", ["Introduction", "Education", "Skills", "Projects", "Experience", "Contact Information"])

if section == "Introduction":
    st.header("Introduction")
    st.write("""
    Hello! I am Sourabh Singh. 
    I am excited to start my career and contribute to innovative projects.
    """)
elif section == "Education":
    st.header("🎓 Education")
    
    st.subheader("📘 Master of Science")
    st.write("""
    **Indian Institute of Technology, Indore**  
    *2023 - Present*
    
    - **Relevant Coursework**: 
        - Machine Learning
        - Advance Computer Network
        - Advance Algorithms
    - **Achievements**: 
        - Ranked in the top 3% of problem solvers at IIT Indore on GeeksforGeeks.
        - CodeChef rating of 1550+.
    - **Activities**: 
        - Participated in e-sports tournament hosted by the gaming club of IIT Indore.
    """)
    
    st.subheader("📗 Bachelor of Engineering")
    st.write("""
    **Institute of Engineering, Jiwaji University, Gwalior**  
    *2019 - 2023*
    
    - **Relevant Coursework**: 
        - Computer Networks
        - Operating Systems
        - Database Management System
        - Data Structures
        - Design and Analysis of Algorithms
        - Engineering Mathematics
        - Probability
        - Linear Algebra
    - **Activities**: 
        - Finance Lead in E-Fest 2019.
    """)
    
    st.subheader("📙 Higher Secondary School")
    st.write("""
    **Kempfort Public School, Bhopal**  
    *2018*
    
    - **Achievements**: 
        - Top 1% of the class.
    - **Activities**: 
        - Secured second place in a football tournament, showcasing teamwork and strategy.
        - Participated in a drama performance, bringing creativity and expression to life.
    """)
    
    st.subheader("📕 Secondary School")
    st.write("""
    **Kempfort Public School, Bhopal**  
    *2016*
    - **Achievements**: 
        - Top 5% of the class.
    - **Activities**: 
        - Won third position in Volleyball.
    """)
elif section == "Skills":
    st.header("🛠️ Skills ")
    with st.expander("Soft Skills"):
        st.write("""
        - Communication
        - Teamwork and Collaboration
        - Problem-Solving
        - Adaptability
        - Leadership
        """)
    
    with st.expander("Programming Languages"):
        st.write("""
        - Python
        - Java
        - C++
        - P4
        - C
        """)

    with st.expander("Web Development"):
        st.write("""
        - HTML
        - CSS
        - JavaScript
        - React
        - Express
        """)

    with st.expander("Tools & Technologies"):
        st.write("""
        - Git
        - Docker
        - Kubernetes
        """)

    with st.expander("Data & Machine Learning"):
        st.write("""
        - Data Analysis
        - PyTorch
        - Scikit-learn
        - Pandas
        - Matplotlib
        - Seaborn
        - TensorFlow
        - Keras
        - NumPy
        - SciPy
        - Plotly
        """)

    with st.expander("Frameworks"):
        st.write("""
        - Django
        - Flask
        - Angular
        """)

    with st.expander("Operating Systems"):
        st.write("""
        - Windows
        - Kali Linux
        - Kodachi
        - Ubuntu
        - P4
        """)

    with st.expander("Networking Tools & Technologies"):
        st.write("""
        - Wireshark
        - Nmap
        - Cisco Packet Tracer
        - OpenVPN
        - Mininet
        - Scapy
        - Netcat
        - OpenFlow
        """)



elif section == "Projects":
    st.header("💡 Project")
    st.write("""
    1. **[AutoML](https://github.com/yourusername/automl-project) 🧠**:
        - **Overview**: Created a dynamic web application leveraging Streamlit, integrating PyCaret for automated machine learning, and D-Tale for insightful data exploration.
        - **Features**:
            - **User-Friendly Interface**: Users can effortlessly upload datasets and explore them through interactive visualizations.
            - **Machine Learning Simplified**: Automate model selection and comparison for classification and regression tasks, allowing users to focus on insights rather than complex configurations.
            - **Interactive Data Exploration**: Utilize D-Tale for real-time data manipulation and analysis, enhancing the decision-making process.

    2. **[Packet Latency Monitor](https://github.com/yourusername/packet-latency-monitor) 🌐**:
        - **Overview**: Developed a sophisticated network simulation tool to monitor and analyze packet latency across custom network topologies.
        - **Features**:
            - **Custom Network Topology**: Designed networks with multiple high-traffic senders and a few receivers, incorporating switches to reflect real-world scenarios.
            - **Advanced Packet Tracking**: Added a custom timestamp in the IP option field to measure the time each packet spends within switches, providing detailed latency insights.
            - **Impact Analysis**: Analyzed latency data to pinpoint influential IP addresses and optimize network performance, facilitating the development of more efficient systems.

    3. **[Attendance Monitoring System with Facial Recognition in Real Time](https://github.com/yourusername/attendance-monitoring-system) 📸**:
        - **Overview**: Built a cutting-edge facial recognition system for real-time attendance tracking, utilizing OpenCV and Facial Recognition libraries.
        - **Features**:
            - **Real-Time Recognition**: Implemented a robust facial recognition system for accurate and instantaneous attendance logging.
            - **Backend Integration**: Used Firebase’s API to store and manage attendance data in real-time, ensuring seamless data access and updates.
            - **Admin Management**: Enabled administrators to easily add new users, facilitating straightforward system management and scalability.

    """)





elif section == "Experience":
    st.header("💼 Experience")
    st.write("""
    - **Freelance Independent Contractor**, [CHEGG] (Feb. 2021 - Mar.2023)
      - Tackled over 2,000 complex questions in Algebra, Calculus, Probability, and Higher Mathematics,
              helping students overcome challenges and deepen their understanding of these subjects.
      - Contributed to Chegg’s growth in user engagement, which saw an 18% increase in subscribers in 2021, 
             expanding to 8.2 million users by 2022.
    """)
    
    
    
    
elif section == "Contact Information":
    st.header("📞 Contact Information")
    st.write("""
    - 📧 Email: sourabhsingh4800@gmail.com
    - 💼 LinkedIn: [https://www.linkedin.com/in/sourabhsingh4800/](https://www.linkedin.com/in/sourabhsingh4800/)
    - 🐙 GitHub: [https://github.com/sourabh4800](https://github.com/sourabh4800)
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
