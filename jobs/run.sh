# Python Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Running jobs (test)
python main/main_mcqa.py --config=config/general.yaml --dset=rm --n=10 --ans_mode=index --model=gpt2 --version=gpt2
