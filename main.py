import requests
import re
from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/ahaber.m3u8')
def get_stream():
    try:
        url = "https://ahaber.com.tr"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        r = requests.get(url, headers=headers)
        match = re.search(r'(https://.*\.m3u8\?e=[^"\']*)', r.text)
        if match:
            return redirect(match.group(1), code=302)
    except:
        pass
    return "Yayın Bulunamadı", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
