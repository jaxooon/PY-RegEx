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

    lines = [ re.sub(r"(<!\[CDATA\[)(XIC\(F_)([A-Z][1-9][A-Z]_|[A-Z][A-Z][1-9]_|[A-Z][A-Z][1-9][1-9][A-Z]_|[A-Z][A-Z][1-9][A-Z]_)([0-9][0-9]|[0-9])(_MSD_OFF\))(OTE\()([A-Z][1-9][A-Z]_|[A-Z][A-Z][1-9]_|[A-Z][A-Z][1-9][1-9][A-Z]_|[A-Z][A-Z][1-9][A-Z]_)([0-9][0-9]|[0-9])(_MTR.ANTI_CASC\);]]>)", 
            r"\1[\2\3\4\5, XIC(F_\3\4_OVRIDE)]\6\7\8\9", 
            line) for line in WordsWritten ]
    
    

    with open(name, 'w') as TextFile:
        TextFile.write('\n'.join(lines))

