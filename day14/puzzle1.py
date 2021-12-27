import collections

def read_data(file_name):
    with open(file_name) as file:
       data = file.readlines() 
       data = [line.rstrip('\n') for line in data if line != '\n']
       polymer_template, rules = data[0], data[1:]
       rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules}
       return polymer_template, rules


def insert_rules(polymer_template, rules, steps=1):
    count = 1
    while count <= steps:
        inserteds = []
        for i in range(len(polymer_template) - 1):
            key = polymer_template[i] + polymer_template[i+1]
            if key in rules:
                inserted = rules[key]
                inserteds.append((inserted, i + 1 + len(inserteds)))

        for key, index in inserteds:
            polymer_template = polymer_template[:index] + key + polymer_template[index:]
        
        count += 1
    
    most_common_element = collections.Counter(polymer_template).most_common(1)[0]
    least_common_element = collections.Counter(polymer_template).most_common()[::-1][0]
    diff = most_common_element[1] - least_common_element[1] 

    print(most_common_element)
    print(least_common_element)
    print(diff)




def main():
    polymer_template, rules = read_data('input.txt')
    insert_rules(polymer_template, rules, 4)

if __name__ == '__main__':
    main()
