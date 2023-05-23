# given a order list, trim it so that each individual element does not repeat more than max_e times

def delete_nth(order, max_e):
    result = []
    
    for i in order:
        count = 0
        for j in result:
            if j == i:
                count += 1
        if count < max_e:
            result.append(i)
    return result
        