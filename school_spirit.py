def get_scores(iterations):
    scores = []
    for i in range(iterations):
        scores.append(int(input()))
    return scores

def get_group_score(scores):
    coef = .2
    inner = 0
    for index, score in enumerate(scores):
        inner += score * (.8**index)
    return coef * inner

def get_average(scores):
    start = 0
    end = len(scores)
    subscores = []
    for i in range(end):
        subscores.append(get_group_score(scores[0:i]+scores[i+1:end]))
    return subscores

def main():
    iterations = int(input())
    scores = get_scores(iterations)
    print(get_group_score(scores))
    print(sum(get_average(scores))/len(get_average(scores)))



if __name__ == "__main__":
    main()