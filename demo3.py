import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "早上好" if is_morning else "晚上好"
    greeting = f"{salutation} {name}， 今天的温度是 {temperature} （华氏度）"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()
