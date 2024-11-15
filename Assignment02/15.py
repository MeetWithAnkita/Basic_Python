# 15. Develop a Python script to determine the minimum number of 100
# rupee notes, 200 rupee notes, 500 rupee notes and 2000 rupee notes
# required to dispense a given sum of money.
def calculate_notes(amount):
    
    denominations = [2000, 500, 200, 100]
    note_count = {}  
    
    for note in denominations:
        note_count[note] = amount // note
        amount %= note  

    return note_count


amount = int(input("Enter the amount in rupees: "))
note_count = calculate_notes(amount)


print("Minimum number of notes required:")
for note, count in note_count.items():
    print(f"Rs. {note} notes: {count}")
