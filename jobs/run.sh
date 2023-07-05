# Running jobs
python main/main_mcqa.py --config=config/gpt-j.yaml --dset=RACE --n=10 --ans_mode=index --model=gpt-j --version=EleutherAI/gpt-j-6B
python main/main_mcqa.py --config=config/gpt-j.yaml --dset=RACE --n=10 --ans_mode=desc --model=gpt-j --version=EleutherAI/gpt-j-6B
python main/main_mcqa.py --config=config/gpt-j.yaml --dset=RACE --n=10 --ans_mode=index-desc --model=gpt-j --version=EleutherAI/gpt-j-6B


