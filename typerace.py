import time
sentence="The quick brown fox jumps over the lazy dog"
speeds=[]
attemps=0

print(f"This is a typerace game......\n {sentence}")

while True:
   start=time.time()
   a=input("Rewrite the sentence=")
   end=time.time()

   time_taken=end-start
   words=sentence.split()
   speed=(len(words)/time_taken)*60

   attemps += 1
   speeds.append(speed)

   if a == sentence:
        print(f"The time taken is {time_taken:.2f}sec") 
        print(f"speed of {speed:.2f} WPM.\n Thats great!")
   else:
        print("wrong sentence!")

   b=input("Do u want to play again?(y/n):")
   if b.lower() != "y":
        break
    
top=max(speeds)
print(f"At {attemps} attemps,the highest speed is {round(top,2)}WPM")


