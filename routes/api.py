from flask import Blueprint, jsonify, request, Response
from constant.constant import Constant
from logger.logger import exc_logger, logger
from objdict import ObjDict
from main import Main
from utilities.utilities import Utilities

app = Blueprint('api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return app


@app.route('/')
def init():
    dataDict, dictResp = ObjDict(), {}
    dictResp['result'] = f"{Constant.PROJECT_NAME} api's are integrated successfully"
    dictResp['version'] = 'v1.0.0'
    logger.info("TSP api's are working fine.")

    # Serializing json
    return Utilities.prepareResonpe(dataDict, dictResp, True, jsonify)

@app.route('/api/v1/text/speech', methods = ['POST'])
def textToSpeech():
    dataDict, dictResp, flag = ObjDict(), {}, False

    logger.info(f'{Constant.PROJECT_NAME} - execute text-to-speech Api')

    # post parameter send by client
    param = request.get_json(silent=True)

    # Validate User Name
    uName = Utilities.isParameterEmpty(param, 'user_name', dictResp)
    if uName is None:
        logger.error('user_name' + Constant.ERROR_MESSAGE)
        return Utilities.prepareResonpe(dataDict, dictResp, flag, jsonify)

    language = Utilities.isParameterEmpty(param, 'language', dictResp)
    if language is None:
        language = 'en'

    text = Utilities.isParameterEmpty(param, 'text', dictResp)
    if text is None:
        logger.error('text' + Constant.ERROR_MESSAGE)
        return Utilities.prepareResonpe(dataDict, dictResp, flag, jsonify)

    try:
        path = Main.getInstance().text_to_speech(uName, text, language)
        def generate(path):
            with open(path, "rb") as fmp3:
                data = fmp3.read(1024)
                while data:
                    yield data
                    data = fmp3.read(1024)
        return Response(generate(path), mimetype="audio/mpeg3")
    except Exception as e:
        dictResp['result'] = str(e)
        logger.error(str(e))

    return Utilities.prepareResonpe(dataDict, dictResp, flag, jsonify)

@app.route('/api/v1/speech/text', methods = ['POST'])
def speechToText():
    dataDict, dictResp, flag = ObjDict(), {}, False

    logger.info(f'{Constant.PROJECT_NAME} - execute text-to-speech Api')

    # post parameter send by client
    param = request.get_json(silent=True)

    # Validate User Name
    uName = Utilities.isParameterEmpty(param, 'user_name', dictResp)
    if uName is None:
        logger.error('user_name' + Constant.ERROR_MESSAGE)
        return Utilities.prepareResonpe(dataDict, dictResp, flag, jsonify)

    language = Utilities.isParameterEmpty(param, 'language', dictResp)
    if language is None:
        language = 'en'

    try:
        path = Main.getInstance().text_to_speech(uName, language)
        def generate(path):
            with open(path, "rb") as fmp3:
                data = fmp3.read(1024)
                while data:
                    yield data
                    data = fmp3.read(1024)
        return Response(generate(path), mimetype="audio/mpeg3")
    except Exception as e:
        dictResp['result'] = str(e)
        logger.error(str(e))

    return Utilities.prepareResonpe(dataDict, dictResp, flag, jsonify)

