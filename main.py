print ('Hello Mars')

try:
    f = open( 'mission_computer_main.log', 'r', encoding='utf-8')
    lines = f.read()
    print(lines)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except PermissionError:
    print("파일에 대한 권한이 없습니다.")
except:
    print("예상치 못한 예외가 발생했습니다.")
    f.close()

#역순
a = open('mission_computer_main.log', 'r')
r = a.readlines()
r.sort(reverse=True)
for line in r:
    print(line,end='')
f.close()

#문제가 발생되는 구간의 로그 따로저장
d = open('mission_computer_main.log', 'r')
w = d.readlines()
e = open('Error.txt', 'w+',)
for l in range(33,36):
    e.write(w[l])
d.close()
e.close()

