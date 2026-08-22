import streamlit as st
from modules import home
from modules import workspace as ws
# import base64

st.set_page_config(
     page_title="Data Profiler",
     page_icon="📊",
     layout="wide"
)

# for background effect
st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                ellipse 55% 45% at 10% 5%,
                rgba(0, 110, 255, 0.45),
                transparent 70%
            ),
            radial-gradient(
                ellipse 50% 40% at 90% 10%,
                rgba(120, 40, 255, 0.35),
                transparent 70%
            ),
            radial-gradient(
                ellipse 45% 35% at 50% 15%,
                rgba(0, 200, 255, 0.30),
                transparent 70%
            ),
            radial-gradient(
                ellipse 60% 45% at 30% 35%,
                rgba(50, 60, 255, 0.20),
                transparent 75%
            ),
            radial-gradient(
                ellipse 50% 40% at 80% 40%,
                rgba(150, 50, 255, 0.15),
                transparent 75%
            ),
            linear-gradient(
                to bottom,
                rgba(0, 80, 255, 0.08),
                transparent 75%
            );

        background-size:
            180% 180%,
            160% 160%,
            150% 150%,
            170% 170%,
            160% 160%,
            100% 100%;

        animation: randomGradient 15s ease-in-out infinite;
    }


    @keyframes randomGradient {

        0% {
            background-position:
                0% 0%,
                100% 0%,
                50% 0%,
                0% 30%,
                100% 40%,
                center;
        }

        20% {
            background-position:
                30% 15%,
                70% 20%,
                20% 30%,
                40% 10%,
                80% 50%,
                center;
        }

        40% {
            background-position:
                70% 0%,
                20% 30%,
                80% 10%,
                10% 50%,
                50% 20%,
                center;
        }

        60% {
            background-position:
                40% 35%,
                90% 5%,
                30% 40%,
                70% 20%,
                20% 60%,
                center;
        }

        80% {
            background-position:
                10% 10%,
                60% 35%,
                90% 20%,
                30% 60%,
                80% 10%,
                center;
        }

        100% {
            background-position:
                50% 0%,
                0% 20%,
                60% 30%,
                90% 40%,
                30% 20%,
                center;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


if "explore" not in st.session_state:
    st.session_state.explore = False


if st.session_state.explore:
    ws.workspace()

else:
    home.show_home()






