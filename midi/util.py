import tensorflow as tf


def midi_file_to_raw(midi_file):
        with tf.gfile.Open(midi_file, 'rb') as f:
            midi_as_string = f.read()
        return midi_as_string