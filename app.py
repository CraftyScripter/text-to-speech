from flask import Flask, jsonify, render_template, request
from methods import *

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False
app.json.sort_keys = False
tts = TextToSpeech()


# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
	return "GET"

# Route for getServices
@app.route('/getServices', methods=['GET'])
def get_services_route():
	_SERVICES_ = tts.services()
	return jsonify({"status":"success","services":_SERVICES_})

# Route for getVoices
@app.route('/getVoice', methods=['GET'])
def get_voice():
	# default_service = "StreamElements"
	# default_all_voice = False
	# all_voice = request.args.get('allVoice', default=default_all_voice, type=bool)
	service = request.args.get('service', default=None,type=str)
	if service:
		result_service = tts.voices(service=service)
		if result_service:
			return jsonify({"status":"success",service:tts.voices(service=service)})
		else:
			return jsonify({"status":"failed","error":"invalid service"})
	else:
		return jsonify({"status":"failed","error":"missing required parameter"})
	# return jsonify({service:_voices_})

@app.route('/getAllVoice',methods=['GET'])
def get_all_voice():
	_voices_ = tts.voices(all_voice=True)
	return jsonify({"status":"success","voices":_voices_})


# Route for getAudioLink
@app.route('/getAudioLink', methods=['GET'])
def get_audio_link_route():
	# default_text = "This is default text, which is converted to audio using Express Voice"
	# default_service = "StreamElements"
	# default_voice = "Brian"
	_SERVICE_ = request.args.get('service',type=str)
	VOICE = request.args.get('voice',type=str)
	TEXT = request.args.get('text',type=str)
	error_json = {}
	wrong_parameter = False
	if _SERVICE_ == None:
		error_json['status']="failed"
		error_json["service"]="missing"
	if VOICE == None:
		error_json['status']="failed"
		error_json["voice"]="missing"
	else:
		VOICE = VOICE.split()[0]
	if TEXT == None:
		error_json['status']="failed"
		error_json["text"]="missing"

	if len(error_json) != 0:
		if wrong_parameter == False:
			error_json["error"]="missing required parameter"
		return jsonify(error_json)
	
	else:

			
		audio_link = tts.audio_link(service=_SERVICE_,voice=VOICE,text=TEXT)
		if not audio_link:
			
			error_json["status"] = "failed"
			error_json["error"]="Invalid parameter"
			return error_json

		return jsonify({"status":"success",'audio_url':audio_link})


if __name__ == "__main__":
	app.run()
