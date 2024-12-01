from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

CSV_FILE = "../reviews.csv"

def read_reviews():
    reviews = []
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reviews.append(row)
    except FileNotFoundError:
        with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "comment"])
            writer.writeheader()
    return reviews

def write_review(name, comment):
    with open(CSV_FILE, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "comment"])
        writer.writerow({"name": name, "comment": comment})

@app.route('/')
def home():
    reviews=read_reviews()
    return render_template('index.html', reviews=reviews)

# Informacijos apie produktą puslapis
@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        write_review(name, comment)
        return redirect(url_for('review'))
    return render_template('review.html')

# Paleidžiame serverį
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
