from transformers import YolosFeatureExtractor, YolosForObjectDetection
from PIL import Image
import requests
import streamlit as st
import re


# Заголовок страницы
st.title("Object detection YOLOS model Web App")

# Получение имени пользователя и вывод приветствия
name = st.text_input("Enter your name", "")
st.write(f"Hello {name}!")


url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)


feature_extractor = YolosFeatureExtractor.from_pretrained('hustvl/yolos-tiny')
model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')


inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)


# model predicts bounding boxes and corresponding COCO classes
logits = outputs.logits
bboxes = outputs.pred_boxes
