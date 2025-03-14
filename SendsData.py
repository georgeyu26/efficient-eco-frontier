# Define the sends with their first and last rounds
sends = [
    ("Grouped Reds", 1, 11),
    ("Spaced Blues", 1, 2),
    ("Spaced Greens", 2, 4),
    ("Grouped Blues", 3, 12),
    ("Spaced Yellows", 3, 6),
    ("Spaced Pinks", 4, 8),
    ("Grouped Greens", 5, 16),
    ("Spaced Whites", 5, 9),
    ("Spaced Blacks", 6, 9),
    ("Grouped Yellows", 7, 19),
    ("Spaced Purples", 8, 10),
    ("Grouped Pinks", 9, 100),
    ("Spaced Zebras", 9, 10),
    ("Grouped Blacks", 10, 25),
    ("Grouped Whites", 10, 21),
    ("Spaced Leads", 10, 11),
    ("Grouped Purples", 11, 100),
    ("Grouped Zebras", 11, 29),
    ("Grouped Leads", 12, 22),
    ("Spaced Rainbows", 12, 12),
    ("Grouped Rainbows", 13, 100),
    ("Spaced Ceramics", 13, 15),
    ("Grouped Ceramics", 16, 23),
    ("Tight Leads", 23, 100)
]

# Assign numbers to each send
send_numbers = {
    "Zero Send": 0,
    "Grouped Reds": 1,
    "Spaced Blues": 2,
    "Grouped Blues": 3,
    "Spaced Greens": 4,
    "Grouped Greens": 5,
    "Spaced Yellows": 6,
    "Grouped Yellows": 7,
    "Spaced Pinks": 8,
    "Grouped Pinks": 9,
    "Spaced Whites": 10,
    "Grouped Whites": 11,
    "Spaced Blacks": 12,
    "Grouped Blacks": 13,
    "Spaced Purples": 14,
    "Grouped Purples": 15,
    "Spaced Zebras": 16,
    "Grouped Zebras": 17,
    "Spaced Leads": 18,
    "Grouped Leads": 19,
    "Tight Leads": 20,
    "Spaced Rainbows": 21,
    "Grouped Rainbows": 22,
    "Spaced Ceramics": 23,
    "Grouped Ceramics": 24
}

# Determine available sends for each round
round_sends = {round_num: [0] for round_num in range(1, 31)}

for send, first_round, last_round in sends:
    for round_num in range(first_round, min(last_round + 1, 31)):
        round_sends[round_num].append(send_numbers[send])

# Print the available sends for each round
for round_num in range(1, 31):
    print(f"r{round_num} = [BloonSend(eco_data['Cost/6s'][i], eco_data['Eco/6s'][i], eco_data['Send Name'][i]) for i in {round_sends[round_num]}]")