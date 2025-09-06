from tkinter import *
import random

# Game State
player_score = 0
ai_score = 0
round_number = 1
game_active = True


def handle_choice(player_choice):
    global player_score, ai_score, game_active

    if not game_active:
        return  # Prevent playing during inactive state

    ai_choice = random.choice(["stone", "paper", "scissor"])

    # Determine result
    if ai_choice == player_choice:
        result = f"🤝 Draw! AI chose {ai_choice.capitalize()}."
    elif (player_choice == "stone" and ai_choice == "scissor") or \
         (player_choice == "paper" and ai_choice == "stone") or \
         (player_choice == "scissor" and ai_choice == "paper"):
        player_score += 1
        result = f"🎉 You Win! AI chose {ai_choice.capitalize()}."
    else:
        ai_score += 1
        result = f"💥 You Lose! AI chose {ai_choice.capitalize()}."
    # Show result
    result_label.config(text=result)
    score_label.config(text=f"🧍 You: {player_score}    🤖 AI: {ai_score}")

    # Disable move buttons and enable next round
    set_buttons_state(DISABLED)
    next_button.config(state=NORMAL)
    game_active = False


def next_round():
    global round_number, game_active
    round_number += 1
    round_label.config(text=f"Round: {round_number}")
    result_label.config(text="Make your move.")
    set_buttons_state(NORMAL)
    next_button.config(state=DISABLED)
    game_active = True


def reset_game():
    global player_score, ai_score, round_number, game_active
    player_score = 0
    ai_score = 0
    round_number = 1
    game_active = True
    round_label.config(text="Round: 1")
    score_label.config(text="🧍 You: 0    🤖 AI: 0")
    result_label.config(text="Make your move.")
    set_buttons_state(NORMAL)
    next_button.config(state=DISABLED)


def set_buttons_state(state):
    stone_btn.config(state=state)
    paper_btn.config(state=state)
    scissor_btn.config(state=state)


# GUI Setup
root = Tk()
root.title("Stone Paper Scissors - Round Mode")
root.geometry("500x550")
root.configure(bg="black")
root.resizable(False, False)

# Title
title_label = Label(root, text="Stone ✊  Paper ✋  Scissor ✌️", font=(
    "Arial", 20, "bold"), bg="black", fg="white")
title_label.pack(pady=10)

# Round
round_label = Label(root, text="Round: 1", font=(
    "Arial", 14, "bold"), bg="black", fg="orange")
round_label.pack(pady=5)

# Score
score_label = Label(root, text="🧍 You: 0    🤖 AI: 0", font=(
    "Arial", 16, "bold"), bg="black", fg="white")
score_label.pack(pady=5)

# Result
result_label = Label(root, text="Make your move.",
                     font=("Arial", 14), bg="black", fg="yellow")
result_label.pack(pady=15)

# Move buttons
button_style = {"width": 15, "height": 2, "font": (
    "Arial", 12, "bold"), "relief": SUNKEN, "bd": 0}

stone_btn = Button(root, text="Stone ✊",
                   command=lambda: handle_choice("stone"), **button_style)
stone_btn.pack(pady=10)

paper_btn = Button(root, text="Paper ✋",
                   command=lambda: handle_choice("paper"), **button_style)
paper_btn.pack(pady=10)

scissor_btn = Button(root, text="Scissor ✌️",
                     command=lambda: handle_choice("scissor"), **button_style)
scissor_btn.pack(pady=10)

# Next round button (initially disabled)
next_button = Button(root, text="➡️ Next Round", command=next_round, font=(
    "Arial", 12), bg="orange", fg="black", state=DISABLED)
next_button.pack(pady=10)

# Reset game button
reset_btn = Button(root, text="🔄 Restart Game", command=reset_game,
                   font=("Arial", 12), bg="gray", fg="white")
reset_btn.pack(pady=10)

root.mainloop()
