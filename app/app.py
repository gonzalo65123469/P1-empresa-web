from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Página "Quiénes Somos"
@app.route('/about')
def about():
    return render_template('about.html')

# Página de Servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Página de Noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Página de Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        return f"Gracias {nombre}, hemos recibido tu mensaje."
    return render_template('contact.html')

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
