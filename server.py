from flask import Flask, render_template

app = Flask(__name__)

# Pagrindinis puslapis
@app.route('/')
def home():
    return render_template('index.html')

# Informacijos apie produktą puslapis
@app.route('/product')
def product():
    return render_template('product.html')
    
# Paleidžiame serverį
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
