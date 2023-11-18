# Purpose of App: The overall purpose of this app is to be a midterm calculator, that lets a user calculate their best guess for who will win the midterm elections that year. (Fed. only).
# As a reminder house and some of senate is up every 2 years, but president is up for election every 4.

# This current block is focused only on presidential as it should be simpler. Winner needs 270 out of 538 ec (electoral college) votes to win.
class State():
    def __init__(self, name, party, total_ec, senate_count, house_seat_count):
        self.name = name
        self.party = party
        self.total_ec = total_ec
        self.senate_count = senate_count
        self.house_seat_count = house_seat_count
        self.house_seats = {}

    def set_party(self, party):
        self.party = party

    



    


states = [
    State('Alabama', "", 9, 2, 7),
    State('Alaska', "", 3, 2, 1),
    State('Arizona', "", 11, 2, 9),
    State('Arkansas', "", 6, 2, 4),
    State('California', "", 55, 2, 52),
    State('Colorado', "", 9, 2, 8),
    State('Connecticut', "", 7, 2, 5),
    State('Delaware', "", 3, 2, 1),
    State('District', "", 3, 0, 0),
    State('Florida', "", 29, 2, 28),
    State('Georgia', "", 16, 2, 14),
    State('Hawaii', "", 4, 2, 2),
    State('Idaho', "", 4, 2, 2),
    State('Illinois', "", 20, 2, 17),
    State('Indiana', "", 11, 2, 9),
    State('Iowa', "", 6, 2, 4),
    State('Kansas', "", 6, 2, 4),
    State('Kentucky', "", 8, 2, 6),
    State('Louisiana', "", 8, 2, 6),
    State('Maine', "", 4, 2, 2),
    State('Maryland', "", 10, 2, 8),
    State('Massachusetts', "", 11, 2, 9),
    State('Michigan', "", 16, 2, 13),
    State('Minnesota', "", 10, 2, 8),
    State('Mississippi', "", 6, 2, 4),
    State('Missouri', "", 10, 2, 8),
    State('Montana', "", 3, 2, 2),
    State('Nebraska', "", 5, 2, 3),
    State('Nevada', "", 6, 2, 4),
    State('New Hampshire', "", 4, 2, 2),
    State('New Jersey', "", 14, 2, 12),
    State('New Mexico', "", 5, 2, 3),
    State('New York', "", 29, 2, 26),
    State('North Carolina', "", 15, 2, 14),
    State('North Dakota', "", 3, 2, 1),
    State('Ohio', "", 18, 2, 15),
    State('Oklahoma', "", 7, 2, 5),
    State('Oregon', "", 7, 2, 6),
    State('Pennsylvania', "", 20, 2, 17),
    State('Rhode Island', "", 4, 2, 2),
    State('South Carolina', "", 9, 2, 7),
    State('South Dakota', "", 3, 2, 1),
    State('Tennessee', "", 11, 2, 9),
    State('Texas', "", 38, 2, 38),
    State('Utah', "", 6, 2, 4),
    State('Vermont', "", 3, 2, 1),
    State('Virginia', "", 13, 2, 11),
    State('Washington', "", 12, 2, 10),
    State('West Virginia', "", 5, 2, 2),
    State('Wisconsin', "", 10, 2, 8),
    State('Wyoming', "", 3, 2, 1),
]


def assign_all_states_parties(states):
    acceptable_parties = ['i', 'd', 'r']

    for state in states:
        party_affiliation = input(
            f"Enter party affiliation of {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
        while True:
            if party_affiliation.lower() in acceptable_parties:
                state.set_party(party_affiliation)
                break
            else:
                print('You may only enter "i", "d", or "r"')
                party_affiliation = input(
                    f"Enter party affiliation of {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
    
    for state in states:
        party_affiliations = []
        for seat in range(state.senate_count):
            party_affiliation = input(
                f"Enter party affiliation for Senate seat {seat + 1} of {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
            while True:
                if party_affiliation.lower() in acceptable_parties:
                    party_affiliations.append(party_affiliation)
                    break
                else:
                    print('You may only enter "i", "d", or "r"')
                    party_affiliation = input(
                        f"Enter party affiliation for Senate seat {seat + 1} of {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
        
        state.senate_seats = party_affiliations
    
    for state in states:
        house_seats = {}
        for i in range(state.house_seat_count):
            party_affiliation = input(
                f"Enter party affiliation of House seat {i + 1} in {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
            while True:
                if party_affiliation.lower() in acceptable_parties:
                    house_seats[i] = party_affiliation
                    break
                else:
                    print('You may only enter "i", "d", or "r"')
                    party_affiliation = input(
                        f"Enter party affiliation of House seat {i + 1} in {state.name}.\nChoose one of the following (i)ndependent, (r)epublican, (d)emocrat: ")
        
        state.house_seats = house_seats


# I did this just to check total ec (electoral college votes) equal 538, it does. It is annoying to have to enter the party for all 51 states before getting the total, but can't think of way around that for now.
total_ec_sum = sum(state.total_ec for state in states)
print(total_ec_sum)



def presidential_calculator(states):
    republican_counter = 0
    democrat_counter = 0
    independent_counter = 0

    for state in states:
        if state.party.lower() == 'r':
            republican_counter += state.total_ec
        if state.party.lower() == 'd':
            democrat_counter += state.total_ec
        if state.party.lower() == 'i':
            independent_counter += state.total_ec
    return republican_counter, democrat_counter, independent_counter

def senate_calculator(states):
    republican_counter = 0
    democrat_counter = 0
    independent_counter = 0

    for state in states:
        for party in state.senate_seats:
            if party == 'r':
                republican_counter += 1
            elif party == 'd':
                democrat_counter += 1
            elif party == 'i':
                independent_counter += 1
    return republican_counter, democrat_counter, independent_counter

def house_calculator(states):
    republican_counter = 0
    democrat_counter = 0
    independent_counter = 0

    for state in states:
        for party in state.house_seats.values():
            if party == 'r':
                republican_counter += 1
            elif party == 'd':
                democrat_counter += 1
            elif party == 'i':
                independent_counter += 1

    return republican_counter, democrat_counter, independent_counter







def main():
    assign_all_states_parties(states)

    republican_votes, democrat_votes, independent_votes = presidential_calculator(states)
    republican_senate_seats, democrat_senate_seats, independent_senate_seats = senate_calculator(states)
    republican_house_seats, democrat_house_seats, independent_house_seats = house_calculator(states)

    print("Presidential Election:")
    print("Republican Votes:", republican_votes)
    print("Democrat Votes:", democrat_votes)
    print("Independent Votes:", independent_votes)

    print("\nSenate Breakup:")
    print("Republican Senate Seats:", republican_senate_seats)
    print("Democrat Senate Seats:", democrat_senate_seats)
    print("Independent Senate Seats:", independent_senate_seats)

    print("\nHouse Breakup:")
    print("Republican House Seats:", republican_house_seats)
    print("Democrat House Seats:", democrat_house_seats)
    print("Independent House Seats:", independent_house_seats)

if __name__ == "__main__":
    main()
