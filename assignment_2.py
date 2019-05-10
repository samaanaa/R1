data = [50.3, 338.4, 626.5, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]

duration = []
i = 0

duration = [y - x for x, y in zip(data[:-1], data[1:])]

print(duration)

