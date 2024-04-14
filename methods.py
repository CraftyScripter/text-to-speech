import datetime
import requests
import json

class TextToSpeech():

	def __init__(self):
		self.request_url = "https://lazypy.ro/tts/request_tts.php"
		with open('voices.json','r') as voice_file:
			self.voices_data = json.load(voice_file)


	def services(self):
		self._services_ = list(self.voices_data.keys())
		return self._services_

	def voices(self,service=None,all_voice=False):

		if all_voice == True:
			return self.voices_data
		else:
			return self.voices_data.get(service)


	# def dynamic_time(self):
	# 	# Get the current date and time
	# 	current_datetime = datetime.datetime.now()

	# 	# Format the date and time as desired for the filename
	# 	formatted_date_time = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

	# 	return formatted_date_time


	def audio_link(self,text="",service='',voice=""):
		self.text = text
		self.service = service
		self.voice = voice

		self.payload = {
		"service":self.service,
		"voice":self.voice,
		"text":self.text
		}

		requests_session = requests.post(self.request_url, data=self.payload)

		if requests_session.status_code == 200:
			response_content = requests_session.json()
			if response_content['success'] == True:
				
				self.link = response_content['audio_url']
				return self.link


