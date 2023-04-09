import argostranslate.package
import argostranslate.translate
import pathlib

from flask import Flask

app = Flask(__name__)

argostranslate.package.update_package_index()
    
package_path = pathlib.Path("translate-en_th-1_0.argosmodel")
argostranslate.package.install_from_path(package_path)

app.translate = argostranslate.translate