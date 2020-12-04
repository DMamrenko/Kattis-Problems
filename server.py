#Server
tasks_time = [int(s) for s in input().split()]
tasks = [int(s) for s in input().split()]
total = 0
count = 0
while total < tasks_time[1]:
    if count == len(tasks):
        count = len(tasks)
        break
    else:
        total += tasks[count]
        count += 1
        if total > tasks_time[1]:
            count -= 1
print(count)
