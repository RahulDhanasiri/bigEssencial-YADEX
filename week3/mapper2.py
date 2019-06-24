import sys

current_key = None
word_total = 0
sorted_key = None

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t', 1)
        count = int(count)
        
        if current_key != word:
            if current_key:
                print("{}\t{}\t{}".format(sorted_key, current_key, word_total))
                
            current_key = word
            sorted_key  = "".join(sorted(current_key))
            word_total = 0
        
        word_total += count
        
    except ValueError as e:
        print(e)
        continue    

if current_key:
    print("{}\t{}\t{}".format(sorted_key, current_key, word_total))