from fastai.text.all import *
import gradio as gr

learn_lt = load_learner('model_lt_2.pkl')
learn_smg = load_learner('model_smg_2.pkl')
label_lt = 'Lithuanian (Lietuvių)'
label_smg = 'Samogitian (Žemaičių)'

def get_completion(model_choice, prompt, word_count, temperature):
    if (model_choice.startswith('Lit')):
        return learn_lt.predict(prompt, word_count, temperature)
    elif (model_choice.startswith('Sam')):
        return learn_smg.predict(prompt, word_count, temperature)
    else:
        return 'Error: Something went wrong...'

input = gr.Textbox(label='Prompt')
slider_words = gr.Slider(label='Reply Length (words)', minimum=1, maximum=100, value=40, step=1)
slider_temp = gr.Slider(label='Temperature', minimum=0, maximum=1, value=0.75)
dd_model_choice = gr.Dropdown(label='Model', choices=[label_lt, label_smg], value=label_lt)

examples = [[label_lt, 'Europos Sąjunga (ES) – dvidešimt septynių Europos valstybių', None, None],
            [label_lt, 'Indijos vandenynas – trečias pagal dydį vandenynas', None, None],
            [label_smg, 'Žemaitiu kalba prigol baltu', None, None]]

intf = gr.Interface(fn=get_completion, inputs=[dd_model_choice, input, slider_words, slider_temp],
                    outputs='text', examples=examples, cache_examples=False, allow_flagging='never')
intf.launch(inline=False)
