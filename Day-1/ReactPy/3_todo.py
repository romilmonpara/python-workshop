from reactpy import component, html, hooks, run

@component
def todo():
    tasks, set_tasks = hooks.use_state([])
    new_task, set_new_task = hooks.use_state('')

    def handle_input_change(event):
        set_new_task(event["target"]["value"])

    def add_task(event=None):
        if new_task.strip():
            set_tasks(tasks + [new_task])  # Fix: Use set_tasks, not set_new_task
            set_new_task('')

    return html.div(
        html.h1("ReactPy To-do List"),
        html.input({
            "type": "text",
            "value": new_task,
            "onchange": handle_input_change,
            "placeholder": "Enter a new Task"
        }),
        html.button({"onclick": add_task}, "ADD TASK"),
        html.ul(
            [html.li(task) for task in tasks]  # Fix: Use a list, not a set
        )
    )

run(todo)