def spam(number):
    return 'bulochka'*number
    

def my_sum(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result +=i
    return result

    pass



def shortener(string):
    list_of_words = string.split()

    result = []
    for word in list_of_words:
        if len(word) > 6:
            result.append(word[0:6] + "*")
        else: result.append(word)
    return " ".join(result)


    
    pass
   


def compare_ends(words):
    result = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            result += 1
    return result

    
    pass
    

