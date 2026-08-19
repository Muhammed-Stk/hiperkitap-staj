import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

istemci = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class Mesaj(BaseModel):
    mesajMetni: str


app = FastAPI()


kitaplar = [
    {'id': 1, 'isim': 'Kürk Mantolu Madonna', 'yazar': 'Sabahattin Ali'},
    {'id': 2, 'isim': 'İnce Mehmed', 'yazar': 'Yaşar Kemal'},
    {'id': 3, 'isim': 'Dublörün Dilemması', 'yazar': 'Murat Menteş'},
]


@app.get('/api/books')
def kitaplari_getir():
    return kitaplar

@app.get('/api/books/{kitap_id}')
def kitap_getir(kitap_id: int):
    for kitap in kitaplar:
        if kitap['id'] == kitap_id:
            return kitap
        
    return {'hata': 'aradığınız kitap bulunamadı.'}

@app.post('/api/chat')
async def sohbet(mesaj: Mesaj):
    yanit = await istemci.aio.models.generate_content(
        model='gemini-3.6-flash',
        contents=mesaj.mesajMetni,
        config=types.GenerateContentConfig(
            system_instruction="Sen HiperKitap uygulamasının yapay zeka asistanısın. Kullanıcılara sadece kitaplar, yazarlar ve edebiyat hakkında öneriler ver. Konu dışına çıkma."
        )
    ) 
    return {"cevap": yanit.text}