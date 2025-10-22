# app_gradio.py
import gradio as gr
import subprocess

def run_command(cmd, arg=""):
    if cmd == "list":
        proc = subprocess.run(["./playlist", "list"], capture_output=True, text=True)
    elif cmd == "add":
        proc = subprocess.run(["./playlist", "add", arg], capture_output=True, text=True)
    elif cmd == "remove":
        proc = subprocess.run(["./playlist", "remove", arg], capture_output=True, text=True)
    else:
        return "Unknown command"
    return proc.stdout

with gr.Blocks() as demo:
    gr.Markdown("### C Playlist — Gradio UI\nMake sure `./playlist` is compiled before running.")
    with gr.Row():
        btn_list = gr.Button("List songs")
        btn_add = gr.Button("Add song")
        btn_remove = gr.Button("Remove song")
    txt = gr.Textbox(label="Song name / Remove index")
    out = gr.Textbox(label="Output")

    btn_list.click(fn=lambda: run_command("list"), inputs=None, outputs=out)
    btn_add.click(fn=lambda x: run_command("add", x), inputs=txt, outputs=out)
    btn_remove.click(fn=lambda x: run_command("remove", x), inputs=txt, outputs=out)

if __name__ == "__main__":
    demo.launch()
