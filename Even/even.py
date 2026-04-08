def main():

    numbers = [1,2,3,4,5,6,7,8]
    even = []
     
    for number in numbers:
        if number % 2 == 0:
           even.append(number)
    print(even)
if __name__ == "__main__":
    main()
