import unittest
import magenta
import tensorflow as tf
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.melody_rnn import melody_rnn_model
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2
import os

steps_per_quarter = 4

def _steps_to_seconds(steps, qpm):
        return steps * 60.0 / qpm / steps_per_quarter


class MidiFileTest(unittest.TestCase):

    def test_create_midi_default(self):
        BUNDLE_NAME = 'attention_rnn'

        config = magenta.models.melody_rnn.melody_rnn_model.default_configs[BUNDLE_NAME]
        bundle_file = magenta.music.read_bundle_file(os.path.abspath(BUNDLE_NAME + '.mag'))
        steps_per_quarter = 4

        generator = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
            model=melody_rnn_model.MelodyRnnModel(config),
            details=config.details,
            steps_per_quarter=steps_per_quarter,
            # checkpoint=get_checkpoint(),
            bundle=bundle_file)

        qpm = 120
        generator_options = generator_pb2.GeneratorOptions()
        total_seconds = 4.0

        primer_sequence = magenta.music.midi_file_to_sequence_proto('180827_02_midi.mid')
        if primer_sequence.tempos and primer_sequence.tempos[0].qpm:
            qpm = primer_sequence.tempos[0].qpm
        
        generator_options = generator_pb2.GeneratorOptions()
         # Set the start time to begin on the next step after the last note ends.
        last_end_time = (max(n.end_time for n in primer_sequence.notes)
                     if primer_sequence.notes else 0)
        
        generator_options.generate_sections.add(
            start_time=last_end_time + _steps_to_seconds(1, qpm),
            end_time=total_seconds)
        generated_sequence = generator.generate(primer_sequence, generator_options)
        magenta.music.sequence_proto_to_midi_file(generated_sequence, 'new2.mid')

        tf.logging.info('Wrote %d MIDI files to %s',
            "1", "midi folder")

if __name__ == '__main__':
    unittest.main()