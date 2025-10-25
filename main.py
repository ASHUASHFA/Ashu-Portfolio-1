import streamlit as st

st.set_page_config(
    page_title="Ashfaq", 
    page_icon="ashu-logo.jpg",
    layout="centered",
    initial_sidebar_state="auto"
)

# Hide default footer and MainMenu
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap');

    html, body, .stApp {
        height: 100%;
        margin: 0;
        padding: 0;
        background: radial-gradient(ellipse at center, #0a0a0a 0%, #101d2c 100%);
        color: #ffffff;
        font-family: 'Orbitron', monospace;
        animation: pulseBg 2s ease-in-out infinite;
        overflow-x: hidden;
    }

    @keyframes pulseBg {
        0%, 100% { background-color: #0a0a0a; }
        50% { background-color: #121d2b; }
    }

    h1, h2 {
        color: #00f0ff;
        text-shadow:
            0 0 10px #00f0ff,
            0 0 20px #00f0ff,
            0 0 40px #00f0ff;
        animation: glowText 2.5s ease-in-out infinite alternate;
    }

    @keyframes glowText {
        0% { text-shadow: 0 0 5px #00e0ff, 0 0 20px #00f0ff; }
        100% { text-shadow: 0 0 20px #00f0ff, 0 0 40px #00e0ff; }
    }

    .subtitle {
        font-size: 1.5rem;
        color: #c8d8ff;
        letter-spacing: 2px;
        margin-bottom: 2rem;
        animation: glowText 3s ease-in-out infinite alternate;
    }
            
    .custom-write {
        font-family: 'Orbitron', monospace;
        font-size: 1.2rem;
        color: #00f0ff;
        text-shadow: 0 0 1px #00f0ff, 0 0 1px #00caff;
        overflow: hidden;
        white-space: normal;
        display: inline-block;
        border-right: 2px solid #00f0ff;
        width: 0;
        animation: 
            typing 2s steps(100, end) forwards, 
            blink-caret 0.75s step-end 6;
        animation-fill-mode: forwards;
    }

    /* Typing animation */
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    /* Caret blinking */
    @keyframes blink-caret {
        0%, 100% { border-color: transparent }
        50% { border-color: #00f0ff }
    }

    .custom-write1 {
        font-family: 'Orbitron', monospace;
        font-size: 0.9rem;
        color: #00f0ff;
        text-shadow: 0 0 0.7px #00f0ff, 0 0 0.7px #00caff;
        overflow: hidden;
        white-space: normal;
        display: inline-block;
    }


    .stButton > button {
        background-color: #00f0ff;
        color: black;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        box-shadow: 0 0 10px #00f0ff;
        animation: pulseGlow 2s ease-in-out infinite alternate;
    }

    .stButton > button:hover {
        background-color: #00caff;
        transform: scale(1.05);
    }

    #particles-js {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    </style>

    <!-- Particle Background -->
    <div id="particles-js"></div>

    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": {
                "value": 80,
                "density": { "enable": true, "value_area": 800 }
            },
            "color": { "value": "#00f0ff" },
            "shape": { "type": "circle" },
            "opacity": {
                "value": 0.6,
                "random": false
            },
            "size": {
                "value": 4,
                "random": true
            },
            "line_linked": {
                "enable": true,
                "distance": 120,
                "color": "#00f0ff",
                "opacity": 0.4,
                "width": 1.5
            },
            "move": {
                "enable": true,
                "speed": 1.6,
                "direction": "none",
                "random": false,
                "straight": false,
                "out_mode": "out"
            }
        },
        "interactivity": {
            "events": {
                "onhover": { "enable": true, "mode": "repulse" },
                "onclick": { "enable": false }
            },
            "modes": {
                "repulse": {
                    "distance": 100,
                    "duration": 0.4
                }
            }
        },
        "retina_detect": true
    });
    </script>
""", unsafe_allow_html=True)


# Page setup

about_page = st.Page(
    page = "iter_page/about.py",
    title = "About",
    icon = ":material/account_circle:",
    default = True,
)

projects_page = st.Page(
    page = "iter_page/proj_page.py",
    title = "Projects",
    icon = ":material/bar_chart:",
)

course_page = st.Page(
    page = "iter_page/cert_page.py",
    title = "Cources",
    icon = "📃"
)

achieve_page = st.Page(
    page = "iter_page/achievement.py",
    title = "Achievement",
    icon = "🌟"
)

experience_page = st.Page(
    page = "iter_page/colloborator.py",
    title = "Collaboration",
    icon = "📈"
)

#service_page = st.Page(
#    page = "iter_page/service.py",
#    title = "Services",
#    icon = "🛠️"
#)

# Navigation Menu Setup (without section)
pg = st.navigation(pages = [about_page, projects_page, course_page, achieve_page, experience_page])

# Navigation Menu Setup (including section)
#pg = st.navigation(
   # {
  #      "Info":[about_page],
 #       "Projects":[project_1_page, project_2_page]
#    }
#)

# Shared on all pages
st.logo("ashu-logo.jpg")
st.sidebar.text("Graphic Designer")

# Run Navigation
pg.run()
