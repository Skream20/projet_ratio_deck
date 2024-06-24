## Explanation of the Program `hand_tester_ygo V.1.0`

### Description
The program `Skream_update: V.1.0` is a starting hand simulator for the Yu-Gi-Oh! card game. It allows you to load a deck list from a `.ydk` file, simulate a large number of starting hand draws, and analyze the results to provide various statistics on the cards and the hands drawn.

### Features
1. **Loading the Yu-Gi-Oh! Database:**
   - The program fetches card information from an online API.
   
2. **Loading a Decklist:**
   - Users can provide a `.ydk` file containing their deck list.
   
3. **Simulating Draws:**
   - The program simulates a large number of starting hand draws from the deck list.
   
4. **Analyzing Results:**
   - The program can calculate the percentages of drawing specific cards.
   - It displays the most frequently drawn hands.
   - It calculates the probability of having a certain number of specific cards in the hand.
   
5. **Saving Results:**
   - Simulation results can be saved to a text file for later analysis.

### How to Use the Program

#### Step 1: Launch the Program
Run the `Skream_update: V.1.0` Python program.

#### Step 2: Load the Database
The program will automatically load card information from the API `https://db.ygoprodeck.com/api/v7/cardinfo.php`. Ensure you have an active internet connection.

#### Step 3: Load the `.ydk` File
The program will prompt you to enter the path to the `.ydk` file. This file should contain the list of cards in your deck. Ensure the file is in the correct format and the card IDs are correct.

#### Step 4: Select Cards for Analysis
The program will prompt you to enter the IDs or exact names of the cards you want to analyze, separated by commas.

#### Step 5: Simulation and Analysis
The program simulates all possible draws of starting hands (based on your deck size) and provides several analysis options:

1. **Percentage chance of drawing a specific card.**
2. **Most frequently drawn hands.**
3. **Probability of having a certain number of specific cards in the hand.**

#### Step 6: Results and Performance
The program calculates and displays the number of draws per second, the total number of draws, and the total execution time.

### Saving the Results
The results of the simulation, including the percentages of drawing each specific card, the most frequent hands, and performance statistics, are saved to a text file named `resultats.txt`.

### Conclusion
The program `Skream_update: V.1.0` is a powerful tool for analyzing draw chances in a Yu-Gi-Oh! deck. By following the steps above, you can load your deck, perform simulations, and obtain precise statistics to improve your game strategy.
