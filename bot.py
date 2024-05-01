import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["흥미로운데요. 더 알려주세요!",
                    "좋은데요? 더 얘기해 주세요.",
                    "왜 그렇게 생각하시나요?",
                    "오늘 날씨가 재밌네요. 그렇지 않나요??",
                    "그렇군요. 다른 얘기를 해볼까요?",
                    "어제 경기 보셨나요?"]

print("안녕하세요, 마빈입니다, 간단한 로봇이에요.")
print("대화를 그만하고 싶으면 '그만'이라고 적어주세요")
print("답변을 하신 후에는 'enter'키를 눌러주세요.")
print("오늘 어떠셨나요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input == "그만":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어요, 안녕히가세요!")
