import json
import random
import sys

if len(sys.argv) != 4:
    print('Usage: python quiz2.py %filename% %num_of_students% %quiz_title%')
    exit()

FILE_NAME = sys.argv[1]
NUM_STUDENTS = int(sys.argv[2])
QUIZ_TITLE = sys.argv[3]

qaDict = {}

with open(FILE_NAME) as qa:
    qaDict = json.load(qa)

questionsList = list(qaDict.keys())
num_of_que = len(questionsList)

for i in range(NUM_STUDENTS):
    random.shuffle(questionsList)
    quizFileName = 'quiz%s.txt' % (i + 1)
    ansFileName = 'ansKey%s.txt' % (i + 1)

    quizFile = open(quizFileName, 'w')
    ansFile = open(ansFileName, 'w')

    quizFile.write('\n\nName: \nDate: \nStudent_ID: \n\n')
    quizFile.write((' ' * 20) + QUIZ_TITLE + ' SERIES %s\n\n' % (i + 1))

    for queNum in range(num_of_que):
        correctAns = qaDict[questionsList[queNum]]
        wrongAns = list(qaDict.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        options = wrongAns + [correctAns]
        random.shuffle(options)

        quizFile.write('%s. %s\n' %
                       ((queNum + 1), questionsList[queNum]))
        for i in range(4):
            quizFile.write('    %s . %s\n' % ('ABCD'[i], options[i]))
        quizFile.write('\n')

        ansFile.write('%s . %s\n' % (
            (queNum + 1), 'ABCD'[options.index(correctAns)]))
    quizFile.close()
    ansFile.close()
