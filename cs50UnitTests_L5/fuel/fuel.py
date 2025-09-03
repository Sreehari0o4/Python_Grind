def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percent = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        print(gauge(percent))
        break


def convert(fraction):
    try:
        num_str, den_str = fraction.strip().split("/")
    except ValueError:
        raise ValueError
    if not (num_str.isdigit() and den_str.isdigit()):
        raise ValueError
    num = int(num_str)
    den = int(den_str)
    if den == 0:
        raise ZeroDivisionError
    if num > den:
        raise ValueError
    return round(num / den * 100)


def gauge(percentage):
    # Return fuel gauge string
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    return f"{percentage}%"


if __name__ == "__main__":
    main()