from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    response = simpledialog.askstring(title='questions', prompt="what country does The Jungle book take place in?")
    #      // 3.  Use an if statement to check if their answer is correct
    if response=='India':
    #      // 4.  if the user's answer was correct, add one to their score 
        score +=1
    else:
        score-=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    response = simpledialog.askstring(title='questions', prompt="In Harry Potter and the Sorcerers Stone what keeps the three headed dog asleep?")
    if response=='music':
        score +=1
    #      // Option: Subtract a point from their score for a wrong answer
    else:
        score -=1
    response = simpledialog.askstring(title='questions', prompt="what year was Jurassic Park released?")
    if response=='1993':
        score +=1
    else:
        score -=1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title='', message='your score is '+str(score))
    # Run the window's .mainloop() method
    window.mainloop()
