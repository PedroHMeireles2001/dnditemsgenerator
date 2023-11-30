from main import app
from flask import request, jsonify
import GPTService as gpt
from item import Item

@app.route("/healthcheck",methods=['POST','GET'])
def heatlhcheck():
    return jsonify({health: True})

@app.route("/generate",methods=['POST',])
def generate():
    itemDescription = request.form['item']
    if not itemDescription:
        return makeErrorResponse(msg="No item")
    visual = gpt.generateVisuals(itemDescription)
    sheet = gpt.generateSheet(itemDescription)
    itemUrl = gpt.dalle(visual)
    item = Item(itemDescription,visual,sheet,itemUrl)
    return jsonify(item.serialize())

@app.route("/surprise",methods=['POST','GET'])
def generateSurprise():
    itemDescription = gpt.chatGPT("", "generate just one name idea for magic items. The exit should only be the magic item. use only plain text, without bold or anything else")
    visual = gpt.generateVisuals(itemDescription)
    sheet = gpt.generateSheet(itemDescription)
    itemUrl = gpt.dalle(visual)
    item = Item(itemDescription, visual, sheet, itemUrl)
    return jsonify(item.serialize())

@app.route("/image",methods=['POST',])
def image():
    prompt = request.form['prompt']
    if not prompt:
        return makeErrorResponse(msg="No item")
    item = gpt.dalle(prompt)
    return jsonify(item)

def makeErrorResponse(code=400, msg=""):
    resposta = jsonify({'erro': msg})
    resposta.status_code = code
    return resposta