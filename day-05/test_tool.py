from tools import get_current_time, roll_dice,generate_password,read_file

print(f"Current Time is: {get_current_time()}");
print(f"Roll dice: {roll_dice()}");
print(f"Password: {generate_password()}");

print(f"File content of notes.txt: \n {read_file("data/notes.txt")}")
print(f"File content of notes1.txt with gracefull error: {read_file("data/notes1.txt")}")




