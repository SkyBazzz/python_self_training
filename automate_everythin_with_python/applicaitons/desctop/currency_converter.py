from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox
from bs4 import BeautifulSoup
import requests


def get_rate(first_currency: str, second_currency: str) -> float:
    """Gets rate of between provided currencies
    Args:
          first_currency: first currency
          second_currency: second currency
    Return:
        rate: currencies rate

    """
    url = f"https://www.x-rates.com/calculator/?from={first_currency}&to={second_currency}&amount=1"
    content = requests.get(url, timeout=5).text
    parser = BeautifulSoup(content, "html.parser")
    rate = parser.find("span", class_="ccOutputRslt").get_text()
    rate = rate[:6]
    return float(rate)


def show_currency():
    input_amount = float(text.text())
    in_cur = in_combo.currentText()
    tar_cur = target_combo.currentText()
    rate = get_rate(in_cur, tar_cur)
    result = input_amount * rate
    output_amount = f"{result:.2f}"
    message = f"{input_amount} {in_cur} is {output_amount} {tar_cur}"
    output_label.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel("")
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

in_combo = QComboBox()
currencies = ["USD", "EUR"]
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

text = QLineEdit()
layout3.addWidget(text)

button = QPushButton("Convert")
layout3.addWidget(button)
button.clicked.connect(show_currency)


window.setLayout(layout)
window.show()

app.exec()
