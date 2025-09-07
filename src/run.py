from streamlit.web import cli

if __name__ == "__main__":
    cli.main_run(["src/__main__.py", "--server.port", "8501"])