import json


class DataParser:
    @staticmethod
    def parse_json(context):
        return json.loads(context)