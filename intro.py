import json
import sys
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'e6fanOmrVcNtQP1N2eja-3ZABk0Tz0F9WSpZE9j_BMo9'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/14f9e636-e4e4-44e5-9c14-99884dba3f3a'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

if ".flac" in sys.argv[1]:
    with open(join(dirname(__file__), './.', sys.argv[1]),
                'rb') as audio_file:
        res = stt.recognize(
            audio=audio_file,
            content_type='audio/flac',
        ).get_result()

        
        text = []
        for snip in res['results']:
            text.append(snip['alternatives'][0]['transcript'])
        with open('output.txt', 'w') as out:
            out.writelines(text)


elif ".wav" in sys.argv[1]:
    with open(join(dirname(__file__), './.', sys.argv[1]),
                'rb') as audio_file:
        res = stt.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='en-US_NarrowbandModel'
        ).get_result()

        
        text = []
        for snip in res['results']:
            text.append(snip['alternatives'][0]['transcript'])
        print(text)
        with open('output.txt', 'w') as out:
            out.writelines(text)