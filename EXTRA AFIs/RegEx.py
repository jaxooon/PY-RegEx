import glob
import re

FileNameList = []
FileNameListLength = 0

for filename in glob.glob('*.L5*'):
    FileNameList.append(filename)

print(FileNameList)

FileNameListLength = len(FileNameList)

print(FileNameListLength)


for name in FileNameList:
    with open(name, 'r') as TextFile:
        WordsWritten = [line.strip() for line in TextFile]

    lines = [re.sub(r"\,AFI\(\) \]", r"]", line) for line in WordsWritten]
    

    with open(name, 'w') as TextFile:
        TextFile.write('\n'.join(lines))


    with open(name, 'r') as TextFile:
        WordsWritten = [line.strip() for line in TextFile]

    lines = [re.sub(r"\[ AFI\(\) \,AFI\(\) \]", r"[ AFI() ]", line) for line in WordsWritten]
    

    with open(name, 'w') as TextFile:
        TextFile.write('\n'.join(lines))



    
    

    