import numpy as np
input()
answers = [
    'The future is unclear',
    'No',
    'Yes',
    'Only if you really want it',
    'If they say it be like it is, it do',
    'Eh, worry about that later',
    'This feels targeted at me',
    'Sure?',
    'Do you really want to know?',
    "No, and don't you dare ask again",
    "Ya, sure, you betcha!"    
]

range = len(answers)
result = np.random.randint(0,range)

print(answers[result])