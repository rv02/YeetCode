from typing import List

if __name__ == '__main__':
    records: List[List] = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    runner_up_score = sorted(list(set(record[1] for record in records)))[1]
    runner_ups = [record[0] for record in records if record[1] == runner_up_score]
    for runner_up in sorted(runner_ups):
        print(runner_up)

