from dataset.utils import *
from const import LETTERS

class QADSET():
    def __init__(self, name='RACE'):
        self.dset_name = name
        self.dataset = load_mini_rm(0, False)
        print(f"type: {type(dataset)} | length: {len(dataset)}")
        # Prompt Question
        self.npq, self.bpq = None, None

    # Prepare Natural Prompt Question
    def npq(self):
        if self.npq is None:
            self.npq = [(data.get_natural_prompt(), data.answer_idx) for data in self.dataset]
        return self.npq

    # Prepare Brown Prompt Question
    def bpq(self):
        if self.bpq is None:
            self.bpq = [(data.get_brown_prompt(), data.answer_idx) for data in self.dataset]
        return self.bpq
    
    def choices(self, mode='index'):
        desc, index, index_desc = [], [], []
        for data in self.dataset:
            choice, idx = data.choice, LETTERS[0:len(data.choices)]
            index.append(idx)
            desc.append(choice)
            index_desc.append(list(map('. '.join, zip(idx, choice))))
        if mode == 'index':
            return index
        elif mode == 'desc':
            return desc
        elif mode == 'index_desc':
            return index_desc
        else:
            raise NotImplementedError
        
if __name__ == '__main__':
    pass
        