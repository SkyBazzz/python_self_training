import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet


def read_page() -> str:
    war_page = requests.get(url="https://www.unian.net/war")
    return war_page.text


def find_links(html_text) -> ResultSet:
    bs = BeautifulSoup(html_text, features='html.parser')
    return bs.find_all(name="a", attrs={"class", "list-thumbs__title"})


def show_all_titles(titles: ResultSet) -> None:
    for title in titles:
        print(title.text.strip(), title["href"])


def main():
    html = read_page()
    links = find_links(html)
    show_all_titles(links)


if __name__ == "__main__":
    main()
