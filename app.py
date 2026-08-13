from fastapi import FastAPI

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