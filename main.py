from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/bikes')
def bikes():
  return render_template('bikes.html')

@app.route('/seguro')
def seguro():
  return render_template('segurogratis.html')

@app.route('/sobre')
def sobrenos():
  return render_template('sobrenos.html')

@app.route('/agradecimento')
def agradecimento():
  return render_template('agradecimento.html')

@app.route('/contato')
def contato():
  return render_template('contato_clientes.html')

@app.route('/envio', methods=['GET', 'POST'])
def envio():
  return render_template('envio.html')

@app.route('/suporte')
def suporte():
  return render_template('suporte.html')

@app.route('/avaliacoes')
def avaliacoes():
  clientes = [ {"nome": "Cliente_1", "nota": 10, "comentario": "A bike Oggi Bigwhell 7.5 é a melhor do mercado atualmente, estou indo muito bem nas competições."},
              {"nome": "Clinte_2", "nota": 6, "comentario": "A Bike Oggi 7.0 poderia vir com uma geometria mais atualizada do quadro, não vale o valor que paguei por ela."},
              {"nome": "Cliente_3", "nota": 9, "comentario": "Experência indescritível, melhorou 100% meu pedal. Loja confiável, podem comprar sem medo."},
              {"nome": "Cliente_3", "nota": 5, "comentario": "Bike chegou com defeito na gancheira, não consigo regular as marchas, acionei a garantia e espero que resolvam o mais rápido possível."},
              {"nome": "Cliente_4", "nota": 10, "comentario": "Oggi 7.5, de longe é a melhor! Obrigado pelo atendimento!"},
              {"nome": "Cliente_5", "nota": 9, "comentario": "Oggi Bikes, a melhor marca Nacional de Bikes!"},
             ]
  return render_template('avaliacoes.html', clientes=clientes)
  
  
app.run(host='0.0.0.0', port=81)