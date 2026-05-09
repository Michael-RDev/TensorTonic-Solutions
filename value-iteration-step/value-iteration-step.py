def value_iteration_step(values, transitions, rewards, gamma):
    num_states = len(values)
    new_values = [0.0] * num_states

    for s in range(num_states):
        q_values = []
        for a in range(len(transitions[s])):
            expected_value = 0
            for s_prime in range(num_states):
                expected_value += transitions[s][a][s_prime] * values[s_prime]
            q_s_a = rewards[s][a] + (gamma * expected_value)
            q_values.append(q_s_a)
        new_values[s] = max(q_values)
    return new_values