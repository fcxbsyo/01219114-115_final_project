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


def save_score(player_name, score):
    try:
        with open("scoreboard.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            data = list(reader)

        updated = False
        for row in data:
            if row[0] == player_name:
                if int(row[1]) < score:
                    row[1] = str(score)
                updated = True
                break

        if not updated:
            data.append([player_name, str(score)])

        with open("scoreboard.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Player", "Score"])
            writer.writerows(data)

    except FileNotFoundError:
        with open("scoreboard.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Player", "Score"])
            writer.writerow([player_name, str(score)])

