dictionary = {}

while True:
    word = input("\n영어 단어 등록 (종료는 quit) : ")
    if word == "quit":
        print("영어 단어 등록 종료\n")
        break
    elif word in dictionary.keys():
        print(f"{word}는 이미 등록된 단어입니다.")
    else:
        meaning = input(f"{word}의 뜻 입력 (종료는 quit): ")
        if meaning == "quit":
            break
        else: 
            dictionary[word] = meaning

while True:
    search_word = input("검색할 단어 입력 (종료는 quit): ")
    if search_word == "quit":
         print("\n종료합니다.")
         break
    elif search_word in dictionary:
        print(f"{search_word}의 뜻은 {dictionary[search_word]}입니다.\n")
    else:
        print(f"{search_word}는 사전에 없는 단어입니다.\n")