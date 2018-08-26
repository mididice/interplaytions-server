from rest_framework.parsers import BaseParser


class MidiParser(BaseParser):
    """
    Midi parser.
    """
    media_type = 'audio/midi'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a midi stream representing the body of the request.
        """
        return stream.read()