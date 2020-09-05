'''
Suppose we want to design a Python API for producing song lyrics. The MVP of our tool will programmatically produce the song lyrics for "Five Little Monkeys" (see the lyrics at the bottom of this document for an example).

In particular, we want:

a configurable AnimalVerse class that is capable of producing each stanza of the song on demand through the stanza method
a configurable Song class that produces sequential collections of stanzas for a given Verse type (we may want to produce songs with different verses in the future)
the AnimalVerse class should allow for different animals to be specified; note that the current feature request only applies to "monkey" but we expect other users to request new animals in the future. We expect to have to keep an explicit list of "approved" animals.
The following test suite describes the desired API. Your goal is to implement the two tested classes in such a way that all tests pass unchanged.

Keep in mind:

the use case and possible future changes described above
the tests do not specify argument names or defaults, but you should name your arguments
you may choose to implement utility functions or other classes not described by the tests
'''

class AnimalVerse:
    ''' '''
    approved_animals = {
        'monkey': 'monkeys',
        'mouse' : 'mice',
    }

    def __init__(self, animal='monkey'):
        if animal in self.approved_animals:
            self.animal = animal
        else:
            raise NameError('Unapproved animal')

    def stanza(self, number):
        if number < 0:
            raise ValueError('Stanza number must be an integer >= 0')
        elif number == 0:
            return (
                f"No little {self.approved_animals[self.animal]} jumping on the bed\n"
                "None fell off and bumped their head\n"
                "Mama called the doctor\n"
                "And the doctor said\n"
                f"Put those {self.approved_animals[self.animal]} straight back to bed!"
            )
        elif number == 1:
            return (
                f"1 little {self.animal} jumping on the bed\n"
                "It fell off and bumped his head\n"
                "Mama called the doctor\n"
                "And the doctor said\n"
                f"No more {self.approved_animals[self.animal]} jumping on the bed"
            )
        else:
            return (
                f"{number} little {self.approved_animals[self.animal]} jumping on the bed\n"
                "1 fell off and bumped his head\n"
                "Mama called the doctor\n"
                "And the doctor said\n"
                f"No more {self.approved_animals[self.animal]} jumping on the bed"
            )
    

class Song:
    def __init__(self, verse):
        self.verse = verse

    def lyrics(self, first_verse, last_verse):
        compiled_song = ''
        for i in reversed(range(last_verse, first_verse + 1)):
            compiled_song += self.verse.stanza(i)
            compiled_song += "\n"
        return compiled_song[:-1] # slicing compiled_song removes newline at end


class TestVerse:

    def test_standard_verse(self):
        expected = ("5 little monkeys jumping on the bed\n"
                    "1 fell off and bumped his head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "No more monkeys jumping on the bed")

        assert AnimalVerse().stanza(5) == expected

    def test_high_number_verse(self):
        expected = ("515 little monkeys jumping on the bed\n"
                    "1 fell off and bumped his head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "No more monkeys jumping on the bed")

        assert AnimalVerse().stanza(515) == expected

    def test_second_to_last_verse(self):
        expected = ("1 little monkey jumping on the bed\n"
                    "It fell off and bumped his head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "No more monkeys jumping on the bed")

        assert AnimalVerse().stanza(1) == expected

    def test_final_verse(self):
        expected = ("No little monkeys jumping on the bed\n"
                    "None fell off and bumped their head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "Put those monkeys straight back to bed!")

        assert AnimalVerse().stanza(0) == expected

    def test_animal_is_configurable(self):
        expected = ("1 little mouse jumping on the bed\n"
                    "It fell off and bumped his head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "No more mice jumping on the bed")

        assert AnimalVerse("mouse").stanza(1) == expected


class TestSong:

    def test_song_responds_to_verse(self):
        class SillyVerse:
            def stanza(self, x, *args, **kwargs):
                return f"This is silly verse {x}"

        song = Song(SillyVerse())
        assert song.lyrics(4, 3) == "This is silly verse 4\nThis is silly verse 3"

    def test_song_produces_verses(self):
        expected = ("1 little monkey jumping on the bed\n"
                    "It fell off and bumped his head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "No more monkeys jumping on the bed\n"
                    "No little monkeys jumping on the bed\n"
                    "None fell off and bumped their head\n"
                    "Mama called the doctor\n"
                    "And the doctor said\n"
                    "Put those monkeys straight back to bed!")

        song = Song(AnimalVerse())

        assert song.lyrics(1, 0) == expected

