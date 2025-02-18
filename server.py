from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This function packages the request in text format and outputs a
        emotion dictionary for anger, disgust, fear, joy, and sadness and
        also the most dominant emotion
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check if text is missing or empty
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Handle response when None returned
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application 
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
