import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0
print("This Program is Helping you Type Faster. Type the Word Programming as Fast as you can 5 Times")
input("Press Enter to Continue")
while len(times) < 5:
    start = t.time()
    word = (input("Type the Word: "))
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    
    if (word.lower() != "programming"):
        mistakes += 1
        
print ("You Made " + str(mistakes) + " Mistake(s)")
print ("Now Let's See Your Evolution")
t.sleep(4)
        
x = [1, 2, 3, 4, 5]
y = times
plt.plot (x ,y)
legend = ["1", "2", "3", "4", "5",]
plt.xticks(x, legend )
plt.ylabel('Times in Seconds')
plt.xlabel('Total Attempts')
plt.title('Yor Typing Speed Evolution')
plt.show()