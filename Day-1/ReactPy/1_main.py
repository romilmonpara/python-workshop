from reactpy import component, run, html

@component
def HelloReactPy():

    return html.div("Hello ReactPy")

if __name__ == '__main__':
    run(HelloReactPy)