
with open("sonar_inputs.txt", "r") as f:
    sonar_inputs_raw = f.readlines()
    sonar_inputs = [int(line.strip("\n")) for line in sonar_inputs_raw]

# Problem 1:
# Return total number of increases between individual measurements.
prev = sonar_inputs[0]
total = 0
for i in range(1, len(sonar_inputs)):
    if sonar_inputs[i] > prev:
        total += 1
    prev = sonar_inputs[i]

print(f"Total increases for problem 1: {total}")

# Problem 2:
# Return total number of increases between sum of sliding window measurements Ex: A(1,3,2) vs B(3,2,5) vs C(2,5,6)
prev_window = sum((sonar_inputs[0], sonar_inputs[1], sonar_inputs[2]))
total = 0
for i in range(1, len(sonar_inputs)):
    window = sum((sonar_inputs[i], sonar_inputs[i + 1], sonar_inputs[i + 2]))
    if window > prev_window:
        total += 1
    if i == len(sonar_inputs) - 3:
        break
    prev_window = window

print(f"Total increases for problem 2: {total}")