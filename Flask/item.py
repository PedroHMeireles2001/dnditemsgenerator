class Item():
    def __init__(self, item, visual, sheet,itemUrl):
        self.item = item
        self.visual = visual
        self.sheet = sheet
        self.itemUrl = itemUrl

    def serialize(self):
        return {"item": self.item,
                "visual": self.visual,
                "sheet": self.sheet,
                "itemUrl": self.itemUrl}
