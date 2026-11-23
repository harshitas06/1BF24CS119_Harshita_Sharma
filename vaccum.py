class VacuumCleanerAgent:
    def __init__(self):
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

        self.position = "A"

    def perceive(self, location, status):
        """
        Update the internal model based on the current percept.
        """
        self.position = location
        self.model[location] = status

    def choose_action(self):
        """
        Choose an action based on the current percept
        and the internal model of the environment.
        """

        if self.model[self.position] == "Dirty":
            return "Suck"

        if self.model[self.position] == "Obstacle":
            if self.position == "A":
                return "Move Right"
            else:
                return "Move Left"

        if self.position == "A":
            return "Move Right"
        else:
            return "Move Left"

    def execute_action(self, action):
        """
        Update the agent's position after performing an action.
        """

        if action == "Suck":
            self.model[self.position] = "Clean"

        elif action == "Move Right":
            self.position = "B"

        elif action == "Move Left":
            self.position = "A"


# Environment
environment = {
    "A": "Dirty",
    "B": "Obstacle"
}

agent = VacuumCleanerAgent()

print("Initial Environment:", environment)
print("Initial Agent Model:", agent.model)
print()

step = 0

while True:

    current_location = agent.position
    current_status = environment[current_location]

    # Agent perceives the environment
    agent.perceive(current_location, current_status)

    if current_status == "Obstacle":
        other_rooms_clean = all(
            status == "Clean"
            for room, status in environment.items()
            if room != current_location
        )

        if other_rooms_clean:
            print("Endpoint condition reached.")
            print("Obstacle cannot be cleaned.")
            print("All other rooms are clean.")
            print("Vacuum cleaner stopping...")
            break

    action = agent.choose_action()

    step += 1

    print(f"Step {step}")
    print("Location :", agent.position)
    print("Percept  :", current_status)
    print("Model    :", agent.model)
    print("Action   :", action)

    if action == "Suck":
        environment[agent.position] = "Clean"

    agent.execute_action(action)

    print("Environment:", environment)
    print()


print("Final Environment:", environment)
print("Final Agent Model:", agent.model)
