import re
import sys

def parse_log_line(line: str) -> dict:
    log_list = line.strip().split()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s[A-Z]*(\s.*)*", line):
        raise Exception("Invalid formar")
    log_dict = {}
    for indx, el in enumerate(log_list):
        if indx == 0:
            log_dict["date"] = el
        elif indx == 1:
            log_dict["time"] = el
        elif indx == 2:
            log_dict["level"] = el
        elif indx == 3:
            log_dict["message"] = el
        elif indx > 3:
            log_dict["message"] = f"{log_dict["message"]} {el}"
    return log_dict

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding = 'utf8') as file:
            logs = []
            for line in file:
                logs.append(parse_log_line(line))
            return logs

    except FileNotFoundError:
        return "File not found"
    except:
        return "Invalid format file."

def filter_logs_by_level(logs: list, level: str) -> list:
    return [el for el in logs if el["level"] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    logs_dict = {}
    for el in logs:
        if el["level"] in logs_dict:
            logs_dict[el["level"]] += 1
        else:
            logs_dict[el["level"]] = 1
    return logs_dict

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for el in counts:
        print(f"{el:<17}| {counts[el]:<9}")
    print("\n")

def display_log_details(logs: list, level: str):
    print(f"Деталі логів для рівня '{level.upper()}':")
    new_list = filter_logs_by_level(logs, level)
    for el in new_list:
        print(f"{el["date"]} {el["time"]} {el["level"]} - {el["message"]}")

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("You input invalid arguments. "\
            "Must be 2 or 1 arguments, 'path' and 'level'")
        return 0

    path = sys.argv[1]
    log_list = load_logs(path)
    if type(log_list) != list:
        print(log_list)
        return 0

    logs_dict = count_logs_by_level(log_list)
    display_log_counts(logs_dict)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        if not level.upper() in logs_dict:
            print("Invalid arguments: level")
            return 0

        sorted_logs = filter_logs_by_level(log_list, level)
        display_log_details(sorted_logs, level)
   
if __name__ == "__main__":
    main()