with open("./input/names/invited_names") as names:
    for name in names:
        with open("./input/letters/started_letter") as letter:
            updated_letter = letter.read().replace("[NAME]", name)
            with open(f"./output/ready_to_send/letter_for_{name}", mode="w") as final_letter:
                final_letter.write(updated_letter)
