import requests
import json

def emotion_detector(text_to_analyze):
    '''This method analyses text and detects the emotion
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post( url, json = myobj, headers = header)

    if response.status_code == 200:
        formatted_reponse = json.loads(response.text)
        emotion_values = formatted_reponse['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_values,key=emotion_values.get)
        
        result = {
            'anger': emotion_values['anger'],
            'disgust': emotion_values['disgust'],
            'fear': emotion_values['fear'],
            'joy': emotion_values['joy'],
            'sadness': emotion_values['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None      
        }    

    return result
