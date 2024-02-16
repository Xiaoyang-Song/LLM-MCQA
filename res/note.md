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

Model: Red Pajama 7B

| Dataset   | Method     | Accuracy  |
| --------- | ---------- | --------- |
|           | Index      | 44%       |
| RACE-M    | Desc       | 27%       |
|           | Index-Desc | 36%       |
| -------   | ---------- | --------- |
|           | Index      | 19.8%     |
| COSMOS-QA | Desc       | 22%       |
|           | Index-Desc | 24.8%     |

Model: MPT 7B

| Dataset   | Method     | Accuracy  |
| --------- | ---------- | --------- |
|           | Index      | 30%       |
| RACE-M    | Desc       | 23%       |
|           | Index-Desc | 26.4%     |
| -------   | ---------- | --------- |
|           | Index      | 23%       |
| COSMOS-QA | Desc       | 19.8%     |
|           | Index-Desc | 27.6%     |
