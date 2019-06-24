
#! /usr/bin/env python

import sys

# Your functions may be here.


stop_words = 0
total_words = 1

if __name__ == '__main__':
    # Your code here.
    
    for line in sys.stdin:
        try: 
            key, value = line.strip().split('=', 1)
            
            if key == sys.argv[1]: 
                stop_words = float(value)
            elif key == sys.argv[2]: 
                total_words = float(value)
        
        except Exception as e:
            continue
            
    print((stop_words / total_words) * 100)