import streamlit as st
import base64


# def home():

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Portfolio",
    page_icon="🖥️",
)

# CSS styles file
with open("styles/main.css") as f:
    st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Profile image file
with open("assets/waqas-Avatar.png", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

# PDF CV filewith en("assets/waqas_CV.pdf", "rb") as pdf_file:
with open("assets/waqas_CV.pdf","rb") as pdf_file:
    pdf_bytes = pdf_file.read()

    
# Top title
st.write(f"""<div class="title"><strong>Hi! My name is</strong> Syed Waqas 👋</div>""", unsafe_allow_html=True)

    # Profile image
    # st.write(f"""
    # <div class="container">
    #     <div class="box">
    #         <div class="spin-container">
    #             <div class="shape">
    #                 <div class="bd">
    #                     <img src="{img}" alt="Syed Waqas">
    #                 </div>
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # """, 
    # unsafe_allow_html=True)

# Alternative image (static and rounded) uncomment it if you prefer this one
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Syed Waqas" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 5px; margin-bottom: 5px;">
</div>
""", unsafe_allow_html=True)

# Subtitle
st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning and Software Engineer</div>""", unsafe_allow_html=True)

# Social Icons
social_icons_data = {
    # Platform: [URL, Icon]
    # "Kaggle": ["https://www.kaggle.com/wms31", "https://www.kaggle.com/static/images/site-logo.svg"],
    "LinkedIn": ["https://www.linkedin.com/in/syed-waqas-22a73baa", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
    "GitHub": ["https://github.com/wms31", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
    # "Twitter": ["https://twitter.com/wms31", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
    # "YouTube": ["https://www.youtube.com/@wms31", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
    # "Medium": ["https://medium.com/@wms31", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"]
}

social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

st.write(f"""
<div style="display: flex; justify-content: center; margin-bottom: 10px;">
    {''.join(social_icons_html)}
</div>""", 
unsafe_allow_html=True)

# st.write("##")

# About me section
st.subheader("About Me")
st.write("""
- 🧑‍💻 I am a **Senior ML and Software Engineer** @ [Vacker Global](https://www.vackerglobal.com/)

- ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision, Automation** and more!
    
- 🤖 I enjoy developing ML projects
    
- 📫 How to reach me: waqas_95@live.com
    
- 🏠 United Arab Emirates
""")

st.write("##")

# Download CV button
st.download_button(
    label="📄 Download my CV",
    data=pdf_bytes,
    file_name="waqas_cv.pdf",
    mime="application/pdf",
)

st.write("##")
    
st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)




# if __name__ == "__main__":

#     home()