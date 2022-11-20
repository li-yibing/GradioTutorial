import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs=gr.Textbox(lines=2, placeholder="在这里填写你的名字"), outputs="text")

demo.launch()
