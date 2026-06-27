import requests
import re
from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/ahaber.m3u8')
def get_stream():
    try:
        # Doğru canlı yayın sayfasına yönlendiriyoruz
        url = "https://www.ahaber.com.tr/video/canli-yayin"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': '
