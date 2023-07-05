import openai
import os
import torch
# COLOR
import colored
import colorama
from colorama import Fore, Back, Style

def device_info():
    # DEVICE Configuration
    print(colored.fg("#ffbf00") + Style.BRIGHT + line(n=120, is_print=False))
    if torch.backends.mps.is_available():
        print("-- MPS is built: ", torch.backends.mps.is_built())
        print("-- Let's use GPUs!")
    elif torch.cuda.is_available():
        print(f"-- Current Device: {torch.cuda.get_device_name(0)}")
        print(
            f"-- Device Total Memory: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
        print("-- Let's use", torch.cuda.device_count(), "GPUs!")
    else:
        print("-- Unfortunately, we are only using CPUs now.")
    line(n=120)
    print(colored.fg("#d33682") + Style.NORMAL + line(n=120, is_print=False))

def line(x='-',n=80):
    return x*n
# Credit: https://github.com/BYU-PCCL/leveraging-llms-for-mcqa/blob/main/utils.py

def idx_to_ltr(idx):
    return chr(idx + ord("A"))


def ltr_to_idx(ltr):
    return ord(ltr) - ord("A")


def make_dir_if_does_not_exist(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def prep_openai_obj_for_save(obj, prompt_text=None):
    obj = dict(obj)
    for key in obj.keys():
        if isinstance(obj[key], openai.openai_object.OpenAIObject):
            obj[key] = prep_openai_obj_for_save(obj[key])
        if isinstance(obj[key], list):
            for i in range(len(obj[key])):
                if isinstance(obj[key][i], openai.openai_object.OpenAIObject):
                    obj[key][i] = prep_openai_obj_for_save(obj[key][i])
    if prompt_text is not None:
        obj["prompt_text"] = prompt_text
    return obj