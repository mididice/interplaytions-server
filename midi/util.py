import tensorflow as tf
import shutil
import os
from os import listdir
from os.path import isfile, join


def midi_file_to_raw(midi_file):
	with tf.gfile.Open(midi_file, 'rb') as f:
		midi_as_byte = f.read()
	return midi_as_byte


def raw_to_midi_file(raw, seq):
	with io.open('{}.mid'.format(seq), 'wb') as f:
		shutil.copyfileobj(raw, f)


def delete_midi_file(path):
	midifiles = [file_name for file_name in listdir(path) if isfile(join(path, file_name))]
	for f in midifiles:
		os.remove(join(path, f))
