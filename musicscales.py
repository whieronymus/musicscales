# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:17:18 2017

@author: kygwilson
"""
# Intialize Dictionaries for Sharps and flats
sharps_dict = {
        'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#': 8,
        'A':9, 'A#':10, 'B':11, 0:'C', 1:'C#', 2:'D', 3:'D#', 4:'E', 5:'F', 
        6:'F#', 7:'G', 8:'G#', 9:'A', 10:'A#', 11:'B'
        }

flats_dict = {
        'C':0, 'Db':1, 'D':2, 'Eb':3, 'E':4, 'F':5, 'Gb':6, 'G':7, 'Ab':8, 
        'A':9, 'Bb':10, 'B':11, 0:'C', 1:'Db', 2:'D', 3:'Eb', 4:'E', 5:'F',
        6:'Gb', 7:'G', 8:'Ab', 9:'A', 10:'Bb', 11:'B'
        }

tonic_flats = ['F' 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
tonic_sharps = ['C', 'G', 'D', 'A', 'E', 'B' 'F#', 'C#']

def major_scale (tonic):
    """Tonic is the root of a scale, expressed in a string with either a # or
    a b representing sharp or flat.
    returns a list filled with every note in a major scale built off of the 
    tonic
    """
    major_intervals = []
    major_notes = []

    if tonic in tonic_flats:
        major_intervals.append(flats_dict[tonic])
    
        for i in [2,4,5,7,9,11]:
            major_intervals.append(flats_dict[tonic]+i)
        
        for j in major_intervals:
            if j < 12:
                major_notes.append(flats_dict[j])
            else:
                octave_shift = j - 12
                major_notes.append(flats_dict[octave_shift])

    elif tonic in tonic_sharps:
        major_intervals.append(sharps_dict[tonic])
    
        for i in [2,4,5,7,9,11]:
            major_intervals.append(sharps_dict[tonic]+i)
        
        for j in major_intervals:
            if j < 12:
                major_notes.append(sharps_dict[j])
            else:
                octave_shift = j - 12
                major_notes.append(sharps_dict[octave_shift])
    else:
        return 'Invalid Input'
            
    return major_notes
    
    