from flask import Flask, request, current_app
from flask_cors import CORS

import argostranslate.package
import argostranslate.translate
import pathlib


def setup_translation_module():
    argostranslate.package.update_package_index()
        
    package_path = pathlib.Path("translate-en_th-1_0.argosmodel")
    argostranslate.package.install_from_path(package_path)

    return argostranslate.translate

app = Flask(__name__)
cors = CORS(app)
app.translate = setup_translation_module()

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    if not request.is_json:
        return "Content type is not supported", 415
    
    term = data["term"]
    if not term:
        return "No term specified for translation", 400
    
    from_code = "en"
    to_code = "th"
    
    translatedText = current_app.translate.translate(term, from_code, to_code)
    return {
        "value": term,
        "translation": translatedText
    }