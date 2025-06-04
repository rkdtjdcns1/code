# zodiac.py

def get_zodiac(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리 (Aries)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리 (Taurus)"
    # (나머지 별자리들도 같은 방식으로 추가)
    else:
        return "알 수 없는 별자리"

if __name__ == "__main__":
    date_str = input("생년월일을 YYYY-MM-DD 형식으로 입력하세요: ")
    year, month, day = map(int, date_str.split("-"))
    print(f"당신의 별자리는 {get_zodiac(month, day)}입니다.")
