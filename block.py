import json


# Block creating
def write_block():
    data = {'name': 'ivan',
            'amount': 5,
            'to_whom': 'Vasya',
            'hash': '123'}

# Open or create new file and write into info
    with open('test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block()


if __name__ == '__main__':
    main()
