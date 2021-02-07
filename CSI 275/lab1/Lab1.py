numbers = [] #had to make a global variable so sort can use it

def build_list():
  userInput = ""

  while userInput.upper() != "DONE":

    #Outputting List
    if len(numbers) > 0:
      print("Current Numbers: "),
      for i in range(len(numbers)):
        print(numbers[i])

    #User Input
    userInput = input("Insert a number: ")

    #Checks User Input
    if userInput.isnumeric():
      numbers.append(userInput)
    elif userInput == "DONE":
      print("") #Creates break so it is easier to see sorted list
    else:
      print(userInput + " is not a number")

def sort_list(list):
  list = [int(x) for x in list] #changes the list from strings to ints so they can be properly sorted
  list.sort(key=int) 
  print("Sorted List: ")
  print(*list, sep = ", ") #Printed it in a line so it is easier to read

if __name__ == "__main__":
  build_list()
  sort_list(numbers)
