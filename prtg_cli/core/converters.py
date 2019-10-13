import json

import xmltodict


def xml_to_json(content):
    return json.loads(json.dumps(xmltodict.parse(content)))
