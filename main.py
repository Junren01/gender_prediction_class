import streamlit as st
import nltk
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
    st.set_page_config(page_title="Hello Kitty Gender Predictor KAWKAW 🌸✨", page_icon="🎀", layout="centered")

    st.markdown("""
        <style>
        body {
            background: linear-gradient(270deg, #ffd1dc, #ffe6f2, #ffd1dc, #ffe6f2);
            background-size: 800% 800%;
            animation: rainbowBG 12s ease infinite;
        }
        @keyframes rainbowBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        h1 {
            text-align: center;
            font-size: 3em;
            color: #ff66b3;
            animation: blink 1.5s infinite alternate;
        }
        @keyframes blink {
            from {opacity: 1;}
            to {opacity: 0.6;}
        }
        .card {
            background-color: rgba(255, 240, 245, 0.95);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 0px 30px #ff99cc;
            margin: 20px auto;
            max-width: 500px;
            text-align: center;
            font-size: 18px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff99cc, #ff66b3, #ff99cc);
            color: white;
            font-size: 20px;
            border-radius: 12px;
            padding: 0.6em 2em;
            border: 2px solid #ff66b3;
            box-shadow: 0 0 10px #ff99cc;
            animation: glow 2s infinite alternate;
        }
        @keyframes glow {
            from {box-shadow: 0 0 10px #ff99cc;}
            to {box-shadow: 0 0 20px #ff66b3;}
        }
        .footer {
            font-size: 16px;
            color: #ff66b3;
            margin-top: 50px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🎀🌸 HELLO KITTY GENDER PREDICTOR 🌸🎀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:20px;'>✨🌈 Enter your cutest name and see the kawaii magic explode! 💖✨</p>", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    input_name = st.text_input('🌸 Your Magical Name 🌸', placeholder="e.g., Kitty, Melody, Daniel")

    if st.button('🎀 Predict My Destiny 🎀'):
        if input_name.strip() != '':
            features = extract_gender_features(input_name)
            predicted_gender = bayes.classify(features)

            # KAWKAW EFFECTS 🎉
            st.balloons()
            st.snow()
            time.sleep(0.3)

            st.markdown(f"""
            <div style="font-size:22px;color:#ff3399;">
            🎉✨🌸 The predicted gender for <b>{input_name}</b> is: <b>{predicted_gender.capitalize()}</b> 🌸✨🎉
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning('💖 Please enter your magical name 💖')

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="footer">
        🌸✨ Made with infinite kawaii sparkles ✨🌸
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
