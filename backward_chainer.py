from production import AND, OR, NOT, IF, THEN, match, populate, simplify
from data import zookeeper_rules

def backchain_to_goal_tree(rules, hypothesis):
    breakdown = [hypothesis]
    for i in rules:
        cons = i.consequent()
        if isinstance(cons, (AND, OR, NOT)):
            for a in cons.conditions():
                breakdown.append(backchain_to_goal_tree(rules, a))
        elif isinstance(cons, str):
            matched = match(cons, hypothesis)
            if matched is not None:
                antecedent = i.antecedent()
                x = populate(antecedent, matched)
                breakdown.append(backchain_to_goal_tree(rules, x))
        else:
            print(f"error")
    return simplify(OR(*breakdown))

if __name__ == "__main__":
    hypothesis = 'patrick is a zebra'
    goals = backchain_to_goal_tree(zookeeper_rules, hypothesis)
    print("goals'{}':".format(hypothesis))
    print(goals)