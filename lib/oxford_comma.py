def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    elif len(items) == 3:
        return f"{items[0]}, {items[1]}, and {items[2]}"
    else:
        comma_separated = ", ".join(items[:-1])
        return f"{comma_separated}, and {items[-1]}"
    