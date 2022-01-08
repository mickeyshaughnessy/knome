 This repo has programs related to a distributed reputation system

<!--[Contribution guidelines for this project](docs/CONTRIBUTING.md)-->
(images/sample.pdf)
(images/sample2.png)

# Iterated prisoner's dilemma
  In the pd/ directory. Run as `python main.py`. Adjust config settings in pd.py


# Reputation Principles:
1. Reputation is fungible.
2. Reputation can be created or destroyed through transactions with other accounts.
3. Reputation is correlated with the likelihood that future transactions partners will act to increase your reputation.
4. There is a fixed cost to each account, regardless of reputation.
5. Registering a transaction with the reputation system confers a benefit (to encourage participation) and also carries a risk (to discourage fake transactions).
6. If both parties cooperate, their reputation goes up modestly.
7. If both parties defect, their reputation does not change (and they pay the fixed transaction cost).
8. If either party defects, while the other party does not, the defecting party earns a large reward. The cooperating party earns no reward, and pays a penalty.

:w
