# Eazy-Evals 
**Eazy-Evals** is a quick and dirty library for running evaluations of Large Language Model output, by comparing a ground truth evaluation set to the generated output from one or multiple LLMs.


## Models currently supported:
- **Google:**
	- text-bison-32k@002
	- text-bison@001
	- text-bison@002
	- text-unicorn@001
	- gemini-pro
	- MedLM-large
	- MedLM-medium
	- code-bison-32k@002
	- code-bison@001
	- code-gecko@001
	- code-gecko@002
- **OpenAI:**
	- GPT-3.5 Turbo
	- GPT-4
	- GPT-4 Turbo	

## Evaluation metrics supported: 
- Exact Match (case insensitive or case sensitive)
- Cosine similarity
- Bleu
- Rouge
- Levenshtein distance	

## Logging:
Results of an eval run can be logged in several different ways depending on the intended use. 
- For embedding in a CI/CD pipeline, logs can be written to stdout. 
- For local development or quick and dirty debugging, logs can be written to a local sqlite table, or a flat file (.txt, .csv or .jsonl)
- for large-scale evals, pretty dashboards or further analysis, logs can be written to Google BigQuery or using a SQLAlchemy connection. 

## Analytics: 
- Eval results are binned in quartiles and plotted in the included interactive-style notebook

## Ground truth samples: 
Input and output ground truth samples can be provided in a local or remote text file, with examples provided in .jsonl format e.g.
```
{
	"input_text":"What is the capital city of France?",
	"output_text":"Paris"
}
{
	"input_text":"Context: you are a talented elementary school art teacher. Answer the following question as concisely as possible. Question: What are the three primary colors?",
	"output_text":"Red, blue and yellow"
}
```
Conveniently, this is the same file format used to fine-tune models in Vertex AI. 
If a system prompt or prompt template is needed and not included in the evaluation file, it can be passed into the library at runtime and prepended to the input text examples when calling the LLM. 

![](assets/images/eazy-e-transparent.png)
