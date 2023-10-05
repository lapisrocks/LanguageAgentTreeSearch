python main.py \
  --run_name "test_dfs_humaneval2" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "dfs" \
  --language "py" \
  --model "gpt-3.5-turbo" \
  --pass_at_k "1" \
  --max_iters "8" \
  --verbose
