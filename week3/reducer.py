
# Your code for reducer here.
import sys

current_key = None
total_words = 0

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)

        if current_key != key:
            
            if current_key:
                print("{}\t{}".format(current_key, total_words))
            
            total_words = 0
            current_key = key
            
        total_words += count
    
    except ValueError as e:
        continue
    
if current_key:
    print("{}\t{}".format(current_key, total_words))