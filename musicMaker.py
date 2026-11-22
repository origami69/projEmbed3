from fractions import Fraction
import math
from fractions import Fraction
from music21 import converter

def main():
    #use https://github.com/Audiveris/audiveris to convert the music PDF to a musicXML and  put it through this script
    score = converter.parse(".\militurtle.mxl")
    #this is for converting piano or a different trumpet types to BFLAT since I use BFLAT trumpet as my standard
    offset = 0
    melody = score.parts[0]
    notes = []
    beats = []
    for element in melody.flatten().notesAndRests:
        if element.isRest:
            notes.append(0)
        elif element.isChord: #if chord then get largest
            midi_note = element.pitches[-1].midi - offset
            note_index = midi_note - 48 + 1
            if 1 <= note_index <= 48:
                notes.append(note_index)
                beats.append(element.duration.quarterLength)
            else:
                print("note has been skipped feel free to expand my array")
        else:
            #bflat trumpet
            midi_note = element.pitch.midi - offset + 1
            #MIDI 48
            note_index = midi_note - 48
            if 1 <= note_index <= 48: #our buzzers range based on notees feel free to extend
                notes.append(note_index)
                beats.append(element.duration.quarterLength)
            else:
                print("note has been skipped feel free to expand my array")

    def lcm(a, b): #least common multipleso we can make all the beats a whole number
        return abs(a * b) // math.gcd(a, b)
    beat_resolution = 1
    for beat in beats:
        beat_fraction = Fraction(str(beat))
        beat_resolution = lcm(beat_resolution, beat_fraction.denominator)
    index = 0
    for beat in beats:
        beat *= beat_resolution
        beats[index] = int(beat)
        index = index+1
    print(notes)
    print(beats)
    print(beat_resolution)
    print(index)

if __name__ == "__main__":
    main()
