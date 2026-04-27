def countdown_bottles(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 == 1:
                print(f"Take one down pass it around, one bottle of beer on the wall.\n")
            else:
                print(f"Take one down pass it around, {i} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown_bottles(bottles)
    print("You’re out of beer. Go buy more!")


main()