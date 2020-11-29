class NoteError(Exception):
    """Ошибка с написанием нот"""
    pass


class MoodError(Exception):
    """Ошибка с выбором лад"""
    pass


class MelodyNote:
    """Класс нотной тетради"""

    """Инициализация класса MelodyNote"""
    def __init__(self, songs=[]):
        self.__songs = songs
        __open = False

    """добавдение песен в тетрадь"""
    def __lshift__(self, other):
        if isinstance(other, Song):
            return self.__songs.append(other)
        else:
            raise NoteError("В тетрадь можно добавить только песни")

    """"Взятие элемента по индексу через obj[i]"""
    def __getitem__(self, item):
        if not self.__open:
            raise Exception("Тетрадь закрыта")
        return self.__songs[item]

    """"Итерация тетради"""
    def __iter__(self):
        self.__open = True
        return EnumSong(self.__songs)

    """"Вывод песен"""
    def __enter__(self):
        self.__open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Song:
    """Класс песни"""

    """Инициализация класса Song"""
    def __init__(self, song=[]):
        self.__song = song

    """Добавдение нот в песню"""
    def __lshift__(self, other):
        if isinstance(other, Note):
            return self.__song.append(other)
        else:
            raise NoteError("В песню можно добавлять только ноты")

    """"Взятие элемента по индексу через obj[i]"""
    def __getitem__(self, item):
        return self.__song[item]

    """"Изменение лада в песне"""
    def changemood(self, mood, start: int = 1, end: int = 0):
            if end == 0:
                end = len(self.__song) - 1
            for i in range(start - 1, end + 1):
                self.__song[i].mood = mood

    """Проиграование песни"""
    def play(self):
        print("Start playing song")
        for i in self.__song:
            if i.mood == 'major':
                print(f"{i.sign.upper()}", end=" ")
            else:
                print(f"{i.sign}", end=" ")
        print('\n' "Song ended" '\n')

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        pass

    @property
    def song(self):
        return self.__song

    def __iter__(self):
        return EnumNoteSign(self.__song)

    """Подсчёт элементов разных ладов"""
    def count(self):
        major = 0
        for i in self.__song:
            if i.mood == 'major':
                major += 1
        return major

    """"Перегрузка  < """
    def __lt__(self, other):
        if len(self.__song) < len(other.__song):
            print("1 песня меньше" '\n')
        elif self.count() < other.count() and len.self.__song == len.other.__song:
            print("1 песня меньше" '\n')
        else:
            print("2 песня меньше" '\n')

    """"Перегрузка  > """

    def __gt__(self, other):
        if len(self.__song) > len(other.__song):
            print("1 песня больше" '\n')
        elif self.count() > other.count() and len.self.__song == len.other.__song:
            print("1 песня больше" '\n')
        else:
            print("2 песня больше" '\n')

    """"Перегрузка  <= """

    def __le__(self, other):
        if len(self.__song) <= len(other.__song):
            print("1 песня меньше или равна" '\n')
        elif self.count() <= other.count() and len.self.__song == len.other.__song:
            print("1 песня меньше или равна" '\n')
        else:
            print("2 песня меньше или равна" '\n')

    """"Перегрузка  >= """

    def __ge__(self, other):
        if len(self.__song) >= len(other.__song):
            print("1 песня больше или равна" '\n')
        elif self.count() >= other.count() and len.self.__song == len.other.__song:
            print("1 песня больше или равна" '\n')
        else:
            print("2 песня больше или равна" '\n')

    def __eq__(self, other):
        if self.count() == other.count() and len.self.__song == len.other.__song:
            print("Песни равны" '\n')
        else:
            print("Песни не равны" '\n')


class Note:
    """"Класс нот"""

    Notes = ["c", "d", "e", "f", "g", "a", "h"]
    MusicalMood = ["major", "minor"]

    """"Инициализация класса Note"""
    def __init__(self, note_sign, musical_mood="major"):
        if note_sign in Note.Notes and musical_mood in Note.MusicalMood:
            self.notesign = note_sign
            self.musicalmood = musical_mood
        else:
            raise NoteError("Такой ноты не существует")

    """"Блокировка смены ноты"""
    @property
    def sign(self):
        return self.notesign

    """"Смена лада"""
    @property
    def mood(self):
        return self.musicalmood

    @mood.setter
    def mood(self, musical_mood):
        if musical_mood in Note.MusicalMood:
            self.musicalmood = musical_mood
        else:
            raise MoodError("Такого лада не существует")

    """"Перегрузка  < """
    def __lt__(self, other):
        if Note.Notes.index(self.notesign) < Note.Notes.index(other.notesign):
            print("1 нота меньше" '\n')
        elif self.mood == "minor" and self.mood == "major" and Note.Notes.index(self.notesign) == Note.Notes.index(other.notesign):
            print("1 нота меньше" '\n')
        else:
            print("2 нота меньше" '\n')

    """"Перегрузка  > """

    def __gt__(self, other):
        if Note.Notes.index(self.notesign) > Note.Notes.index(other.notesign):
            print("1 нота больше" '\n')
        elif self.mood != "minor" and other.mood == "minor" and Note.Notes.index(self.notesign) == Note.Notes.index(other.notesign):
            print("1 нота больше" '\n')
        else:
            print("2 нота больше" '\n')

    """"Перегрузка  <= """

    def __le__(self, other):
        if Note.Notes.index(self.notesign) <= Note.Notes.index(other.notesign):
            print("1 нота меньше или равна" '\n')
        elif self.mood == "minor" and (other.mood == "minor" or other.mood != "minor") and Note.Notes.index(self.notesign) == Note.Notes.index(other.notesign):
            print("1 нота меньше или равна" '\n')
        else:
            print("2 нота меньше или равна" '\n')

    """"Перегрузка  >= """
    def __ge__(self, other):
        if Note.Notes.index(self.notesign) < Note.Notes.index(other.notesign):
            print("1 нота больше или равна" '\n')
        elif self.mood == "minor" and (other.mood == "minor" or other.mood != "minor") and Note.Notes.index(self.notesign) == Note.Notes.index(other.notesign):
            print("1 нота больше или равна" '\n')
        else:
            print("2 нота больше или равна" '\n')

    def __eq__(self, other):
        if Note.Notes.index(self.notesign) == Note.Notes.index(other.notesign) and self.mood == other.mood:
            print("ноты равны" '\n')
        else:
            print("ноты не равны" '\n')


class EnumNoteSign:
    """"класс для итерации нот"""
    def __init__(self, song):
        self.__song = song
        self.__limit = len(self.__song)
        self.__simv = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__simv >= self.__limit:
            raise StopIteration
        self.__simv += 1
        return self.__song[self.__simv - 1]


class EnumSong:
    """"класс для итерации песен"""
    def __init__(self, song):
        self.__songs = song
        self.__limit = len(self.__songs)
        self.__simv = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__simv >= self.__limit:
            raise StopIteration
        self.__simv += 1
        return self.__songs[self.__simv - 1]

# демонстрация

note1 = Note('c', 'minor')
note2 = Note('d', 'minor')
note3 = Note('h', 'minor')
note4 = Note('g', 'minor')
note5 = Note('a', 'minor')
note6 = Note('e', 'minor')
note7 = Note('f', 'minor')
note8 = Note('c', 'major')
note9 = Note('d', 'major')
note10 = Note('h', 'major')
note11 = Note('g', 'major')
note12 = Note('a', 'major')
note13 = Note('e', 'major')
note14 = Note('f', 'major')

song1 = Song([note2, note4, note5, note6, note8, note11, note12, note14, note6, note3, note2, note1, note5, note8, note1, note9, note12, note13, note12, note13, note6, note10, note9, note6, note7, note3, note5, note3, note10, note11, note13, note14, note5, note3, note1, note6, note5])
song2 = Song([note12, note13, note6, note10, note9, note6, note7, note3, note5, note3, note10, note11, note13, note14, note5, note3, note1, note6, note5, note5, note1, note10, note4, note3, note4, note13, note11, note12, note4, note3, note2, note4, note6])
song3 = Song([note6, note5, note1, note10, note4, note3, note4, note13, note11, note12, note4, note3, note2, note4, note6, note13, note6, note10, note9, note6])

melodynote = MelodyNote([song1, song2, song3])

print(song1[1].sign)
print()
print("до изменений")
song2.play()
print("после изменений")
song2 << Note('e', 'major')
song2.play()
with melodynote as note:
    note[1].play()

song1 > song3
song2 < song3
song3 == song1
song2 >= song3
song1 <= song2

newsong = Song([note12, note13, note6, note10, note9, note6, note7, note3, note5, note3, note10, note11, note13, note14, note5, note3, note1, note6, note5, note7, note1, note6, note5, note4, note3, note1, note2, note7, note3, note1, note2, note7, note3, note4, note6, note3])
newsong.play()
melodynote << newsong
newsong.changemood('minor')
newsong.play()
