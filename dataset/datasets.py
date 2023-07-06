from dataset.utils import *
from const import LETTERS

class QADSET():
    def __init__(self, name='rm', n=500, verbose=False):
        # Basic dataset information
        self.dset_name, self.n = name, n
        self.dataset = get_questions_with_exemplars(
            info=get_dataset_info(self.dset_name), n_shots=0, n=self.n, do_strong_shuffle=False)
        if verbose:
            print(f"Dataset [{self.dset_name}] with {len(self.dataset)} questions are loaded successfully!")
            # print(f"type: {type(self.dataset)} | length: {len(self.dataset)}")
        # Prompt Question Preparation
        self.npq, self.bpq = None, None

    # Prepare Natural Prompt Question
    def get_npq(self):
        if self.npq is None:
            self.npq = [(data.get_natural_prompt(), data.answer_idx) for data in self.dataset]
        return self.npq

    # Prepare Brown Prompt Question
    def get_bpq(self):
        if self.bpq is None:
            self.bpq = [(data.get_brown_prompt(), data.answer_idx) for data in self.dataset]
        return self.bpq
    
    def get_choices(self, mode='index'):
        desc, index, index_desc = [], [], []
        for data in self.dataset:
            content, idx = data.choices, LETTERS[0:len(data.choices)]
            index.append(idx)
            desc.append(content)
            index_desc.append(list(map('. '.join, zip(idx, content))))
        if mode == 'index':
            return index
        elif mode == 'desc':
            return desc
        elif mode == 'index-desc':
            return index_desc
        else:
            raise NotImplementedError
        
if __name__ == '__main__':
    pass
        