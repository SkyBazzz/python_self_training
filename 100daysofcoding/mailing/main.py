PLACEHOLDER = "[NAME]"
with open("./input/names/invited_names") as names:
    all_names = names.readlines()
for name in all_names:
    with open("./input/letters/started_letter") as letter:
        stripped_name = name.strip()
        updated_letter = letter.read().replace(PLACEHOLDER, stripped_name)
        with open(
            f"./output/ready_to_send/letter_for_{stripped_name}", mode="w"
        ) as final_letter:
            final_letter.write(updated_letter)
