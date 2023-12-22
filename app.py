from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    images = ['example_image.png', 'example_image2.png']

    return render_template('index.html', images=images)

@app.route('/redirect')
def redirect_to_another_site():
    return redirect('https://www.example.com')

if __name__ == '__main__':
    app.run(debug=True)
