def main():
    with open(file="python/day-1/input.txt", mode="r") as input:
        lines = input.readlines()
        counts = []
        current_elf = 0
        for line in lines:
            if line == "\n": 
               counts.append(current_elf)
               current_elf = 0
            else:
               current_elf += int(line)
        counts.sort(reverse=True)
        top_3 = sum(counts[:3])
        print(top_3)
           

if __name__ == "__main__":
    main()