import pandas

#  use gspread to edit/add data to google spread sheet

#  get a public sharable link from csv
#  remove edit?usp=sharing
#  add gviz/tq?tqx=out:csv&sheet=[SHEET'S_NAME]
URL = (
    "https://docs.google.com/spreadsheets/d/1A_ixfpvxmYxWN6Su4wo3FSY2E8de2vTdqi6KNL5BVUg/gviz/tq?tqx=out:csv&sheet=2013"
)
data = pandas.read_csv(URL)
print(data["income"].mean())
