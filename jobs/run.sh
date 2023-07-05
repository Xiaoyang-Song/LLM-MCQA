# Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`
# Running jobs
python main/main_mcqa.py --config=config/general.yaml --dset=RACE --n=10 --ans_mode=index --model=gpt2 --version=gpt2
# python main/main_mcqa.py --config=config/general.yaml --dset=RACE --n=10 --ans_mode=desc --model=gpt2 --version=gpt2
# python main/main_mcqa.py --config=config/general.yaml --dset=RACE --n=10 --ans_mode=index-desc --model=gpt2 --version=gpt2


