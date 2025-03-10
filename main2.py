from flask import Flask
import random
app = Flask(__name__)
facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]

def yazi_tura():
    para = random.randint(0, 1)
    if para == 0:
        return f"<h1>YAZI<h1>"
    else:
        return "<h1>TURA<h1>"
        
@app.route("/")
def index():
    return f'<a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/yazi_tura")
def yazi():
    return yazi_tura()


@app.route("/rastgele_gercek")
def facts():
    return f'<h1>{random.choice(facts_list)}</h1>'
app.run(debug=True)