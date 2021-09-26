from model.predict import get_caption
import shutil
from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import vision
import requests
import os
import io
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/socialcurator-secret.json"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=200)
def read_root():
    return 'Server Healthy'


def save_file(file):
    with open('images/image.jpg', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


@app.post('/predict', status_code=200)
async def predict(response: Response, file: UploadFile = File(...)):
    try:
        save_file(file)
        caption = get_caption(f'images/{file.filename}')
        print(caption)

        client = vision.ImageAnnotatorClient()
        result = client.annotate_image(request={
            "image": vision.Image({"content": file.file.read()}),
            "features": [{'type_': vision.Feature.Type.LABEL_DETECTION}],
        })

        keywords = [keyword.description.lower() for keyword in result.label_annotations]
        print(f'keywords: {keywords}')

        hashtags = [generate_hashtags(keyword=keyword) for keyword in keywords]
        hashtags = [hashtag for item in hashtags for hashtag in item]
        hashtags.sort(key=lambda x: int(x['media_count']), reverse=True)
        print(f'hashtags: {hashtags}')

        return {"cation": caption, "hashtag": hashtags[:50]}
    except:
        response.status_code = 404
        return {"msg": "unexpected error"}


def generate_hashtags(keyword):
    # res = requests.get(f'https://www.instagram.com/web/search/topsearch?context=hashtag&query=${keyword}')
    # json_response = res.json()
    keyword = keyword.replace(" ", "-")
    file_path = f'./instagram_api_responses/{keyword}.json'
    res = []
    if os.path.isfile(file_path):
        json_file = open(file_path)
        data = json.load(json_file)

        for item in data['hashtags']:
            hashtag_object = item['hashtag']
            res.append({
                "name": hashtag_object['name'],
                "media_count": hashtag_object['media_count']
            })

    return res
