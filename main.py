# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


# == LOAD DATA ==
fname = config['mne']
raw = mne.io.read_raw(fname)

# == GET CONFIG VALUES ==

sfreq   = config['sfreq']

# Advanced parameters
npad   = config['npad'] if config['npad'] else 'auto'
window = config['window'] if config['window'] else 'boxcar'
pad    = config['pad'] if config['pad'] else 'reflect_limited'
events = config['events'] if config['events'] else 'None'
stim_picks = config['stim_picks'] if config['stim_picks'] else 'None'

n_jobs = 1
verbose=None

# == RESAMPLE ==

raw.resample(sfreq, npad, window, stim_picks, n_jobs, events, pad, verbose)

# save mne/raw
raw.save(os.path.join('out_dir','raw.fif'))