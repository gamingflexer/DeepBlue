"""elements = ['About', 'Activity', 'Education', 'Highlights', 'Experience', 'Licenses & certifications', 'Skills',
            'Projects', 'Honors & awards', 'Languages', 'Interests', 'Causes']

my_dict = {}
for i in range(12):
    with open(f"blocks/{i + 1}b.txt", "r") as file:
        first_line = file.readline()
        for j in range(12):
            if elements[j] in first_line:
                remaining_lines = file.readlines()
                my_dict[elements[i]] = remaining_lines

print(my_dict)"""
