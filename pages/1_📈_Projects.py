import streamlit as st
from streamlit_extras.mention import mention

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Projects",
    page_icon="📈",
)

st.header("📈 Projects")
with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Dummy Project Title")
            st.write("*Project Description*")
            st.markdown("""
            - Stuff I did......
            - More details.....
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Github Repo", icon="github", url="",)
        with image_column:
            st.image("assets/test_project.png")