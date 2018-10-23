from rest_framework.decorators import api_view, authentication_classes, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from midi.creation import Samdasu
from midi.util import midi_file_to_raw, copy_basic_midi
from midi.parser import MidiParser
from midi.integration import convert_midi
import json
import requests
import os.path
from django.http import HttpResponse
from django.conf import settings
import tensorflow as tf


@api_view(['POST'])
@parser_classes((MidiParser,))
def generate_midi(request):
	if request.method == 'POST':
		print(request.body)
	cm = Samdasu()
	result = cm.create_midi(request.body)
	response = HttpResponse(result, content_type="audio/midi")
	response['Content-Disposition'] = 'attachment; filename=generated.mid'
	return response


@api_view(['POST'])
def generate_midi_one(request, seq, file_number):
	base_dir = settings.BASE_DIR
	basic_dir = os.path.join(base_dir, 'midibasic')
	generated_dir = os.path.join(base_dir, 'midifile')
	if not tf.gfile.Exists(generated_dir):
		tf.gfile.MakeDirs(generated_dir)
	file_name = str(file_number)+'.mid'
	generate_file_name = str(seq)+'a.mid'
	
	basic_file_path = os.path.join(basic_dir, file_name)
	generated_file_path = os.path.join(generated_dir, generate_file_name)
	
	cm = Samdasu()
	cm.create_midi_default(basic_file_path, generated_file_path)
	converted_file_path = convert_midi(seq, generated_file_path)
	result = midi_file_to_raw(converted_file_path)

	response = HttpResponse(result, content_type="audio/midi")
	response['Content-Disposition'] = 'attachment; filename=generated.mid'	
	return response


@api_view(['POST'])
def generate_midi_one_path(request, seq, file_number):
	base_dir = settings.BASE_DIR
	basic_dir = os.path.join(base_dir, 'midibasic')
	generated_dir = os.path.join(base_dir, 'midifile')
	if not tf.gfile.Exists(generated_dir):
		tf.gfile.MakeDirs(generated_dir)
	file_name = str(file_number)+'.mid'
	generate_file_name = str(seq)+'a.mid'
	
	basic_file_path = os.path.join(basic_dir, file_name)
	generated_file_path = os.path.join(generated_dir, generate_file_name)
	
	cm = Samdasu()
	cm.create_midi_default(basic_file_path, generated_file_path)
	converted_file_path = convert_midi(seq, generated_file_path)
	
	return Response(converted_file_path)


@api_view(['GET'])
def request_test(request, seq, file_number):
	return Response({"file_number":file_number, "seq":seq})