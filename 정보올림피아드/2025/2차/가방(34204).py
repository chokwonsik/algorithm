"""
https://www.acmicpc.net/problem/34204
문제: 가방 (KOI 2025 중등부 2번)
분류: 그리디, 정렬, 누적합, 두 포인터

[문제 한 줄 요약]
- 우리가 무게 합이 x 이하가 되게 일부 물건을 미리 챙김.
- 그 다음 도둑은 남은 물건 중 "제일 가벼운 K개"를 가져감.
- 목표: x=1..C 각각에 대해, 도둑이 가져가는 K개 무게 합을 최대화.

[아이디어(쉽게)]
1) 물건을 가벼운 순으로 정렬.
2) 누적합 P[i] 준비 (P[i] = 가장 가벼운 i개 합, P[0]=0 포함).
3) x가 주어지면, 앞에서 t개(=가벼운 t개)를 빼는 게 항상 최선.
   - 이렇게 해야 같은 t를 빼는 데 드는 무게가 최소 → 더 큰 t까지 가능 → 도둑이 집는 K개가 더 무거워짐.
4) 단, 너무 많이 빼면 K개가 안 남음 → t ≤ N-K.
5) 정답 = P[t+K] - P[t]  (t 다음의 K개 구간 합)

[알고리즘 흐름]
- A 정렬 → P 만들기 → x=1..C 순회하면서
  P[t+1] ≤ x일 때만 t를 1씩 올림 → 매번 P[t+K]-P[t] 출력.

[복잡도]
- 정렬 O(N log N) + 순회 O(C) → 전체 O(N log N + C), 메모리 O(N)
"""

from itertools import accumulate
import sys

def solve1():
    input = sys.stdin.readline

    # N: 물건 개수, K: 도둑이 가져갈 개수, C: x의 최대값
    N, K, C = map(int, input().split())

    # 가벼운 순 정렬 (앞에서 t개 = 가장 가벼운 t개가 되게)
    A = sorted(map(int, input().split()))

    # 누적합 P: P[i] = 가장 가벼운 i개 합. P[0]=0을 넣어서 t=0 처리 깔끔하게.
    # 예) A=[1,2,3] → accumulate=[1,3,6], P=[0,1,3,6]
    P = [0] + list(accumulate(A))

    # t: 우리가 빼는 개수(최대 N-K). 도둑이 K개는 꼭 가져가야 해서 이 제한 필요.
    max_t = max(0, N - K)

    t = 0        # 처음엔 아무것도 안 뺌
    out = []     # 출력 모아서 한 번에 찍자 (빠름)

    # x를 1부터 C까지 키우면서, 가능할 때만 t를 한 칸씩 밀어줌
    for x in range(1, C + 1):
        while t < max_t and P[t + 1] <= x:  # 다음 것까지 빼도 x 이하면 t 증가
            t += 1
        # 도둑이 가져갈 K개 합 = (t 다음 K개) 합 = P[t+K] - P[t]
        out.append(str(P[t + K] - P[t]))

    print("\n".join(out))

if __name__ == "__main__":
    solve1()