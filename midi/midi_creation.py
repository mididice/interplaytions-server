import magenta
import tensorflow as tf
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.melody_rnn import melody_rnn_model
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2

import time
import os
import tempfile


class Samdasu():

    def create_midi(self):

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
        seconds_per_step = 60.0 / qpm / generator.steps_per_quarter
        total_seconds = 3

        primer_sequence = magenta.music.midi_file_to_sequence_proto("./midifile/test.mid")
        if primer_sequence.tempos and primer_sequence.tempos[0].qpm:
            qpm = primer_sequence.tempos[0].qpm
        if primer_sequence:
            input_sequence = primer_sequence
            # Set the start time to begin on the next step after the last note ends.
            last_end_time = (max(n.end_time for n in primer_sequence.notes)
                             if primer_sequence.notes else 0)
            # generate_section = generator_options.generate_sections.add(
            #     start_time=last_end_time + seconds_per_step,
            #     end_time=total_seconds)

        input_sequence = music_pb2.NoteSequence()
        input_sequence.tempos.add().qpm = qpm
        generate_section = generator_options.generate_sections.add(
            start_time=0,
            end_time=total_seconds)
        # generator_options.args['temperature'].float_value = FLAGS.temperature
        # generator_options.args['beam_size'].int_value = FLAGS.beam_size
        # generator_options.args['branch_factor'].int_value = FLAGS.branch_factor
        # generator_options.args[
        #       'steps_per_iteration'].int_value = FLAGS.steps_per_iteration
        # tf.logging.debug('input_sequence: %s', input_sequence)
        # tf.logging.debug('generator_options: %s', generator_options)

        # Make the generate request num_outputs times and save the output as midi
        # files.
        date_and_time = time.strftime('%Y-%m-%d_%H%M%S')
        digits = 1

        generated_sequence = generator.generate(input_sequence, generator_options)
        midi_filename = '%s_%s.mid' % (date_and_time, str(1).zfill(digits))
        midi_path = os.path.join("./midifile", midi_filename)
        magenta.music.sequence_proto_to_midi_file(generated_sequence, midi_path)

        tf.logging.info('Wrote %d MIDI files to %s',
                        "1", "midi folder")


    def create_midi_test(self, midi_data):

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
        seconds_per_step = 60.0 / qpm / generator.steps_per_quarter
        total_seconds = 3

        primer_sequence = magenta.music.midi_to_sequence_proto(midi_data)
        if primer_sequence.tempos and primer_sequence.tempos[0].qpm:
            qpm = primer_sequence.tempos[0].qpm
        if primer_sequence:
            input_sequence = primer_sequence
            # Set the start time to begin on the next step after the last note ends.
            last_end_time = (max(n.end_time for n in primer_sequence.notes)
                             if primer_sequence.notes else 0)
            # generate_section = generator_options.generate_sections.add(
            #     start_time=last_end_time + seconds_per_step,
            #     end_time=total_seconds)

        input_sequence = music_pb2.NoteSequence()
        input_sequence.tempos.add().qpm = qpm
        generate_section = generator_options.generate_sections.add(
            start_time=0,
            end_time=total_seconds)
        # generator_options.args['temperature'].float_value = FLAGS.temperature
        # generator_options.args['beam_size'].int_value = FLAGS.beam_size
        # generator_options.args['branch_factor'].int_value = FLAGS.branch_factor
        # generator_options.args[
        #       'steps_per_iteration'].int_value = FLAGS.steps_per_iteration
        # tf.logging.debug('input_sequence: %s', input_sequence)
        # tf.logging.debug('generator_options: %s', generator_options)

        # Make the generate request num_outputs times and save the output as midi
        # files.
        date_and_time = time.strftime('%Y-%m-%d_%H%M%S')
        digits = 1

        generated_sequence = generator.generate(input_sequence, generator_options)
        midi_filename = '%s_%s.mid' % (date_and_time, str(1).zfill(digits))
        midi_path = os.path.join("./midifile", midi_filename)
        magenta.music.sequence_proto_to_midi_file(generated_sequence, midi_path)

        tf.logging.info('Wrote %d MIDI files to %s',
                        "1", "midi folder")


    def create_midi(self, midi_data):

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
        seconds_per_step = 60.0 / qpm / generator.steps_per_quarter
        total_seconds = 3

        primer_sequence = magenta.music.midi_to_sequence_proto(midi_data)
        if primer_sequence.tempos and primer_sequence.tempos[0].qpm:
            qpm = primer_sequence.tempos[0].qpm
        if primer_sequence:
            input_sequence = primer_sequence
            # Set the start time to begin on the next step after the last note ends.
            last_end_time = (max(n.end_time for n in primer_sequence.notes)
                             if primer_sequence.notes else 0)
            # generate_section = generator_options.generate_sections.add(
            #     start_time=last_end_time + seconds_per_step,
            #     end_time=total_seconds)

        input_sequence = music_pb2.NoteSequence()
        input_sequence.tempos.add().qpm = qpm
        generate_section = generator_options.generate_sections.add(
            start_time=0,
            end_time=total_seconds)
        # generator_options.args['temperature'].float_value = FLAGS.temperature
        # generator_options.args['beam_size'].int_value = FLAGS.beam_size
        # generator_options.args['branch_factor'].int_value = FLAGS.branch_factor
        # generator_options.args[
        #       'steps_per_iteration'].int_value = FLAGS.steps_per_iteration
        # tf.logging.debug('input_sequence: %s', input_sequence)
        # tf.logging.debug('generator_options: %s', generator_options)

        generated_sequence = generator.generate(input_sequence, generator_options)
        
        output = tempfile.NamedTemporaryFile()
        magenta.music.midi_io.sequence_proto_to_midi_file(generated_sequence, output.name)
        output.seek(0)
        return output