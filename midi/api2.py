from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from midi.midi_creation import Samdasu
from midi.parser import MidiParser
import json
import requests
from django.http import HttpResponse


@api_view(['GET', 'POST'])
@parser_classes((MidiParser,))
def generate_midi(request):
	if request.method == 'POST':
		print(request.body)
	cm = Samdasu()
	result = cm.create_midi(request.body) # create_midi2(여운승교수님 테스트용)
	response = HttpResponse(result, content_type="audio/midi")
	# return Response(result, headers=headers)
	return response


""" 
this api is for test api "/api/v2/"
"""
@api_view(['GET'])
def request_midi(request):
	url = 'http://localhost:8000/api/v2/'
	headers = {"content-type":"audio/midi"}
	cm = Samdasu()
	midi_str = cm.midi_file_to_sequence_proto('./midifile/test.mid')
	r = requests.post(url,data=midi_str, headers=headers)
	if r.status_code < 300:
		return Response({"message":"midi request completed"})
	else:
		return Response({"message":"midi request failed"})