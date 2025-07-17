import json
import random  # 예시로 랜덤 데이터 사용

# 예시 데이터: 중대원 수와 출타율
data = {
    "total_members": 50,
    "absent_members": random.randint(0, 50),  # 출타 인원 랜덤 생성
    "absence_rate": 0  # 나중에 계산
}

# 출타율 계산
data["absence_rate"] = (data["absent_members"] / data["total_members"]) * 100

# JSON 파일로 저장
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
