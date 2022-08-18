# Lithuanian LM
  
This is a personal project to build a deep learning [language model](https://en.wikipedia.org/wiki/Language_model) that can learn the Lithuanian language, inspired after my completion of the 2022 [fast.ai course](https://course.fast.ai/).

## Description

The model is a 44 million parameter sequential RNN called [AWD-LSTM](https://arxiv.org/abs/1708.02182) from 2017. Initially pretrained on English text, I finetuned it on an archived copy of the [Lithuanian Wikipedia](https://dumps.wikimedia.org/ltwiki/) from August 1, 2022, obtained with the help of [WikiExtractor](https://github.com/attardi/wikiextractor).

Training was done on a [Kaggle notebook](https://www.kaggle.com/code/tomaspetrikas/lithuanian-lm) for ~7 hours with a single GPU and achieves a perplexity score of 34.7 on my dataset (random 10% validation set). The model was trained on approximately 250 MB of uncompressed text in total.

This could certainly be improved by training for 1-3 more epochs or using a more modern architecture. Subword-based tokenization would be much better suited for Lithuanian as well, as the size of the model's vocabulary was heavily restricted by limited GPU memory. That said, I feel satisfied with what I've learned by making this project so far and might leave those improvements for the future.

## Demo

A live demo with interactive examples is available on Hugging Face Spaces [here](https://huggingface.co/spaces/NoUsernameSelected/Lithuanian-LM).

The same code and models can also be found in the **Gradio** folder in this repository.
