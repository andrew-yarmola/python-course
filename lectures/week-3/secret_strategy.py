def good(boxes, person) :
    count = 0
    idx = person
    while count < 5 :
        curr = boxes[idx]
        if curr == person :
            return True
        idx = curr
        count += 1
    return False
