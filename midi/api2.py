from rest_framework.decorators import api_view, authentication_classes, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from midi.midi_creation import Samdasu
from midi.util import midi_file_to_raw
from midi.parser import MidiParser
import json
import requests
import os.path
from django.http import HttpResponse
from django.conf import settings


@api_view(['GET', 'POST'])
@parser_classes((MidiParser,))
def generate_midi(request):
	if request.method == 'POST':
		print(request.body)
	cm = Samdasu()
	result = cm.create_midi(request.body)
	response = HttpResponse(result, content_type="audio/midi")
	response['Content-Disposition'] = 'attachment; filename=generated.mid'
	# response['Content-Length'] = os.path.getsize(result)
	return response


@api_view(['POST'])
def generate_midi_one(request, seq, file_number):
	base_dir = settings.BASE_DIR
	basic_dir = os.path.join(base_dir, 'midibasic')
	generated_dir = os.path.join(base_dir, 'midifile')
	file_name = str(file_number)+'.mid'
	generate_file_name = str(seq)+'.mid'
	basic_file_path = os.path.join(basic_dir, file_name)
	generated_file_path = os.path.join(generated_dir, generate_file_name)
	# raw_midi = midi_file_to_raw(basic_file_path)
	cm = Samdasu()
	cm.create_midi_default(basic_file_path, generated_file_path)
	result = midi_file_to_raw(generated_file_path)
	response = HttpResponse(result, content_type="audio/midi")
	response['Content-Disposition'] = 'attachment; filename=generated.mid'	
	return response


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def request_auth(request, format=None):
	content = {
		'user' : unicode(request.user),
		'auth' : unicode(request.auth),
	}
	return Response(content)


@api_view(['GET'])
def request_test(request, seq, file_number):
	return Response({"file_number":file_number, "seq":seq})