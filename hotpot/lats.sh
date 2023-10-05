python run.py \
    --task hotpot \
    --task_start_index 0 \
    --task_end_index 100 \
    --method_generate sample \
    --method_evaluate vote \
    --method_select greedy \
    --mcts \
    --n_generate_sample 5 \
    --n_evaluate_sample 1 \
    --n_select_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    --log logs/new_run.log \
    ${@}


# 0.3 dollars per line ->  30 dollars for 100 lines