def count_substring(string, sub_string):
    count = 0
    sub_l = len(sub_string)
    for i in range(0,len(string)):
        k = 0
        if i == 0:
            k = i+sub_l-1
        else:
            i+sub_l
        if k >= len(string)-1:
            break
        else:
            if string[i:i+sub_l] == sub_string:
                count += 1
        
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
