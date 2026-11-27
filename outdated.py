months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            m, d, y = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            m, d, y = date.split(" ")
            if m.title() in months:
                m = months.index(m.title()) + 1
        else:
            continue

        if int(m) <= 12 and int(d) <= 31:
            print(f"{int(y):04}-{int(m):02}-{int(d):02}")
            break
    except (ValueError, NameError):
        pass
