# PY3004	Chia từ điển thành các từ điển con kích thước K

import sys
def main():    
    input = sys.stdin.readline    
    N, K = map(int, input().split())    
    items = []    
    for _ in range(N):        
        key, value = input().split()        
        items.append((key, value))    
    for i in range(0, N, K):        
        chunk = items[i:i+K]        
        print(' '.join(f'{k}:{v}' for k, v in chunk))

if __name__ == "__main__":    
    main()