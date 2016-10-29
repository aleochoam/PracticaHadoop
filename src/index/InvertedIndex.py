import os
import re
import unicodedata

from mrjob.job import MRJob

timesMap = {}

def limpiar(line):
    line = line.lower()
    line = elimina_tildes(line)
    line = re.findall(r"[\w']+", line)
    return line

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

class InvertedIndex(MRJob):

    def mapper(self, _, line):
        fileName = os.environ['map_input_file']
        line = limpiar(line)

        for word in line:
            if (fileName, word) not in timesMap:
                timesMap[(fileName, word)] = 1
            else:
                timesMap[(fileName, word)] +=1

            yield (word, fileName)

    def reducer(self, word, files):
        lFiles = list(files)
        fileTimes = [(x, timesMap[(x, word)]) for x in lFiles]
        # yield (word, len(lFiles)), list(set((fileTimes)))
        yield word, list(set(fileTimes))

if __name__ == '__main__':
    InvertedIndex.run()
