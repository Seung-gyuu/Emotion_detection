''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emo_detector():
    '''This function receives text input, analyzes its emotion, and returns the emotion scores 
    for anger, disgust, fear, joy, sadness, and the dominant emotion.
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return "Invalid text! Please try again!!"

    # Return a formatted string with the emotion labels and scores, breaking it into multiple lines
    return f"""
        For the given statement, the system response is:
        'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 
        'joy': {joy}, 'sadness': {sadness}.
        The dominant emotion is: {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
