import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL, headers, and input payload
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores from the dictionary
    # (The Watson API returns them under 'emotionPredictions' -> 'emotion')
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Create a dictionary of just the scores to find the max
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Find the key (emotion name) with the highest value
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the final requested output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }