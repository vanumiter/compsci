import serial
import tkinter as tk
import os
import csv

# serials
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
ser.open()

# defining variables
received_temperature = 0
received_lightlevel = 0
received_accel = 0
received_compass = 0
received_sound = 0

# csv headings
data_dict = {
    'temperature': received_temperature,
    'light level': received_lightlevel,
    'acceleration': received_accel,
    'compass': received_compass,
    'sound': received_sound
}

# csv file
csv_file_path = "data.csv"
is_header = not any(cell.isdigit() for cell in csv_file_path[0]) # checks if a file exists, if it doesn't then it writes a header
csvfile = open(csv_file_path, "a", newline='')
writer = csv.DictWriter(csvfile, fieldnames=['temperature', 'light level', 'acceleration', 'compass', 'sound']) # dictwriter calls the variables from the dictionary above and assigns them into their csv cells
if is_header: # refer to is_header variable
    writer.writeheader() # writes the header

# realtime data recorder
def update_labels():
    data = ser.readline().decode('utf-8') # decodes bytes instead of converting it into string with str()
    data.strip() # truncates whitespace
    
    if all(char in data for char in "!$^&;"): # data doesn't send properly (broken delimiters in this case) due to desynchronicity between microbit and pc, this ensures that it doesn't send such invalid data
        index_temp = data.index("!")
        index_light = data.index("$")
        index_accel = data.index("^")
        index_compass = data.index("&")
        index_sound = data.index(";")

        # slices the single string provided by the microbit into respective data based on the delimiters
        received_temperature = data[0:index_temp]
        received_lightlevel = data[index_temp+1:index_light]
        received_accel = data[index_light+1:index_accel]
        received_compass = data[index_accel+1:index_compass]
        received_sound = data[index_compass+1:index_sound]

        # renames the labels to display the recorded values every time the function runs
        temp_label.config(text=f"Temperature: {received_temperature}")
        light_label.config(text=f"Light Level: {received_lightlevel}")
        accel_label.config(text=f"Acceleration: {received_accel}")
        compass_label.config(text=f"Compass: {received_compass}")
        sound_label.config(text=f"Sound: {received_sound}")

        # updates dictionary
        data_dict.update({
            'temperature': received_temperature,
            'light level': received_lightlevel,
            'acceleration': received_accel,
            'compass': received_compass,
            'sound': received_sound
        })

        writer.writerow(data_dict) # writes the dictionary in a row
       
       # print(f"Temperature: {received_temperature}\nLight Level: {received_lightlevel}\nAcceleration: {received_accel}\nCompass: {received_compass}\nSound: {received_sound}")
    else:
        pass
    
    if root.winfo_exists(): # checks if window is open: updates if it is, closes everything if it isnt
        root.after(200, update_labels) # runs update_labels function every 200ms
    else:
        ser.close()
        os.exit() 

# clears csv file by pressing button
def clear_csv(): 
    clear_csvfile = open(csv_file_path, "w", newline='')
    clear_csvfile.truncate()
    clear_csvfile.close()
    writer.writeheader()



# creating main window
root = tk.Tk()
root.title("Microbit Data Displayer")

# labels and buttons
temp_label = tk.Label(root, text = "Temperature: ")
light_label = tk.Label(root, text = "Light Level: ")
accel_label = tk.Label(root, text = "Acceleration: ")
compass_label = tk.Label(root, text = "Compass: ")
sound_label = tk.Label(root, text = "Sound: ")
clear_button = tk.Button(root, text = "Clear CSV File", command=clear_csv) 

root.geometry("400x200")

temp_label.pack()
light_label.pack()
accel_label.pack()
compass_label.pack()
sound_label.pack()
clear_button.pack()

update_labels() 

root.mainloop() # initializes gui

csvfile.close()


      
