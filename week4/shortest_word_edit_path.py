from string import ascii_letters


def shortestWordEditPath(source, target, words):
    if not len(words): return -1
  
    # This is to recored the depth of each word and visited nodes
    visited = dict()
    visited[source] = 0

    queue = []
    queue.insert(0, source)

    while len(queue) != 0 :
        # if the word is in the queue than, it's index in the queue is difference
        # print(queue)
        depth = visited.get(queue[len(queue)-1])
        word = queue.pop()

        if word == target: return depth

        # if current word is not equal to target then look for negihboring words of that word
        # negihboring words are words that have one char difference
        for idx in range(len(word)):
            # iterate over the current word and try different changes 
            # if one of the changes is in the word list and haven't yet been added to the queue
            # then add it and mark it as visited
            for char in ascii_letters:
                tmp = list(word)
                tmp[idx] = char
                tmp = "".join(tmp)

                
                if tmp in words and not visited.get(tmp):
                    # print("fund: %s" %tmp)
                    queue.insert(0, tmp)
                    visited[tmp] = depth + 1

    return -1
            


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
# output: 5
#words = ["to"]
# output: -1

print(shortestWordEditPath(source, target, words))

Time : O(N*K^2), where N is the length of words and K is the maximum length of any given word. For each word in words,
in order to find neighbors we may construct O(K) new words, each in O(K) time.
Space: O(NK)


