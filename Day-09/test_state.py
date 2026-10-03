from agent.state import *
# create the initial state

# State: Method 1
state = create_state("Generate Random password and tell me what is current time")

print("Initial State: \n", state)

# State: Method 2
add_action(state, "Generate_password")

# State: Method 3
record_observation(state, "Generate_password", "^sds*2323")

# State: Method 4
next_step(state)

print("")
print("State after 1st iterration: \n", state)


# State: Method 5
finish(state, "Password:^sds*2323 \n Current time: 11-09-2026")

print("")
print("Final State: \n", state)

# State: Method 6
can_con = can_continue(state=state)

print("")
print("Can Continue:", can_con)
