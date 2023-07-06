# Project Note

## Useful resources

### Dataset Description

1. [RACE](https://huggingface.co/datasets/race)
2. [COSMOS-QA](https://huggingface.co/datasets/cosmos_qa)

### Tentative Experimental Results

Model: GPT-J

| Dataset   | Method     | Accuracy  |
| --------- | ---------- | --------- |
|           | Index      | 23%       |
| RACE-M    | Desc       | 23%       |
|           | Index-Desc | 26%       |
| -------   | ---------- | --------- |
|           | Index      | 26.2%     |
| COSMOS-QA | Desc       | 18%       |
|           | Index-Desc | 13.8%     |

Model: GPT4All-J

| Dataset   | Method     | Accuracy  |
| --------- | ---------- | --------- |
|           | Index      | 23.4%     |
| RACE-M    | Desc       | 23.2%     |
|           | Index-Desc | 20.2%     |
| -------   | ---------- | --------- |
|           | Index      | 25%       |
| COSMOS-QA | Desc       | 16.2%     |
|           | Index-Desc | 13.8%     |
