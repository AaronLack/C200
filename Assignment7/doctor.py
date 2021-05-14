def appendicitis():
    # Yes = "1"
    # No = "0"
    # tracker is a variable i set to store the data cases if a paitent has x symptom.
    tracker = 0
    # update tracker when going through each input
    tracker += int(input("Do you have abdominal pain?: "))
    tracker += int(input("Do you have nausea?: "))
    tracker += int(input("Do you have vomiting: "))
    tracker += int(input("Do you have a fever?: "))
    tracker += int(input("Do you have loss of appetite: "))
    # if the tracker count is greater than or = to 3, then the paitent has appendicitis.  
    # Otherwise they don't. 
    if tracker >= 3:
        return ("Appendicitis")
    else:
        return("No Appendicitis")


print(appendicitis())

if __name__ == "__main__":
    pass