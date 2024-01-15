"""
Imports the modules
"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def emot_detector():
    """ function for showing the output """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if list(response.values())[0] is None:
        return "Invalid input ! Please try again!."
    list2 = list(response.keys())
    list3 = list(response.values())
    return ("For the given statement, the system response is "
    +f"{list2[0]}: {list3[0]}, {list2[1]}: {list3[1]},"
    +f" {list2[2]}: {list3[2]}, {list2[3]}: {list3[3]}"
    +f" and {list2[4]}: {list3[4]}."
    +f" The {list2[5].split('_')[0]} {list2[5].split('_')[1]} is {list3[5]}")

@app.route("/")

def render_index_page():
    """ function to render the html page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)
