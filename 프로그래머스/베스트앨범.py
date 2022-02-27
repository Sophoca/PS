def solution(genres, plays):
    answer = []

    total = dict()
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in total:
            total[genre] = {}
            total[genre]["data"] = []
            total[genre]["sum"] = 0
        total[genre]["data"].append({"idx": idx, "play": play})
        total[genre]["sum"] += play
    for value in total.values():
        value["data"] = sorted(value["data"], key=lambda x: x["play"], reverse=True)
    sorted_total = sorted(total.keys(), key=lambda x: total[x]["sum"], reverse=True)
    for obj in sorted_total:
        answer.extend(map(lambda x: x["idx"], total[obj]["data"][:2]))

    return answer


solution(["classic", "pop", "classic", "classic", "pop", "rock"], [500, 600, 500, 800, 2500, 700])
