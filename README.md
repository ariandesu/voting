# Voting Systems App 🗳

Welcome to the **Voting Systems App**! This is a Streamlit-based web application that allows users to simulate and explore different voting systems. The app provides an interactive way to understand how various voting methods work and how they can produce different outcomes based on the same set of votes.

## Features

- **Multiple Voting Systems**: The app supports five different voting systems:
  1. **First Past the Post (FPTP)**
  2. **Approval Voting**
  3. **Preferential Voting**
  4. **Condorcet Method**
  5. **Borda Count**

- **Interactive Interface**: Users can input the number of candidates and voters, and then specify the votes for each voter based on the selected voting system.

- **Real-Time Results**: The app calculates and displays the winner(s) and detailed vote counts or scores in real-time.

- **Visual Feedback**: A fun starburst animation is displayed when a winner is determined.

## How to Use

1. **Install Streamlit**: If you haven't already, install Streamlit using pip:
   ```bash
   pip install streamlit
   ```

2. **Clone the Repository**: Clone this repository to your local machine.

3. **Run the App**: Navigate to the directory containing the app and run the following command:
   ```bash
   streamlit run voting_app.py
   ```

4. **Set Up Candidates and Voters**:
   - Use the sidebar to select the number of candidates and voters.
   - Input the names of the candidates.

5. **Input Votes**:
   - Depending on the selected voting system, input the votes for each voter.
   - For example, in **First Past the Post**, each voter selects one candidate, while in **Approval Voting**, each voter can approve multiple candidates.

6. **Run the Voting System**:
   - Click the "Run Voting System" button to calculate the results.
   - The app will display the winner(s) and the detailed vote counts or scores.

## Voting Systems Explained

### 1. First Past the Post (FPTP)
- Each voter selects one candidate.
- The candidate with the most votes wins.

### 2. Approval Voting
- Each voter can approve any number of candidates.
- The candidate with the most approvals wins.

### 3. Preferential Voting
- Each voter ranks the candidates in order of preference.
- The votes are counted in rounds, with the least preferred candidate eliminated in each round until a candidate has a majority.

### 4. Condorcet Method
- Each voter ranks the candidates in order of preference.
- The app compares each candidate head-to-head against every other candidate.
- A candidate who wins all head-to-head comparisons is the Condorcet winner.

### 5. Borda Count
- Each voter ranks the candidates in order of preference.
- Points are assigned based on the rank (e.g., 1st place gets the highest points).
- The candidate with the most points wins.

## Example Usage

1. **Select "First Past the Post"** from the voting system dropdown.
2. Set the number of candidates to 3 and voters to 5.
3. Input candidate names: "Alice", "Bob", and "Charlie".
4. For each voter, select one candidate.
5. Click "Run Voting System" to see the results.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Any suggestions for improving the app or adding new features are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Streamlit** for providing an excellent framework for building interactive web apps.
- **Wikipedia** for detailed explanations of various voting systems.

Also you can checokout the voting app from this link 
---

Enjoy exploring the world of voting systems with this app! 🎉
