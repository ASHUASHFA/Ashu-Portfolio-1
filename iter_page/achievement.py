import streamlit as st

st.markdown("""
    <style>
    div.streamlit-tabs button[data-baseweb="tab"] {
        font-size: 150px; /* Adjust the font size of the tab labels */
        width: 250px;    /* Set the width of each tab */
    }
    div.streamlit-tabs button[data-baseweb="tab"]:hover {
        color: white; 
        background-color: #007BFF; /* Change background on hover */
    }
    </style>
""", unsafe_allow_html=True)

tab = st.tabs(["Running and Football", "Running", "Drawing", "Running Race Competition", "Art Event"])

with tab[0]:
    st.markdown("<h4 style = 'color: #a6f1f2; font-style: italic; font-size: 8;'>C. Abdul Hakeem College of Engineering and Technology - 27th Annual Sports Day</h4>", unsafe_allow_html = True)
    st.write(
        """
        -   Won 1st place in running competition
        -   For 100 Metres during 2024-2025 Annual sports day
        -   Participated in football and won the match as "Winner" Award
        """
    )
    st.write(" ")
    st.image("acheivements/ach-4.jpg")

with tab[1]:
    st.markdown("<h4 style = 'color: #a6f1f2; font-style: italic; font-size: 8;'>C. Abdul Hakeem College of Engineering and Technology - 26th Annual Sports Day</h4>", unsafe_allow_html = True)
    st.write(
        """
        -   Won 1st place in running competition
        -   For 400 Metres during 2024-2025 in 26th Annual sports day
        """
    )
    st.write(" ")
    st.image("acheivements/ach-5.jpg")

with tab[2]:
    st.markdown("<h4 style='color: #f2a6ec; font-style: italic; font-size: 8;'>C. Abdul Hakeem College of Engineering and Technology - 27th Annual Sports Day</h4>", unsafe_allow_html=True)
    st.write(
        """
        -   DR. Gayathry G(Former International Athlete) who has participated as cheif guest of our college in sports day
        -   I am inspired by her dedicational approach in athlete
        -   I have presented a pencil-work of her image
        """
    )
    st.write(" ")
    st.image("acheivements/acheivement-1.jpg", width=800)

with tab[3]:
    st.markdown("<h4 style = 'color: #a6f1f2; font-style: italic; font-size: 8;'>Anna University zonal level competition</h4>", unsafe_allow_html = True)
    st.write(
        """
        -   I have participated and achieved a medal
        -   I am Third Price in zonal level competitiion in Anna University
        """
    )
    st.write(" ")
    st.image("acheivements/ach-2.jpg", width=800)

with tab[4]:
    st.markdown("<h4 style = 'color: #a6f1f2; font-style: italic; font-size: 8;'>C. Abdul Hakeem College of Engineering and Technology - Revibe' 24</h4>", unsafe_allow_html = True)
    st.write(
        """
        -   Won 1st price in Art event
        -   Conducted by Student Guidance Cell in C. Abdul Hakeem College of Engineering and Technology
        """
    )
    st.write(" ")
    st.image("acheivements/ach-3.jpg")




