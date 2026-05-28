# grades.py

#gradebook v1.0 - 1주차 실습 완료
SUBJECTS = ["국어", "영어", "수학", "과탐"]

def get_scores():
    scores = {}
    print("과목별 점수를 입력하세요 (0~100).\n")
    
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject} 점수: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print(" -> 0에서 100 사이의 점수를 입력하세요.")
            except ValueError:
                print(" -> 숫자를 입력하세요.")
                
    return scores

def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)

def print_result(scores, average):
    print("\n" + "=" * 30)
    print("      성적 결과")
    print("=" * 30)
    for subject in SUBJECTS:
        print(f"{subject:<10} {scores[subject]:>6.1f}점")
    print("-" * 30)
    print(f"{'평균':<10} {average:>6.1f}점")
    print("=" * 30)

def find_highest_lowest(scores):
    highest = max(SUBJECTS, key=lambda s: scores[s])
    lowest = min(SUBJECTS, key=lambda s: scores[s])
    return highest, lowest

if __name__ == "__main__":
    scores = get_scores()
    average = calculate_average(scores)
    print_result(scores, average)
    
    highest, lowest = find_highest_lowest(scores)
    print(f"\n최고점: {highest} ({scores[highest]:.1f}점)")
    print(f"최저점: {lowest} ({scores[lowest]:.1f}점)")