








def javanais(text):
    answer = ''
    counter = 0
    vowels = 'aeiouAEIOU'
    for letter in text:
        counter += 1
        if letter not in vowels:
            if letter[counter] in vowels:
                answer += letter + 'av'
            else:
                answer += letter
    return answer

def minimalGraph(graph):
    return 1