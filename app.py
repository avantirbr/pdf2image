from flask import Flask, request, send_file
from pdf2image import convert_from_bytes
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    try:
        # Lê os bytes do arquivo PDF
        pdf_bytes = file.read()
        
        # Converte a primeira página do PDF para uma imagem PNG em memória
        images = convert_from_bytes(pdf_bytes, fmt='png', first_page=1, last_page=1)
        
        if images:
            # Salva a imagem em um buffer de bytes
            img_io = io.BytesIO()
            images[0].save(img_io, 'PNG')
            img_io.seek(0)
            
            # Retorna a imagem como resposta
            return send_file(img_io, mimetype='image/png')
        else:
            return "Could not convert PDF to image", 500

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
