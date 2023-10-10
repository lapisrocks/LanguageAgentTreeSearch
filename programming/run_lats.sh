python main.py \
  --run_name "test_gpt4" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "mcts" \
  --language "py" \
  --model "gpt-4" \
  --pass_at_k "1" \
  --max_iters "8" \
  --verbose
