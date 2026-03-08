love_book = []

while True:
    line = input().strip('\n')
    if line.strip() == '0':
        break
    res = [] 
    current_word = '' 
    for c in line:
        if c.isalpha():
            current_word += c
        else:
            if current_word:
                if current_word in love_book:
                    idx = love_book.index(current_word) + 1
                    res.append(str(idx))
                    love_book.pop(idx-1)
                    love_book.insert(0, current_word)
                else:
                    res.append(current_word)
                    love_book.insert(0, current_word)
                current_word = ''
            res.append(c)
    if current_word:
        if current_word in love_book:
            idx = love_book.index(current_word) + 1
            res.append(str(idx))
            love_book.pop(idx-1)
            love_book.insert(0, current_word)
        else:
            res.append(current_word)
            love_book.insert(0, current_word)
    print(''.join(res))