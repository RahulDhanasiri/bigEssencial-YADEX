
import sys

current_key = None
word_total = 0

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
        
        if current_key != key:
            if current_key:
                print("{}\t{:d}".format(current_key, word_total))
                
            current_key = key
            word_total = 0
        
        word_total += count
        
    except Exception as e:
        continue  

if current_key:
    print("{}\t{:d}".format(current_key, word_total))