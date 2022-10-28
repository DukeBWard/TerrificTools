from json import tool


class tools:
    def __init__(self, barcode, borrowed, description, tool_name, userid, category):
        self.barcode = barcode
        self.borrowed = borrowed
        self.description = description
        self.tool_name = tool_name
        self.userid = userid
        self.category = category
