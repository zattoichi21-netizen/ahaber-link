import requests
import re
from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/ahaber.m3u8')
def get_stream():
    try:
        # Doğru A Haber canlı yayın sayfası
        url = "https://ahaber.com.tr"
        
        # Tarayıcı gibi görünmek için gerekli başlıklar
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://ahaber.com.tr',
            'Origin': 'https://ahaber.com.tr'
        }
        
        session = requests.Session()
        r = session.get(url, headers=headers, timeout=10)
        
        # Sayfa içerisindeki güncel m3u8 linkini aratıyoruz
        match = re.search(r'(https://[^\s"\']*?\.m3u8\?e=[^\s"\']*)', r.text)
        
        if match:
            clean_url = match.group(1).replace('\\', '')
            # IPTV oynatıcıyı otomatik olarak güncel linke yönlendirir
            return redirect(clean_url, code=302)
            
    except Exception as e:
        return f"Hata olustu: {str(e)}", 500
        
    return "Yayin Linki Bulunamadi. Kaynak sayfa yapisi degismis olabilir.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
