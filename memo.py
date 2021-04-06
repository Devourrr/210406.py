import sys

print(sys.argv) # 리스트 변수

option = sys.argv[1] # 인덱싱 값 저장

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()