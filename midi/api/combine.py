from rest_framework.decorators import api_view, authentication_classes, parser_classes, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from midi.integration import integrate_midi
from midi.util import midi_file_to_raw, delete_midi_file
from django.conf import settings
import os.path
import tensorflow as tf

@api_view(['POST'])
def combine_all(request):
	base_dir = settings.BASE_DIR
	generated_path = os.path.join(base_dir, 'midifile')
	result_path = os.path.join(base_dir, 'midiresult')
	if not tf.gfile.Exists(result_path):
		tf.gfile.MakeDirs(result_path)
	result = integrate_midi()
	raw_data = midi_file_to_raw(result)
	if raw_data:
		delete_midi_file(generated_path)
		delete_midi_file(result_path)
	if result:
		response = HttpResponse(raw_data, content_type="audio/midi")
		return response
	else:
		return HttpResponse(status=500)


@api_view(['POST'])
def combine_all_path(request):
	base_dir = settings.BASE_DIR
	generated_path = os.path.join(base_dir, 'midifile')
	result_path = os.path.join(base_dir, 'midiresult')
	if not tf.gfile.Exists(result_path):
		tf.gfile.MakeDirs(result_path)
	result = integrate_midi()
	if result:
		delete_midi_file(generated_path)
		# delete_midi_file(result_path)
	if result:
		return Response({"result":result})
	else:
		return HttpResponse(status=500)
	