import random
import hangman_words
import hangman_art

print(hangman_art.logo)
lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed this letter: {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"Opps! this letter is not in the word\n You guessed {guess}. You loose a life")


        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}. OOPS!! YOU LOSE THE GAME**********************")
            print("GAME OVER. TRY HARDER NEXT TIME.")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
