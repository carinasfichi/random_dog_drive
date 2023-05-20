import json
import requests
headers = {
    "Authorization": "Bearer ya29.a0AWY7Ckn1oUBc5yZyfsD5iQ-z8vzpMhAJGe5qi61mBZDlRSw4yoMz8uD5dJtnccZjxzJxNS3dRuO_wRur0o-fnQZ7qD2MRvHTYAMTWufpwtfqEiQkEDbIbIc6ch_PBgT3y3z69PfYexasL0Pi2b_a_6n3mCB3aCgYKAdsSARASFQG1tDrpDmc_mdacQtjbIsIhTRD6Qg0163"
}

'NUMELE POZEI SI CALEA SPECIFICA DRIVE ULUI'
para = {
    "name": "test.jpg",
    "parents": ["1shSFPdrHTzC05kRuVuLr0HETQWrFlVPo"]
}

'LOCATIE POZEI DIN CALCULATOR'
files = {
    'data': ('metadata', json.dumps(para), 'application/json;charset=UTF-8'),
    'file': ('test.jpg', open('Poze/caine.jpg', 'rb'), 'image/jpeg')
}

'TESTAREA INCARCARII'
response = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart", headers=headers, files=files)
if response.status_code == 200:
    print("File uploaded successfully")
else:
    print("failed to upload files")
