import re
phoneRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
result=phoneRegex.findall('415-555-6589  265-569-2569')
for i in range(2):
    for j in range(3):
        print(result[i][j])
