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

    # Prepare Natural Prompt Question
    def prepare_npq(self):
        self.npq
        