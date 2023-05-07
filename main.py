print("Fill in the blank lyrics!")
print()
print("(Type in the blank lyrics and see if you are as cool as me.)")
print()

counter = 1
while True:
  lyrics = input("Never going to ______ you up.")
  if lyrics == "give" or lyrics == "Give":
    print("You got it !")
  else:
    print("Nope, try again.")
    counter +=1
  if lyrics == "give":
    break
print("Well done! It only took you", counter, "attempts.")
