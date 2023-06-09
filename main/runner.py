from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter, defaultdict
from tqdm import tqdm
from colorama import Fore, Back, Style
import colored
from tabulate import tabulate

# External imports
from dataset.datasets import QADSET
from models.models import *
from util.utils import *


class RUNNER():
    def __init__(self, dset, model):
        self.dset = dset
        self.model = model
        # Reset / Initialize Runner
        self.reset()

    def save(self, path):
        self.model = None # Model checkpoints will not be stored
        torch.save(self, path)

    def reset(self):
        self.token_of_interest = []
        self.likelihood = []
        self.probs = []
        self.preds = []
        self.gt = []

    def __call__(self, ans_mode, f):
        f.write(line('=', 80)+'\n' + "Experiment Appendix\n" + line('=', 80)+'\n')
        choices = self.dset.get_choices(ans_mode)
        data = self.dset.get_npq()
        for idx, (choice_lst, (prompt, answer_idx)) in enumerate(zip(tqdm(choices), data)):
            ll_lst, prob_lst, toi_lst = [], [], []
            for candidate in choice_lst:
                prob, ll, toi = self.model(prompt, candidate)
                # Likelihood
                ll_lst.append(ll.item())
                # PROBABILITY FOR EACH WORD IN THE SENTENCE
                prob_lst.append(prob)
                # TOKEN OF INTERESTS
                toi_lst.append(toi)
            # MCQA BASED ON LIKELIHOOD
            ll_lst = torch.tensor(ll_lst)
            pred = torch.argmax(ll_lst).item()
            # SAVE RELEVANT STATISTICS
            self.token_of_interest.append(toi_lst)
            self.likelihood.append(ll_lst)
            self.probs.append(prob_lst)
            self.preds.append(pred)
            self.gt.append(answer_idx)
            # Logging
            f.write(f">> QUESTION #{idx+1:<5} | Ground Truth: {answer_idx} | Answer: {pred}")
            f.write(" | \u2714\n" if answer_idx == pred else " | \u2718\n" )
            f.write(f"-- Log Inverse-Perplexity: {list(np.round(np.array(ll_lst), 4))}\n")

        # Results logging
        self.preds = np.array(self.preds)
        self.gt = np.array(self.gt)
        acc = sum(self.preds == self.gt) / len(self.gt)
        f.write(line('=', 80)+'\n')
        f.write(f"MCQA Accuracy: {acc * 100:.2f}%\n")
        f.write(line('=', 80)+'\n')


if __name__ == '__main__':
    # Test
    dset = QADSET()
    runner = RUNNER(dset, None)
    runner('index_desc')
