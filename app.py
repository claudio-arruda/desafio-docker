from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def list_files():
    shared_dir = "/files_data"
    
    try:
        files = os.listdir(shared_dir)
        file_list = [f for f in files if os.path.isfile(os.path.join(shared_dir, f))]
        
        if not file_list:
            return "Nenhum arquivo encontrado\n"
        
        return "\n".join(file_list) + "\n"
    
    except Exception as e:
        return f"Erro ao listar arquivos: {str(e)}\n", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)