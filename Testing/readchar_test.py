import readchar

while(1):
    key = readchar.readkey();
    print(key);

    # Determine what to do based on the key input

    # Numbered Keys
    if(key == "1" or key == "9"):
        # Dive Key
        print("Sinking");

    elif(key == "2"):
        # Down Key
        print("Slower Forward");

    elif(key == "3"):
        # Toggle Light
        print("Toggled Light");

    elif(key == "4"):
        # Left Key
        print("Turning Left");
        
    elif(key == "5"):
        # Stop Turning
        print("Stop Turning & Advancing");

    elif(key == "6"):
        # Right Key
        print("Turning Right");

    elif(key == "7"):
        # Rising Key
        print("Rising");

    elif(key == "8"):
        # Faster Key
        print("Forward Faster");

    # Non-Numbering Keys
    elif(key == "e"):
        # Enable Key
        print("Endabled");

    elif(key == "q" or key == "c" or key == "x" or key == "z"):
        print("Execution Terminated by '"+key+"'");
        exit();

