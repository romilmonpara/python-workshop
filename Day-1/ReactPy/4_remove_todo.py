from reactpy import component, html, hooks, run

@component
def todo():
    tasks, set_tasks = hooks.use_state([])
    new_task, set_new_task = hooks.use_state('')

    def handle_input_change(event):
        set_new_task(event["target"]["value"])

    def add_task(event=None):
        if new_task.strip():
            set_tasks(tasks + [new_task])  # Add task to the list
            set_new_task('')

    def remove_task(index):
        set_tasks([task for i, task in enumerate(tasks) if i != index])  # Remove task by index

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
            [
                html.li(
                    task,
                    html.button({"onclick": lambda event, i=i: remove_task(i)}, "Remove")  # Add remove button
                ) 
                for i, task in enumerate(tasks)
            ]
        )
    )

run(todo)
