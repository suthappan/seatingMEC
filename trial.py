import sys

room_data = {}
subj_data = {}
room_total = {}
total = 0

# Check if file provided as first argument, else read from STDIN
if len(sys.argv) > 1:
    try:
        in_file = open(sys.argv[1], 'r')
    except FileNotFoundError:
        in_file = sys.stdin
else:
    in_file = sys.stdin

for line in in_file:
    line = line.strip()
    if line.startswith("No"):
        continue
    line = line.replace(" ", "")
    line = line.replace(",,", ",")  # Sanitization
    data = line.split(",")
    _, room, sn, name, rn, slot, subj = data
    room = room.strip()
    subj = subj.strip()
    room_data.setdefault(room, {}).setdefault(subj, 0)
    room_data[room][subj] += 1
    subj_data.setdefault(subj, 0)
    subj_data[subj] += 1
    room_total.setdefault(room, 0)
    room_total[room] += 1
    total += 1

sep = '","'
subj_list = sorted(subj_data.keys())
title = '"Room' + sep + sep.join(subj_list) + sep + 'Total"'

# Here is where our output goes.
#out_file = sys.stdout
out_file = open("summary.csv", "w")

print(title, file=out_file)

for room_name in sorted(room_data.keys()):
    det = [room_name]
    for subj_name in subj_list:
        det.append(str(room_data.get(room_name, {}).get(subj_name, 0)))
    det.append(str(room_total.get(room_name, 0)))
    det_str = '"' + sep.join(det) + '"'
    print(det_str, file=out_file)

sum_list = ['Total']
for subj_name in sorted(subj_data.keys()):
    sum_list.append(str(subj_data[subj_name]))
sum_list.append(str(total))
sum_str = '"' + sep.join(sum_list) + '"'
print(sum_str, file=out_file)

# Close files
if in_file is not sys.stdin:
    in_file.close()

