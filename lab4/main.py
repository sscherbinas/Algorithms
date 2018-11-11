def friends_biggest_number(friends):
    graph = {}

    for i, person_friends in enumerate(friends):
        graph[i] = []
        for j, friend in enumerate(person_friends):
            if friend == 'Y':
                graph[i].append(j)
    print(graph)
    cnt = 0
    for person, friends in graph.items():
        friends_cnt = len(graph[person])
        for friend in friends:
            for friend_of_friend in graph[friend]:
                if friend_of_friend != person and friend_of_friend not in graph[person]:
                    friends_cnt += 1
        if friends_cnt > cnt:
            cnt = friends_cnt

    return cnt


print(friends_biggest_number(["NYY", "YNY", "YYN"]))
