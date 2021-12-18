from generator import join

with open('./data/f1.txt', 'r', encoding='utf-8') as string_file:
    with open('./data/f2.txt', 'r', encoding='utf-8') as number_file:
        for line in join(string_file, number_file):
            print(line)
