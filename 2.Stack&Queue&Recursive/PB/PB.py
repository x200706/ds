import sys

def calculate_cycle(num, people):
    while num > people:
        num -= people
    while num < 1:
        num += people
    return num

lines = [line.strip() for line in sys.stdin if line.strip()]
idx = 0
while idx < len(lines):
    line1 = lines[idx]
    idx += 1
    date_part, people_part = line1.split()
    people = int(people_part)
    D = int(date_part.split('/')[0])
    
    line2 = lines[idx]
    idx += 1
    absent_set = set()
    if line2:
        absent_nums = line2.split()
        absent_set = set(map(int, absent_nums))
    
    result = []          
    called_set = set()   
    angry = 0            
    curr = D             
    
    for i in range(8):
        if i == 0:
            new = curr
        else:
            temp1 = curr + 10
            temp1 = calculate_cycle(temp1, people)
            if temp1 not in absent_set and temp1 not in called_set:
                new = temp1
            else:
                angry += 1
                new = calculate_cycle(temp1 + 1, people)
    
        result.append(new)
        called_set.add(new)
        curr = new
    
    print(' '.join(map(str, result)))
    print(f"Jimmy's angry number is {angry}")