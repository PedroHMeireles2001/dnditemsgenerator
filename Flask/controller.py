from main import app
from flask import request, jsonify
import GPTService as gpt
from item import Item


@app.route("/healthcheck", methods=['GET'])
def heatlhcheck():
    return jsonify({"health": True})


@app.route("/generate", methods=['GET', ])
def generate():
    itemDescription = request.args.get('item', default="", type=str)
    generateImage = request.args.get('image', default='True', type=str).lower() == 'true'
    generateImageResolution = request.args.get('imageRes', default="1024x1024", type=str)
    imageQuality = request.args.get('quality', default='standard', type=str).lower()
    model = request.args.get('model', default='gpt-3.5-turbo', type=str).lower()
    creativity = request.args.get('temperature', default=1, type=float)

    print(itemDescription)
    print(model)
    print(creativity)
    print(generateImage)
    if generateImage:
        print(generateImageResolution)
        print(imageQuality)

    if not itemDescription or itemDescription == "":
        itemDescription = gpt.generateItemDescription(model,creativity)

    visual = gpt.generateVisuals(itemDescription,model,creativity)
    sheet = gpt.generateSheet(itemDescription,model,creativity)
    itemUrl = None
    if generateImage:
        itemUrl = gpt.dalle(visual,generateImageResolution,imageQuality)
    item = Item(itemDescription, visual, sheet, itemUrl)
    return jsonify(item.serialize())


def makeErrorResponse(code=400, msg=""):
    resposta = jsonify({'erro': msg})
    resposta.status_code = code
    return resposta
