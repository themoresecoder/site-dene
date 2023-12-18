from flask import Flask
from logic import sifre_olustur

import random , time

app = Flask(__name__)

@app.route("/")
def merhaba():
    return f' <h1> merhaba </h1><a href="/rastgele_gercek"> Rastgele bir gerçeği görüntüle! </a><br/><a href="/şifre_oluştur"> Kendin için rastgele bir şifre oluştur </a>'


facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor." , 

"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir." , 
"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor." , 

"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır." , 

"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor." , 
"""Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. 
Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.""" , 

"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

@app.route("/rastgele_gercek")
def rastgele_gercek():
    return f'<h3>{random.choice(facts_list)}</h3><br/><a href="/rastgele_gercek"> Başka bir tane daha </a><br/><a href="/"> geri </a>'

@app.route("/şifre_oluştur")
def sifre():
    sifre = sifre_olustur()
    return f'<h2> İşte şifren </h2><br/><h3> {sifre} </h3><a href="/şifre_oluştur"> Başka bir tane daha </a><br/><a href="/"> geri </a>'

app.run(debug=True)

