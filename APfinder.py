table = 'jsdladjfkdshfkdsfhkdsfk\n'
table = 'kghskd\n' + table
table = table +'^[[oJ'
print(table)
f = open('ap.txt','w')
f.truncate(0)
f.write(table)
f.close()

f = open('ap.txt', 'r')
lines = f.read().splitlines()

for line in lines:
    if line.find('^[[') == -1:
        print(line)
user_input = input()
if user_input == 'Y' or user_input == 'y' or user_input == 'yes' or user_input == 'YES':
    print('y')
else:
    print('n')



