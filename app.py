from flask import Flask, request, jsonify, render_template
from bard_api import ask_bard

import fitz  # PyMuPDF for PDF processing

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    response = ask_bard(user_input)
    return jsonify({"response": response})

@app.route("/summarize_pdf", methods=["POST"])
def summarize_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files["file"]
    pdf_path = f"uploads/{pdf_file.filename}"
    pdf_file.save(pdf_path)

    extracted_text = extract_text_from_pdf(pdf_path)
    summary = ask_bard(f"Summarize this: {extracted_text}")
    
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
