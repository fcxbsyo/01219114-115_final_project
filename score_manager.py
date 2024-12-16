import csv


def load_high_score():
    try:
        with open("scoreboard.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            try:
                next(reader)
            except StopIteration:
                return 0
            high_score = 0
            for row in reader:
                score = int(row[1])
                if score > high_score:
                    high_score = score
            return high_score
    except FileNotFoundError:
        return 0
