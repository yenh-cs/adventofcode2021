import collections

def read_data(file_name):
    with open(file_name) as file:
       data = file.readlines() 
       data = [line.rstrip('\n') for line in data if line != '\n']
       polymer_template, rules = data[0], data[1:]
       rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules}
       return polymer_template, rules


def count_occurrences(polymer_template):
    pair_occurrences = {}
    single_occurrences = {}

    for i in range(len(polymer_template) - 1):
        key = polymer_template[i] + polymer_template[i+1]
        if key in pair_occurrences:
            pair_occurrences[key] += 1
        else:
            pair_occurrences[key] = 1

    for j in polymer_template:
        if j in single_occurrences:
            single_occurrences[j] += 1
        else:
            single_occurrences[j] = 1

    return pair_occurrences, single_occurrences


def insert_and_count(polymer_template, rules, steps=1):
    count = 1
    pair_occurrences, single_occurrences = count_occurrences(polymer_template)

    while count <= steps:
        pair_occurrences_copy = pair_occurrences.copy()
        for pair in pair_occurrences_copy:
            inserted = rules[pair]
            left = pair[0:1] + inserted 
            right = inserted + pair[1:]

            occurrence = pair_occurrences_copy[pair] 
            pair_occurrences[pair] += (-1 * occurrence)
            
            if inserted in single_occurrences:
                single_occurrences[inserted] += occurrence
            else:
                single_occurrences[inserted] = occurrence

            if left not in pair_occurrences or pair_occurrences[left] == 0:
                pair_occurrences[left] = occurrence
            else:
                pair_occurrences[left] += occurrence

            if right not in pair_occurrences or pair_occurrences[right] == 0:
                pair_occurrences[right] = occurrence
            else:
                pair_occurrences[right] += occurrence
            
        count += 1

    return single_occurrences    




def main():
    polymer_template, rules = read_data('input.txt')
    single_occurrences = insert_and_count(polymer_template, rules, 40)
    diff = max(single_occurrences.values()) - min(single_occurrences.values())
    print(diff)

if __name__ == '__main__':
    main()
