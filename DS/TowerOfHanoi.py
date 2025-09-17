def Tower_Of_Hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"move disk {n} from source {source} to destination {destination}")
        return
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print(f"move disk {n} from source {source} to destination {destination}")
    Tower_Of_Hanoi(n-1, auxiliary, source, destination)

n = 4
Tower_Of_Hanoi(n, "A", "B", "C")