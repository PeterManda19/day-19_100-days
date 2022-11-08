print("Loan Calculator.")
print()
print("Shows how much money you owe for a loan of $1,000 with a 5% APR (Annual Percentage Rate) over 10 years.")
print()
loan = 1000
perc = 0.05

for yrs in range(1,11):
  owing = loan + (loan*0.05)*yrs
print("You owe $",owing)


def endGame():
  while True:
    print()
    input("""Thank you for using Loan Calculator """)
    print()
    continue


if __name__ == "__main__":
  endGame()