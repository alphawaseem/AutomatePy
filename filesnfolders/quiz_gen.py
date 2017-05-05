import random

capitals = {'Alabama':	'Montgomery',	'Alaska':	'Juneau',	'Arizona':	'Phoenix',
            'Arkansas':	'Little	Rock',	'California':	'Sacramento',	'Colorado':	'Denver',
                        'Connecticut':	'Hartford',	'Delaware':	'Dover',	'Florida':	'Tallahassee',
                        'Georgia':	'Atlanta',	'Hawaii':	'Honolulu',	'Idaho':	'Boise',	'Illinois':
                        'Springfield',	'Indiana':	'Indianapolis',	'Iowa':	'Des	Moines',	'Kansas':
                        'Topeka',	'Kentucky':	'Frankfort',	'Louisiana':	'Baton	Rouge',	'Maine':
                        'Augusta',	'Maryland':	'Annapolis',	'Massachusetts':	'Boston',	'Michigan':
                        'Lansing',	'Minnesota':	'Saint	Paul',	'Mississippi':	'Jackson',	'Missouri':
                        'Jefferson	City',	'Montana':	'Helena',	'Nebraska':	'Lincoln',	'Nevada':
                        'Carson	City',	'New	Hampshire':	'Concord',	'New	Jersey':	'Trenton',	'New Mexico':	'Santa	Fe',	'New	York':	'Albany',	'North	Carolina':	'Raleigh',
                        'North	Dakota':	'Bismarck',	'Ohio':	'Columbus',	'Oklahoma':	'Oklahoma	City',
                        'Oregon':	'Salem',	'Pennsylvania':	'Harrisburg',	'Rhode	Island':	'Providence',
                        'South	Carolina':	'Columbia',	'South	Dakota':	'Pierre',	'Tennessee':
                        'Nashville',	'Texas':	'Austin',	'Utah':	'Salt	Lake	City',	'Vermont':
                        'Montpelier',	'Virginia':	'Richmond',	'Washington':	'Olympia',	'West Virginia':	'Charleston',	'Wisconsin':	'Madison',	'Wyoming':	'Cheyenne'}

NUM_OF_STUDENTS = 35


for quizNum in range(NUM_OF_STUDENTS):
    # : Create quiz and answer key files
    quizFile = open('quiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('answerkey%s.txt' % (quizNum + 1), 'w')

    # : Write out the header for the quiz
    quizFile.write('Name: \n\nDate: \n\nID: \n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz Form %s' % (quizNum + 1))
    quizFile.write('\n\n')

    # : Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # : Loop through all the 50 states, making a question for each
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctAnswer)]
        wronganswers = random.sample(wronganswers, 3)
        options = wronganswers + [correctAnswer]
        random.shuffle(options)

        quizFile.write('%s. What is the capital of %s\n' %
                       ((questionNum + 1), states[questionNum]))
        for i in range(4):
            quizFile.write('    %s . %s\n' % ('ABCD'[i], options[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s . %s\n' % (
            (questionNum + 1), 'ABCD'[options.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
