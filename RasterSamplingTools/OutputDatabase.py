"""\
Output database

Created on July 22, 2021

@author Eric Mader
"""

import json

class OutputDatabase(object):
    def __init__(self, file):
        self._file = file
        try:
            inFile = open(file)
        except FileNotFoundError:
            self._db = []
        else:
            # We could check for errors in the input file
            # but it's probably better to just err out...
            self._db = json.load(inFile)
            inFile.close()

    def close(self):
        outFile = open(self._file, "w")
        json.dump(self._db, outFile, indent=4)
        outFile.close()

    def getEntry(self, font):
        psName = font.postscriptName

        for entry in self._db:
            if entry["ps_name"] == psName:
                break
        else:
            entry = {"ps_name": psName, "full_name": font.fullName, "test_results": {}}
            self._db.append(entry)

        if "full_name" not in entry:
            entry["full_name"] = font.fullName

        return entry

    def getTestResults(self, entry):
        return entry["test_results"]