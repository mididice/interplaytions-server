from rest_framework.decorators import api_view, authentication_classes, parser_classes, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from midi.integration import Integration
from midi.util import midi_file_to_raw

@api_view(['POST'])
def combine_all(request):
	ig = Integration()
	result = ig.united_midi('test_dir_name')
	raw_data = midi_file_to_raw(result)
	if result:
		response = HttpResponse(raw_data, content_type="audio/midi")
		return response
	else:
		return Response({"message":"error"})
	