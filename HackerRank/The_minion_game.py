def minion_game(string):
    # your code goes here
    vowels = ['A','E','I','O','U']
    stuart = []
    kevin = []
    stuart_score = 0
    kevin_score = 0
    uni_list = []
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            subs = string[i:j]
            if string[i] not in vowels:
                stuart.append(subs)
                stuart_score += 1
            else:
                kevin.append(subs)
                kevin_score +=1
            if subs not in uni_list:
                uni_list.append(subs)
            print(subs)
    if stuart_score == kevin_score:
        print('Draw')
    elif stuart_score > kevin_score:
        print('Stuart',stuart_score)
    else:
        print('Kevin',kevin_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
