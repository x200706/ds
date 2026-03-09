book = []

while True:
    line = input().strip('\n')
    if line.strip() == 0:
        break
    response = []
    curr_word = ''
    for c in line:
        if c.isalpha(): # 若c是一種字母
            curr_word += c
        else:
            if curr_word:
                # 如果單字已經在書裡又被用到，把它放到第一個
                if curr_word in book:
                    index = book(curr_word)+1
                    res.append(str(index)) # 代替為原始的序號
                    book.pop(index-1)
                    book.insert(0, curr_word)
                else:
                    book.pop(index-1)
                    book.insert(0, curr_word)
                curr_word = '' # 重置
            response.append(c)

    if curr_word:
        # 如果單字已經在書裡又被用到，把它放到第一個
        if curr_word in book:
            index = book(curr_word)+1
            res.append(str(index)) # 代替為原始的序號
            book.pop(index-1)
            book.insert(0, curr_word)
        else:
            book.pop(index-1)
            book.insert(0, curr_word)
    print(''.join(res))
# 此題詳解：https://www.doubao.com/thread/wf23bb4282a95d1e3