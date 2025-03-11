from reactpy import component, hooks, html, run

@component
def Counter():
    count, set_count = hooks.use_state(0)

    def increment(event=None):
        set_count(count + 1)

    return html.div(
        html.h1(f"Count: {count}"),
        html.button({"onclick": increment}, "Increase")
    )

if __name__ == "__main__":
    run(Counter)


# increment = lambda: set_count(count + 1)
# decrement = lambda: set_count(count - 1)
# return html.div(
#     html.h1(f"Count: {count}"),
#     html.button({"on_click": increment}, "+"),
#     html.button({"on_click": decrement}, "-")
# )