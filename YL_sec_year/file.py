N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

class Melody:
    def __init__(self, notes=''):
        self.notes = [note.__str__() for note in notes]
        self.music = self.notes

    def __len__(self):
        return len(self.notes)

    def __repr__(self):
        return ' '.join(self.notes)

    def __rshift__(self, other):


    def replace_last(self,note):
        self.music[-1] = note
        self.notes[-1] = note.__str__()

    def remove_last(self):
        self.music = self.music[:-1]
        self.notes = self.notes[:-1]

    def clear(self):
        self.music = []
        self.notes = []

    def append(self, note):
        self.music.append(note)
        self.notes.append(note.__str__())


class Note():
    def __init__(self, note='до', is_long=False):
        self.ind = PITCHES.index(note)
        self.note = note
        self.gl = 'оэиао'
        self.len = is_long

    def __str__(self):
        if self.len:
            tetr = {
                'до': 'до-о',
                'ре': 'ре-э',
                "ми": "ми-и",
                "фа": "фа-а",
                "соль": "со-оль",
                "ля": "ля-а",
                "си": "си-и",
            }
            return tetr[self.note]
        else:
            return self.note

    def __eq__(self, other):
        return self.note == other

    def __gt__(self, other):
        return self.ind > other.ind

    def __ge__(self, y):
        return self.ind >= y.ind

    def __rshift__(self, y):
        if self.len:
            ret = Note(PITCHES[(PITCHES.index(self.note) + y) % 7], self.len)
            ret.__str__()
            return ret
        else:
            return Note(PITCHES[(PITCHES.index(self.note) + y) % 7], self.len)

    def __lshift__(self, y):
        if self.len:
            ret = Note(PITCHES[(PITCHES.index(self.note) - y) % 7], self.len)
            ret.__str__()
            return ret
        else:
            return Note(PITCHES[(PITCHES.index(self.note) - y) % 7], self.len)

    def get_interval(self, other):
        return INTERVALS[abs(PITCHES.index(self.note) - PITCHES.index(other.note))]


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __str__(self):
        return super().__str__()


class NoteWithOctave(Note):
    def __init__(self, note='до', oct='первая октава', is_long=False):
        self.oct = oct
        super().__init__(note, is_long)

melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)