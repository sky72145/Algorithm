# n개의 정수가 순서대로 입력된다.
# -2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.
#
# n개의 입력된 정수를 순서대로 출력해보자.
n = int(input())
list = list(map(int,input().split()))
for i in range(n):
    print(list[i],sep='\n')