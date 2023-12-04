with open('7/data/output.txt', 'w', encoding='UTF-8') as out_file:
    with open('7/data/visitor_record.txt', 'r', encoding='UTF-8') as in_file:
        for line in in_file:
            if '東京都' in in_file:
                out_file.write(line)
