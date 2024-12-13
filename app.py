import streamlit as st
import pickle
import time

# Load the model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

# Set page title and background color
st.set_page_config(
    page_title='Twitter Sentiment Analysis',
    page_icon=':bird:',
    layout='wide',
    initial_sidebar_state='collapsed',
)

# Define colors
background_color = "#FFD700"  # Gold
text_color = "#00000"  # White
button_color = "#d1e1eb"  # Tomato
tweet_box_color = "#87CEFA"  # Light Sky Blue

# Set custom CSS style for the app
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
        .reportview-container .main .block-container {{
            max-width: 1200px;
            padding: 2rem;
            background-color: {tweet_box_color};
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
        }}
        .stTextInput input, .stButton button {{
            background-color: {button_color};
            color: {text_color};
            border-radius: 5px;
        }}
        .tweet-box {{
            background-color: {tweet_box_color};
            color: {text_color};
            padding: 10px;
            border-radius: 5px;
        }}
        .twitter-icon {{
            color: #1DA1F2;  /* Twitter Blue */
            font-size: 36px;
            margin-right: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Set app title and subtitle with Twitter icon
st.title(':bird: Twitter Sentiment Analysis :bird:')
st.markdown('*An Extraordinary App to Analyze Twitter Sentiments*', unsafe_allow_html=True)

# Add a text input widget for entering the tweet
tweet = st.text_input('Enter your tweet', max_chars=280)

# Add a button to trigger prediction
submit = st.button('Predict')

# Display prediction results and analyzed tweet
if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    with st.spinner('Predicting...'):
        time.sleep(2)  # Simulate prediction time for demonstration purposes
        prediction = model.predict([tweet])[0]
        st.success(f'Prediction: {prediction}')
        
        # Display the analyzed tweet in a small box
        st.markdown('### Analyzed Tweet:')
        st.markdown(f'<div class="tweet-box">{tweet}</div>', unsafe_allow_html=True)


# Add a footer with customization information
st.markdown('---')
st.markdown('Created with :heart: by Nisha', unsafe_allow_html=True)
