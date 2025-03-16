def hanoi(N, A, B, C):
    if N == 1:
        print(f"Move disk 1 from {A} to {C}")
        return
    hanoi(N - 1, A, C, B)
    print(f"Move disk {N} from {A} to {C}")
    hanoi(N - 1, B, A, C)

hanoi(3, 'A', 'B', 'C')
