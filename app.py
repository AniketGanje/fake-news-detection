from flask import Flask, render_template, request
app = Flask(__name__)
def check_fake(news):
    fake_words = ["shocking", "click here", "you wont believe", "viral", "100% true", "lottery"]
    news_low = news.lower()
    for w in fake_words:
        if w in news_low:
            return "FAKE News!"
    return "REAL News"
@app.route('/', methods=['GET','POST'])
def home():
    prediction = None
    if request.method == 'POST':
        news = request.form['news']
        if news.strip()!="":
            prediction = check_fake(news)
    return render_template('index.html', prediction=prediction)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
