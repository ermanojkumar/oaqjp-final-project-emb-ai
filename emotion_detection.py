import requests

#URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#Input json: { "raw_document": { "text": text_to_analyze } }

def emotion_detector(text_to_analyze):
    """
    Analyze the input text and return the detected emotions.

    Args:
    text_to_analyze (str): The text to analyze.

    Returns:
    str: The API response containing emotion predictions.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=my_obj, headers=header, timeout=60)
    return response.text
