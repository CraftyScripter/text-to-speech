from flask import Flask, jsonify, render_template, request
from methods import *

app = Flask(__name__)

tts = TextToSpeech()


# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
	return "GET"

# Route for getServices
@app.route('/getServices', methods=['GET'])
def get_services_route():
	_SERVICES_ = tts.services()
	return jsonify(_SERVICES_)

# Route for getVoices
@app.route('/getVoices', methods=['GET'])
def get_voices_route():
	default_service = "StreamElements"
	default_all_voice = False
	all_voice = request.args.get('allVoice', default=default_all_voice, type=bool)
	service = request.args.get('service', default=default_service, type=str)
	
	voices = tts.voices(all_voice=all_voice, service=service)
	if all_voice:
		return jsonify(voices)
	return jsonify({service:voices})

# Route for getAudioLink
@app.route('/getAudioLink', methods=['GET'])
def get_audio_link_route():
	default_text = "This is default text, which is converted to audio using Express Voice"
	default_service = "StreamElements"
	default_voice = "Brian"
	_SERVICES_ = request.args.get('service',default=default_service,type=str)
	VOICE = request.args.get('voice',default=default_voice,type=str).split()[0]
	TEXT = request.args.get('text',default=default_text,type=str)
	audio_link = tts.audio_link(service=_SERVICES_,voice=VOICE,text=TEXT)
	return jsonify({'audio_url':audio_link})


if __name__ == "__main__":
	app.run()
