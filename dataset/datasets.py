from dataset.utils import *

class QADSET():
    def __init__(self, name='RACE'):
        self.dset_name = name
        self.dataset = load_mini_rm(0, False)
        print(f"type: {type(dataset)} | length: {len(dataset)}")
        data = dataset[0]
        print(data.parts)
        print(data.choices)
        print(data.answer_idx)
        print(data.task)
        print(data.exemplars)

        # Prompt Question
        self.npq, self.bpq = None, None

    # Prepare Natural Prompt Question
    def get_npq(self):
        if self.npq is None:
            self.npq = [data.get_natural_prompt() for data in self.dataset]
        return self.npq

    # Prepare Brown Prompt Question
    def get_bpq(self):
        if self.bpq is None:
            self.bpq = [data.get_brown_prompt() for data in self.dataset]
        return self.bpq
    
    def get_ans_lst(self):
        desc = [data.choices for data in self.dataset]
        index = []

if __name__ == '__main__':
    pass
        