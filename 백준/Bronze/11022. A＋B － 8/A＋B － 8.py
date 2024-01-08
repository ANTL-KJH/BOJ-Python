"""
* Project Name : Baekjoon Online Judge #11022(A+B - 8)
* Program Purpose and Basic Features :
* - 두 정수를 입력받고 합을 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N = int(input())
    for i in range(1, N + 1, 1):
        A, B = map(int, input().split())
        print("Case #{}: {} + {} = {}".format(i, A, B, A + B))


if __name__ == "__main__":
    main()
