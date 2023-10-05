python main.py \
  --run_name "test_react3" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "reflexion" \
  --language "py" \
  --model "gpt-3.5-turbo" \
  --pass_at_k "1" \
  --max_iters "8" \
  --verbose
