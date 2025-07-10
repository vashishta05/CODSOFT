import tkinter as tk
import random
from PIL import Image, ImageTk

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        global user_score
        user_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "You lose!"

# Function to load and resize images
def load_image(filename, size=(120, 120)):  
    img = Image.open(filename)
    img = img.resize(size, Image.LANCZOS)  # Resize images for UI consistency
    return ImageTk.PhotoImage(img)

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    choices_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")
    
    # Update images
    user_image_label.config(image=images[user_choice])
    computer_image_label.config(image=images[computer_choice])

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    choices_label.config(text="Choose Rock, Paper, or Scissors")
    result_label.config(text="")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")
    user_image_label.config(image=default_image)
    computer_image_label.config(image=default_image)

# Function to terminate the game
def terminate_game():
    root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("600x700")  # Adjusted window size
root.configure(bg="#2E2E2E")

# Load images
rock_img = load_image("rock.png")
paper_img = load_image("paper.png")
scissors_img = load_image("scissors.png")
default_image = load_image("default.png")  # Default image before selection

images = {"Rock": rock_img, "Paper": paper_img, "Scissors": scissors_img}

# Initialize scores
user_score = 0
computer_score = 0

# Create labels
welcome_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#2E2E2E", fg="white")
welcome_label.pack(pady=10)

choices_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg="#2E2E2E", fg="white")
choices_label.pack(pady=10)

# Images for user and computer choices
image_frame = tk.Frame(root, bg="#2E2E2E")
image_frame.pack(pady=10)

# Left side (User)
user_frame = tk.Frame(image_frame, bg="#2E2E2E")
user_frame.grid(row=0, column=0, padx=40)

user_image_label = tk.Label(user_frame, image=default_image, bg="#2E2E2E")
user_image_label.pack()
user_label = tk.Label(user_frame, text="YOU", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="lightblue")
user_label.pack()

# VS label
vs_label = tk.Label(image_frame, text="VS", font=("Arial", 18, "bold"), bg="#2E2E2E", fg="white")
vs_label.grid(row=0, column=1, padx=20)

# Right side (Computer)
computer_frame = tk.Frame(image_frame, bg="#2E2E2E")
computer_frame.grid(row=0, column=2, padx=40)

computer_image_label = tk.Label(computer_frame, image=default_image, bg="#2E2E2E")
computer_image_label.pack()
computer_label = tk.Label(computer_frame, text="COMPUTER", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="red")
computer_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#2E2E2E", fg="white")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer Score: {computer_score}", 
                       font=("Arial", 14), bg="#2E2E2E", fg="white")
score_label.pack(pady=10)

# Create buttons for user choices
button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock ✊", command=lambda: play_game("Rock"), 
                        width=12, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper ✋", command=lambda: play_game("Paper"), 
                         width=12, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors ✌️", command=lambda: play_game("Scissors"), 
                            width=12, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
scissors_button.grid(row=0, column=2, padx=10)

# Reset and Terminate buttons
reset_button = tk.Button(root, text="Reset Game", command=reset_game, width=15, height=2, 
                         bg="#FFD700", fg="black", font=("Arial", 12, "bold"))
reset_button.pack(pady=10)

terminate_button = tk.Button(root, text="Terminate Game", command=terminate_game, width=15, height=2, 
                             bg="#FF5733", fg="white", font=("Arial", 12, "bold"))
terminate_button.pack(pady=10)

# Run the main loop
root.mainloop()
