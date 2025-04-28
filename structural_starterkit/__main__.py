"""
A module to designed to perform package installations, and verification of install,
in preparation for the StructuralPython "Python for Structural Engineers" ("pfse")
course.
"""

import pathlib
import time
from rich.console import Console
from rich.progress import track
from rich.markdown import Markdown
from rich.text import Text

console = Console()


def check_installs():
    """
    Runs various mini-scripts to validate that certain packages
    are installed correctly. Offers suggestions for remediation if not.
    """
    header = Markdown("# Structural Python Starter Kit")
    console.print(header)

    validating = Markdown("## Validating installed packages...")
    validating.style = "yellow"
    console.print(validating)

    funcs = [
        check_numpy,
        check_shapely,
        check_sectionproperties,
        check_openpyxl,
    ]
    msgs = []
    for func in track(funcs):
        msg = func()
        if msg is not None:
            msgs.append(msg)
        time.sleep(0.2)

    if len(msgs) != 0:
        for msg in msgs:
            if msg is not None:
                console.print(msg)
        notify = Markdown("# Inconsistencies encoutered")
        notify.style = "red"
        instructions = Markdown(
            "### Please use Ctrl-Shift-C to copy the above error messages and email them to connor@structuralpython.com"
        )
        instructions.style = "red"
        console.print(notify)
        console.print(instructions)
    else:
        verified = Markdown("# PfSE installation seems ok")
        verified.style = "green"
        close_windows = Markdown(
            "## You can now close any windows that have opened as a result of the test."
        )
        close_windows.style = "green"
        console.print(verified)
        console.print(close_windows)


def check_numpy():
    try:
        import numpy as np
    except Exception as err:
        err_msgs = Text("\nnumpy did not import properly:\n")
        for err_arg in err.args:
            err_msgs.append("\t" + err_arg + "\n")
        err_msgs.stylize("bold green")
        return err_msgs
    

def check_pandas():
    try:
        import pandas as pd
    except Exception as err:
        err_msgs = Text("\nnumpy did not import properly:\n")
        for err_arg in err.args:
            err_msgs.append("\t" + err_arg + "\n")
        err_msgs.stylize("bold green")
        return err_msgs


def check_shapely():
    try:
        from shapely import Polygon
    except Exception as err:
        err_msgs = Text("\nshapely did not import properly:\n")
        for err_arg in err.args:
            err_msgs.append("\t" + err_arg + "\n")
        err_msgs.stylize("bold cyan")
        return err_msgs


def check_sectionproperties():
    try:
        import sectionproperties.pre.library.primitive_sections as sections
        from sectionproperties.analysis.section import Section

        geometry = sections.circular_section(d=50, n=64)
        geometry.create_mesh(mesh_sizes=[2.5])
    except Exception as err:
        err_msgs = Text("\nsectionproperties example did not run properly:\n")
        for err_arg in err.args:
            err_msgs.append("\t" + err_arg + "\n")
        err_msgs.stylize("bold cyan")
        return err_msgs


def check_openpyxl():
    try:
        from openpyxl import Workbook

        wb = Workbook()
        dest_filename = "empty_book.xlsx"
        saved_file = pathlib.Path.home() / dest_filename
        wb.save(filename=saved_file)
        if not saved_file.exists():
            raise Exception(f"No file found: {saved_file}")
        else:
            saved_file.unlink()
    except Exception as err:
        err_msgs = Text("\nopenpyxl example did not run properly:\n")
        for err_arg in err.args:
            err_msgs.append("\t" + err_arg + "\n")
        err_msgs.stylize("bold yellow")
        return err_msgs


if __name__ == "__main__":
    check_installs()
