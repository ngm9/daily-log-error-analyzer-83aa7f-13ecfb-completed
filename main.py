from additional_module import count_error_lines


def main() -> None:
    log_path = "logs.txt"
    total_errors = count_error_lines(log_path)
    print("Total ERROR lines:", total_errors)


if __name__ == "__main__":
    main()
