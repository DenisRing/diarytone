import streamlit as st
import plotly.express as px
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import glob

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

#looping through to grab sentiment scores
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

#Getting the dates in order, you dont really join them except for on the chart
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.write("Charting sentiment with diary entries")

st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels ={"x": "Date", "y": "Positivity" })
st.plotly_chart(pos_figure)


st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels ={"x": "Date", "y": "Negativity" })
st.plotly_chart(neg_figure)


