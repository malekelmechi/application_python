from flask import Flask, render_template, request
import os

app = Flask(__name__)

def create_empty_file(directory, filename):
    file_path = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as f:
        pass

@app.route('/')
def index():
    return """
    <form action="/create_file" method="get">
        <label for="directory">Répertoire : </label>
        <input type="text" id="directory" name="directory"><br><br>
        <label for="filename">Nom de fichier : </label>
        <input type="text" id="filename" name="filename"><br><br>
        <input type="submit" value="Créer le fichier">
    </form>
    """

@app.route('/create_file', methods=['GET'])
def create_file():
    directory = request.args.get('directory')
    filename = request.args.get('filename')
    
    if directory and filename:
        create_empty_file(directory, filename)
        return f"Le fichier '{filename}' a été créé dans le répertoire '{directory}'."
    else:
        return "Veuillez fournir à la fois le répertoire et le nom de fichier."

if __name__ == '__main__':
    app.run()

