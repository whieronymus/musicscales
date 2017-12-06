# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:17:18 2017

@author: kygwilson
"""
# Intialize Dictionaries for Sharps and flats
sharps_dict = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7,
        'G#': 8, 'A': 9, 'A#': 10, 'B': 11, 0: 'C', 1: 'C#', 2: 'D', 3: 'D#',
        4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
        }

flats_dict = {
        'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7,
        'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11, 'Cb': 11, 0: 'C', 1: 'Db', 2: 'D',
        3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb',
        11: 'B'
        }

# Initialize empty string
scale_select = ''

# Initialize list of scales and intervals for various keys
scales_list = [
        'major', 'minor', 'minor pentatonic', 'major pentatonic', 'hirajoshi'
        ]
major_scale = [2, 4, 5, 7, 9, 11]
minor_scale = [2, 3, 5, 7, 8, 10]
major_pentatonic = [2, 4, 7, 9]
minor_pentatonic = [3, 5, 7, 10]
hirajoshi = [2, 3, 7, 8]

def scale_builder(tonic, scale, tonality):
    """Tonic is the root of a scale, expressed in a string with either a # or
    a b representing sharp or flat.
    returns a list filled with every note in a major scale built off of the
    tonic
    """
    # Initialize empty lists
    intervals = []
    notes = []

    # Checks the key to return from the correct dictionary
    if tonality == 'major':
        tonality_flats = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
        tonality_sharps = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
    elif tonality == 'minor':
        tonality_flats = ['D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab']
        tonality_sharps = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']

    # Searches tonic_flats in order to use the correct dictionary
    if tonic in tonality_flats:
        intervals.append(flats_dict[tonic])

        for i in scale:
            intervals.append(flats_dict[tonic]+i)

        for j in intervals:
            if j < 12:
                notes.append(flats_dict[j])
            else:
                octave_shift = j - 12
                notes.append(flats_dict[octave_shift])

    # Searches tonic_sharps in order to use the correct dictionary
    elif tonic in tonality_sharps:
        intervals.append(sharps_dict[tonic])

        for i in scale:
            intervals.append(sharps_dict[tonic]+i)

        for j in intervals:
            if j < 12:
                notes.append(sharps_dict[j])
            else:
                octave_shift = j - 12
                notes.append(sharps_dict[octave_shift])
    else:
        return 'Invalid Input'

    # Adjusts enharmonic equivalents to be within key
    if tonic == 'Gb':
        for (i, item) in enumerate(notes):
            if item == 'B':
                notes[i] = 'Cb'
    elif tonic == 'Cb':
        for (i, item) in enumerate(notes):
            if item == 'B':
                notes[i] = 'Cb'
            if item == 'E':
                notes[i] = 'Fb'
    elif tonic == 'F#':
        for (i, item) in enumerate(notes):
            if item == 'C':
                notes[i] = 'B#'
    elif tonic == 'C#':
        for (i, item) in enumerate(notes):
            if item == 'C':
                notes[i] = 'B#'
            if item == 'F':
                notes[i] = 'E#'

    return notes



while scale_select.lower() not in scales_list:
    scale_select = input('What scale? (Type "Help" for a list of options): ')
    if scale_select.lower() == 'help':
        print('Major, Minor, Minor Pentatonic, Major Pentatonic, Hirajoshi')


tonic_select = input('What note is the tonic of the scale?: ')

if scale_select.lower() == 'major':
    print(scale_builder(tonic_select, major_scale, 'major'))
elif scale_select.lower() == 'minor':
    print(scale_builder(tonic_select, minor_scale, 'minor'))
elif scale_select.lower() == 'major pentatonic':
    print(scale_builder(tonic_select, major_pentatonic, 'major'))
elif scale_select.lower() == 'minor pentatonic':
    print(scale_builder(tonic_select, minor_pentatonic, 'minor'))
elif scale_select.lower() == 'hirajoshi':
    print(scale_builder(tonic_select, hirajoshi, 'minor'))
else:
    print("Invalid Command")
