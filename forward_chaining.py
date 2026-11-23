
# Forward Chaining Algorithm

# Step 1: Initial facts
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

# Step 2: Rules
rules = [
    # If x is a missile, then x is a weapon
    ([("Missile", "x")],
     ("Weapon", "x")),

    # If x is a missile and A owns x,
    # then Robert sells x to A
    ([("Missile", "x"), ("Owns", "A", "x")],
     ("Sells", "Robert", "x", "A")),

    # If x is an enemy of America, x is hostile
    ([("Enemy", "x", "America")],
     ("Hostile", "x")),

    # If p is American, q is a weapon,
    # p sells q to r, and r is hostile,
    # then p is a criminal
    ([("American", "p"), ("Weapon", "q"),
      ("Sells", "p", "q", "r"), ("Hostile", "r")],
     ("Criminal", "p"))
]

# Variables used in rules
variables = {"x", "p", "q", "r"}


# Step 3: Match rule conditions with facts
def match_rule(premises, facts):

    substitutions = [{}]

    for pattern in premises:
        new_substitutions = []

        for sub in substitutions:
            for fact in facts:

                if pattern[0] != fact[0] or len(pattern) != len(fact):
                    continue

                new_sub = sub.copy()
                matched = True

                for p, f in zip(pattern[1:], fact[1:]):

                    if p in variables:
                        if p in new_sub and new_sub[p] != f:
                            matched = False
                            break
                        new_sub[p] = f

                    elif p != f:
                        matched = False
                        break

                if matched:
                    new_substitutions.append(new_sub)

        substitutions = new_substitutions

    return substitutions


# Step 4: Forward Chaining
def forward_chaining(facts, rules):

    while True:

        new_facts = []

        for premises, conclusion in rules:

            substitutions = match_rule(premises, facts)

            for sub in substitutions:

                result = tuple(sub.get(x, x) for x in conclusion)

                if result not in facts and result not in new_facts:
                    new_facts.append(result)

        # Stop if no new facts are generated
        if not new_facts:
            break

        # Add new facts to knowledge base
        for fact in new_facts:
            facts.add(fact)
            print("New fact:", fact)

    return facts


# Step 5: Execute the algorithm
result = forward_chaining(facts, rules)

# Step 6: Check the goal
if ("Criminal", "Robert") in result:
    print("\nRobert is a Criminal")
else:
    print("\nGoal not proved")
