import csv


def ready_up():
    lines = []
    with open("esm_famil_data.csv", "r") as file:
        for i in range(6):
            line = file.readline().split(",")
            lines.append(line)
    return lines


def add_participant(participant, answers):
    mylist = list(answers)
    dict = {}
    for i in range(6):
        pass


def calculate_all():
    pass


ready_up()
add_participant(participant='salib',
                answers={'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب',
                         'ghaza': 'باقالیپلو'})
add_participant(participant='kianoush',
                answers={'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل',
                         'ghaza': 'به   پلو'})
add_participant(participant='sajjad',
                answers={'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ',
                         'ghaza': 'برنج خورشت'})
add_participant(participant='farhad',
                answers={'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل',
                         'ghaza': 'باقلوا'})
calculate_all()
