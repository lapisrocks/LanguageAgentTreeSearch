import json

def calculate_overall_accuracy(filename):
    overall_count = 0  # total number of instances
    overall_correct = 0  # total number of correct instances
    running_avg = 0
    prev_acc = 0

    with open(filename, 'r') as f:
        count = 0  # number of instances for the current run
        for line in f:
            data = json.loads(line)
            acc = data['acc']

            # Check for reset
            if acc == 1.0 or acc == 0.0 and prev_acc != 1.0 and prev_acc != 0.0:
                # Use the last running average to find the number of correct instances for this run
                correct = int(running_avg * count)
                
                # Update overall counters
                overall_count += count
                overall_correct += correct
                
                # Reset for the next run
                count = 0
            
            # Update count for the current run
            count += 1
            
            # Keep track of the current running average
            running_avg = acc
            prev_acc = acc

        # Don't forget the last run
        if count > 0:
            correct = int(running_avg * count)
            overall_count += count
            overall_correct += correct

    # Calculate overall accuracy
    if overall_count == 0:
        return 0, count
    else:
        return overall_correct / overall_count, overall_count

filename = "/Users/andyzhou/Documents/Research/LLMPlanning/programming/root/test_mcts_hard_acc_full_4tst_temp_gpt4/humaneval-py._mcts_8_gpt-4_pass_at_k_1_py.jsonl"
res = calculate_overall_accuracy(filename)
overall_avg = res[0]
count = res[1]
print(f"Overall average accuracy: {overall_avg}")
print(f"Count: {count}")

