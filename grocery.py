grocery = {}

while True:
    try:
        item = input().strip().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        for key in sorted(grocery):
            print(f"{grocery[key]} {key}")
        break
