# GS/EECS 6414 Final Project: Social Networks - The Tracking of COVID-19 Misinformation Using NLP and Graph-based Approaches

## Abstract
Misinformation during the COVID-19 pandemic resulted in many unnecessary infections, hospitalizations, and fatalities [10]. This is a trend that has been seen in past health epidemics [11, 12]. Our work aims to study the spread of COVID-19 misinformation on social media platforms such as Twitter and Reddit through a Natural Language Processing (NLP) and Graph-based approach. We use NetworkX, Gephi, Streamlit, Plotly, and Large Language Models to build a comprehensive analytics and visualization system that that is capable of extracting core metrics identifying malicious users in the social network. Lastly, our results are consistent with previous work
[1], however, we extend on what has been done by contributing a robust QA Dashboard system that is interactive and intuitive for users to learn about vaccine misinformation. This work can be valuable for many organizations that aim to address misinformation as it provides an actionable framework to implement.
## Work Distribution
- Twitter and LLM features were implemented by Shogo
- Reddit Dashboard was implemented by Aaryaman
## Installation 
1. To run our application, please ensure that you have installed the following dependencies:
```
pip install streamlit
pip install plotly-express
pip install wordcloud
pip install networkx
pip install tqdm
pip install networkx
pip install powerlaw
pip install praw
pip install nltk
pip install matplotlib
pip install pillow
```
2. Unfortunately, the finetuned large language model was too large to upload onto GitHub. We have provided the training script for you to obtain the model with its respective tokenizer. Please refer to [archive/QA_LLM.ipynb](https://github.com/stoyonaga/EECS6414_SocialNetworks/blob/main/archive/Twitter/QA_LLM.ipynb) and use [datasets/qa_data.json](https://github.com/stoyonaga/EECS6414_SocialNetworks/blob/main/datasets/qa_data.json) as the input file. You should place the model and tokenizer in a model directory that resides within the root of the project.

## Final Deliverables
- For access to our written report, please contact me! :)
- The midterm presentation can be found [here](https://github.com/stoyonaga/EECS6414_SocialNetworks/blob/main/presentation/1-presentation.pdf). For access to our final slides with video demos of the user interface, please contact me :)
