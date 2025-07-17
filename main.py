import streamlit as st
import nltk
from nltk import NaiveBayesClassifier
from joblib import load
import time

nltk.download('names')

def extract_gender_features(name):
    name = name.lower()
    features = {
        "suffix": name[-1:],
        "suffix2": name[-2:] if len(name) > 1 else name[0],
        "suffix3": name[-3:] if len(name) > 2 else name[0],
        "suffix4": name[-4:] if len(name) > 3 else name[0],
        "suffix5": name[-5:] if len(name) > 4 else name[0],
        "suffix6": name[-6:] if len(name) > 5 else name[0],
        "prefix": name[:1],
        "prefix2": name[:2] if len(name) > 1 else name[0],
        "prefix3": name[:3] if len(name) > 2 else name[0],
        "prefix4": name[:4] if len(name) > 3 else name[0],
        "prefix5": name[:5] if len(name) > 4 else name[0]
    }
    return features

bayes = load('gender_prediction.joblib')

def main():
    st.set_page_config(page_title="Hello Kitty Gender Predictor Supreme 💖", page_icon="🎀", layout="centered")

    st.markdown("""
        <style>
        body {
            background: linear-gradient(-45deg, #ffe6f2, #ffd1dc, #ffe6f2, #ffd1dc);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .main {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            color: #ff3399;
            text-align: center;
        }
        .card {
            background-color: rgba(255, 240, 245, 0.9);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 0px 20px #ff99cc;
            margin: 20px auto;
            max-width: 500px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff99cc, #ff66b3);
            color: white;
            font-size: 18px;
            border-radius: 12px;
            padding: 0.5em 2em;
            border: 2px solid #ff66b3;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            background: linear-gradient(90deg, #ff66b3, #ff99cc);
        }
        .footer {
            font-size: 16px;
            color: #ff66b3;
            margin-top: 50px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.image("https://i.imgur.com/5uQ9aO2.png", use_column_width=True)

    st.markdown("<h1>🎀😸 Hello Kitty Gender Predictor SUPREME 😸🎀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:20px;'>✨ Enter your cutest name and see the kawaii magic unfold! ✨</p>", unsafe_allow_html=True)

    with st.container():
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            input_name = st.text_input('🌸 Your Cute Name 🌸', placeholder="e.g., Kitty, Melody, Daniel")
            if st.button('🎀 Predict Now 🎀'):
                if input_name.strip() != '':
                    features = extract_gender_features(input_name)
                    predicted_gender = bayes.classify(features)

                    # cute effects
                    st.balloons()
                    st.snow()
                    time.sleep(0.5)
                    st.success(f'🎀 The predicted gender for **"{input_name}"** is: 🌸 **{predicted_gender.capitalize()}** 🌸')
                else:
                    st.warning('🌸 Please enter a cute name 🌸')
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="footer">
        ✨ Made with 💖 by Hello Kitty Fans Club ✨<br>
        🌸 Stay kawaii & spread cuteness everywhere! 🌸
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
