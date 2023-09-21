import csv

f = open('student.csv', 'r') 
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].replace(',', ' ').replace('\n','').split(' ')

subject = ['국어', '영어', '수학', '사회']

lines[0].append('평균')
subject_index = []
for i in range(len(lines[0])):
        if lines[0][i] in subject:
            subject_index.append(i)
s = ','.join(lines[0]) + '\n'
for lines_index in range(1, len(lines)):
    avg = 0
    for i in subject_index:
        avg += int(lines[lines_index][i])
    lines[lines_index].append(str(avg/len(subject_index)))
    s = s+','.join(lines[lines_index]) + '\n'

print(s)
wf = open('student.csv', 'w')
wf.write(s)
wf.close()