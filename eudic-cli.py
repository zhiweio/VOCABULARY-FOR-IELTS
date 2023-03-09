#!/usr/bin/env python3

import sys

import click
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup


@click.group()
def cli():
    pass


@cli.command("excel")
@click.argument("input", type=click.File("r"), default=sys.stdin)
@click.argument("output", type=click.File("a+"), default=sys.stdout)
@click.option("-c", "--chapter", type=int, default=1)
def to_excel(input, output, chapter):
    html = input.read()
    soup = BeautifulSoup(html, "html.parser")
    data = {"words": [], "interpretations": []}
    for tr in soup.find_all("tr")[1:]:
        td_list = tr.find_all("td")
        word = td_list[1].text.strip()
        interpretation = td_list[2].text.strip()
        data["words"].append(word)
        data["interpretations"].append(interpretation)

    df = pd.DataFrame(data)
    df["phrases"] = ""
    df["examples"] = ""
    click.secho(f"Found {df.count()} words", fg="green")
    if output.name == "<stdout>":
        print(df)
    else:
        with pd.ExcelWriter(output.name, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name=f"Chapter {chapter:02d}")


@cli.command("txt")
@click.argument("input", type=click.Path(exists=True, file_okay=True))
@click.argument("output", type=click.File("w"), default=sys.stdout)
@click.option("-c", "--chapter", type=int, default=0)
def to_txt(input, output, chapter):
    assert chapter >= 0
    workbook = openpyxl.load_workbook(input)
    dfs = []
    if chapter == 0:
        sheets = workbook.sheetnames
    else:
        sheets = [workbook.sheetnames[chapter - 1]]
    for sheet in sheets:
        df = pd.read_excel(input, sheet_name=sheet, engine="openpyxl")
        dfs.append(df)

    df = pd.concat(dfs).fillna("")
    if output.name == "<stdout>":
        print(df)
    else:
        records = df.to_dict(orient="records")
        content = []
        for x in records:
            word = x["words"]
            desc1 = "<br>".join(x["interpretations"].split("\n"))
            desc2 = "<br>".join(x["phrases"].split("\n"))
            desc3 = "<br>".join(x["examples"].split("\n"))
            descriptions = [desc1, desc2, desc3]
            descriptions = [x for x in descriptions if x]
            descriptions = "<br>".join(descriptions)
            content.append(f"{word}@{descriptions}\n")
        output.writelines(content)


if __name__ == "__main__":
    cli()
