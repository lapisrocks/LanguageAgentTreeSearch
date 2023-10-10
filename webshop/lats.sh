python run.py \
    --backend gpt-3.5-turbo \
    --task_start_index 0 \
    --task_end_index 50 \
    --n_generate_sample 5 \
    --n_evaluate_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    --iterations 30 \
    --log logs/new_run.log \
    ${@}

# remember to change the url in lats.py to your local instance of WebShop 

