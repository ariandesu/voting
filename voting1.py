import streamlit as st
from itertools import combinations

# Define the voting functions here (first_past_the_post, approval_voting, preferential_voting, condorcet_method, borda_count)

def first_past_the_post(candidates, votes):
    try:
        vote_counts = {candidate: 0 for candidate in candidates}
        for vote in votes:
            if vote not in candidates:
                raise ValueError(f"Invalid vote: {vote} is not a valid candidate.")
            vote_counts[vote] += 1

        max_votes = max(vote_counts.values())
        winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]

        return winners, vote_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def approval_voting(candidates, votes):
    try:
        approval_counts = {candidate: 0 for candidate in candidates}
        
        for vote in votes:
            for candidate in vote:
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                approval_counts[candidate] += 1
        
        winner = max(approval_counts, key=approval_counts.get)
        
        return winner, approval_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def preferential_voting(candidates, votes):
    try:
        while True:
            vote_counts = {candidate: 0 for candidate in candidates}
            for vote in votes:
                if vote and vote[0] not in candidates:
                    raise ValueError(f"Invalid vote: {vote[0]} is not a valid candidate.")
                if vote:
                    vote_counts[vote[0]] += 1
            
            total_votes = sum(vote_counts.values())
            for candidate, count in vote_counts.items():
                if count > total_votes / 2:
                    return candidate, vote_counts
            
            min_votes = min(vote_counts.values())
            for candidate, count in vote_counts.items():
                if count == min_votes:
                    candidates.remove(candidate)
                    break
            
            for vote in votes:
                if candidate in vote:
                    vote.remove(candidate)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def condorcet_method(candidates, votes):
    try:
        pairwise_counts = {candidate: {opponent: 0 for opponent in candidates if opponent != candidate} for candidate in candidates}
        
        for vote in votes:
            for i, candidate in enumerate(vote):
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                for opponent in vote[i+1:]:
                    pairwise_counts[candidate][opponent] += 1
        
        for candidate in candidates:
            if all(pairwise_counts[candidate][opponent] > pairwise_counts[opponent][candidate] for opponent in candidates if opponent != candidate):
                return candidate, pairwise_counts
        
        return "No Condorcet Winner", pairwise_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def borda_count(candidates, votes):
    try:
        borda_scores = {candidate: 0 for candidate in candidates}
        
        for vote in votes:
            for rank, candidate in enumerate(vote):
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                points = len(candidates) - rank - 1
                borda_scores[candidate] += points
        
        max_score = max(borda_scores.values())
        winners = [candidate for candidate, score in borda_scores.items() if score == max_score]
        
        return winners, borda_scores
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Streamlit App
def main():
    st.title("🗳 Voting Systems App 🗳")
    
    st.sidebar.header("⚙ Settings")
    voting_system = st.sidebar.selectbox(
        "Choose a voting system 🎲",
        ["First Past the Post", "Approval Voting", "Preferential Voting", "Condorcet Method", "Borda Count"]
    )
    
    st.sidebar.header("👥 Set Number of Candidates and Voters")
    num_candidates = st.sidebar.number_input("Number of Candidates  ‍🤝‍🧑", min_value=1, value=3, step=1)
    num_voters = st.sidebar.number_input("Number of Voters 🗳", min_value=1, value=5, step=1)
    
    st.header("📝 Input Candidates")
    candidates = []
    for i in range(num_candidates):
        candidate = st.text_input(f"Candidate {i+1} 🏅", value=f"Candidate {i+1}")
        candidates.append(candidate)
    
    st.header("📥 Input Votes")
    votes = []
    for i in range(num_voters):
        st.subheader(f"Voter {i+1} 👤")
        if voting_system == "First Past the Post":
            vote = st.selectbox(f"Select a candidate for Voter {i+1} 🗳", candidates)
            votes.append(vote)
        elif voting_system == "Approval Voting":
            vote = st.multiselect(f"Select approved candidates for Voter {i+1} ✅", candidates)
            votes.append(vote)
        elif voting_system == "Preferential Voting":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
        elif voting_system == "Condorcet Method":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
        elif voting_system == "Borda Count":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
    
    if st.button("🚀 Run Voting System"):
        if voting_system == "First Past the Post":
            winners, vote_counts = first_past_the_post(candidates, votes)
        elif voting_system == "Approval Voting":
            winners, approval_counts = approval_voting(candidates, votes)
        elif voting_system == "Preferential Voting":
            winners, vote_counts = preferential_voting(candidates, votes)
        elif voting_system == "Condorcet Method":
            winners, pairwise_counts = condorcet_method(candidates, votes)
        elif voting_system == "Borda Count":
            winners, borda_scores = borda_count(candidates, votes)
        
        st.header("🏆 Results")
        if winners:
            st.write(f"The winner(s) is/are: 🎉 {winners} 🎉")
            
            # Starburst Explosion Animation
            st.markdown("""
                <style>
                @keyframes starburst {
                    0% { transform: scale(0); opacity: 1; }
                    50% { transform: scale(2); opacity: 0.5; }
                    100% { transform: scale(4); opacity: 0; }
                }
                .starburst {
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    width: 200px;
                    height: 200px;
                    background: radial-gradient(circle, #ffdd00, #ff5722);
                    clip-path: polygon(
                        50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%
                    );
                    animation: starburst 1.5s ease-out forwards;
                }
                </style>
                <div class="starburst"></div>
            """, unsafe_allow_html=True)
        else:
            st.write("No winner could be determined. 🤷‍♂")
        
        if voting_system == "First Past the Post":
            st.write("Vote Counts: 📊", vote_counts)
        elif voting_system == "Approval Voting":
            st.write("Approval Counts: ✅", approval_counts)
        elif voting_system == "Preferential Voting":
            st.write("Vote Counts: 📊", vote_counts)
        elif voting_system == "Condorcet Method":
            st.write("Pairwise Counts: 🤼", pairwise_counts)
        elif voting_system == "Borda Count":
            st.write("Borda Scores: 🏅", borda_scores)

if __name__ == "__main__":
    main()