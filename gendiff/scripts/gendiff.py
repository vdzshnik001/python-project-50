import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish', type=str,
    )
    return parser.parse_args()


def main():
    args = parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file

    # пока generate_diff может просто вернуть заглушку или разницу для json;
    # позже сюда «подключишь» полноценную логику
    result = generate_diff(file_path1, file_path2, formatter=args.format)
    print(result)


if __name__ == '__main__':
    main()