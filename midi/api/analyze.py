from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from midi.parser import MidiParser
from midi.convert import midi_json 


@api_view(['POST'])
@parser_classes((MidiParser,))
def convert_json(request):
	midi_json()
	request.body;
