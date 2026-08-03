from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'gizli_anahtar_buraya'  # Flash mesajları için gerekli #resend önerilir

@app.route('/')
def home():
    return render_template('index.html', title='Anasayfa')

@app.route('/about')
def about():
    return render_template('about.html', title='Hakkımızda')

@app.route('/services')
def services():
    return render_template('services.html', title='Hizmetler')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolyo')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        flash('Mesajınız başarıyla gönderildi!', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html', title='İletişim')

if __name__ == '__main__':
    app.run(debug=True)