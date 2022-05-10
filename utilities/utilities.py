import base64
import json

import yaml
from constant.constant import Constant


class Utilities:
    @staticmethod
    def isParameterEmpty(param, paramName, dictResp):
        try:
            val = str(param.get(paramName)).strip()
            if val and not str(val).isspace() and len(str(val)) > 0 and val != 'None':
                return val
            else:
                dictResp["result"] = paramName + Constant.ERROR_MESSAGE

        except Exception:
            dictResp["result"] = str(paramName) + Constant.ERROR_MESSAGE

        return None

    @staticmethod
    def prepareResonpe(resDict, msgDict, flag, jsonifyObj):
        resDict.status = flag

        for key, val in msgDict.items():
            resDict[key] = val

        # Serializing json
        json_object = resDict.dumps()
        json_object = json.loads(json_object)

        # Based on jsonify object
        # return object
        if jsonifyObj is None:
            return json_object
        else:
            return jsonifyObj({"response": json_object})

    @staticmethod
    def readConfig(configPath):
        config = None
        try:
            with open(configPath, "r") as f:
                config = yaml.safe_load(f.read())
        except Exception:
            config = None

        return config

    @staticmethod
    def encode(message):
        base64_bytes = base64.b64encode(message)
        return base64_bytes

    @staticmethod
    def decode(message):
        message_bytes = base64.b64decode(message)
        return message_bytes