import requests

import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }
    response = requests.post( url, json = myobj, headers=header )
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        dictionary = formatted_response['emotionPredictions'][0]['emotion']
        list1 = []
        for i in dictionary.keys():
            if dictionary[i] == max(dictionary.values()):
                list1.append(i)
        dictionary['dominant_emotion'] = list1[0]
        return dictionary
    elif response.status_code == 400:
        dictionary = dict()
        dictionary[None] = None
        return dictionary