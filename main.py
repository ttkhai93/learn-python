from collections import Counter, defaultdict, deque

if __name__ == '__main__':
    test = "aabbbcc"
    # test = ["a", "a", "b", "b", "b", "c"]
    # test = {"a", "a", "b", "b", "b", "c"}
    # test = ("a", "a", "b", "b", "b", "c")
    counter = Counter(test)

    print(counter.items())
    print(counter.total())
    print(counter.most_common(2))
    print(list(counter.elements()))

    counter.subtract("abb")
    print(counter.items())


    # Use default dict when expecting a key doesn't exist has a default value
    d = defaultdict(int)
    d["a"] = 1
    print(d)
    print(d["a"])
    print(d["b"])

    # Allow add and remove element in both end
    q = deque()
    q.append(1)
    q.append(2)
    q.appendleft(0)
    q.insert(1, 3)
    q.pop()
    print(q)
    q.popleft()
    print(q)
    print(q.count(3))
    print(q)
    q.extendleft([1, 2])
    print(q)
    q.rotate(-1)
    print(q)