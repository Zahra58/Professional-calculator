from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from sympy import symbols, sympify, diff, integrate, sin, cos, tan, log, sqrt, exp

# Main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Professional Calculator")
main_window.resize(400, 600)

# All objects
text_box = QLineEdit()
text_box.setAlignment(Qt.AlignRight)
text_box.setFixedHeight(50)
text_box.setStyleSheet("font-size: 24px; padding: 5px;")

grid = QGridLayout()
grid.setSpacing(5)  # Add spacing between buttons for a cleaner layout

# Define buttons for basic operations and advanced functions
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'log',
    '(', ')', 'exp', 'd/dx', 'sqrt',
    '^', '<', '∫', 'Clear' , 'delete'
]

# Variable to store the current expression
expression = ""

# Function for button click event
def button_click():
    global expression
    button = app.sender()
    text = button.text()

    if text == "=":
        try:
            result = sympify(expression)
            result = result.evalf()
            # Limit to two decimal places
            text_box.setText(f"{result:.2f}")
            expression = str(result)
        except Exception as e:
            text_box.setText("Error")
            expression = ""
            print("Error:", e)

    elif text == "Clear":
        expression = ""
        text_box.clear()
    elif text == "delete":
        expression = ""
        text_box.clear()
    elif text == "d/dx":
        try:
            x = symbols('x')
            differentiated = diff(sympify(expression), x)
            text_box.setText(str(differentiated))
            expression = str(differentiated)
        except Exception as e:
            text_box.setText("Error")
            expression = ""
            print("Error:", e)

    elif text == "∫":
        try:
            x = symbols('x')
            integrated = integrate(sympify(expression), x)
            text_box.setText(str(integrated))
            expression = str(integrated)
        except Exception as e:
            text_box.setText("Error")
            expression = ""
            print("Error:", e)

    elif text in ["sin", "cos", "tan", "log", "sqrt", "exp", "^"]:
        expression += text + "("
        text_box.setText(expression)

    elif text == "<":
        expression = expression[:-1]
        text_box.setText(expression)

    else:
        expression += text
        text_box.setText(expression)

# Adding buttons to the grid layout and connecting signals
row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    button.setFixedSize(70, 70)  # Consistent button size for uniformity

    # Set default style and hover effect style
    button.setStyleSheet("""
        QPushButton {
            font-size: 18px;
            padding: 10px;
            background-color: #F0F0F0;
            color: black;
            border: 1px solid #BBBBBB;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #D3D3D3;
            border: 1px solid #A9A9A9;
        }
    """)

    # Customize color for specific buttons (e.g., operators)
    if text in ['/', '*', '-', '+', '=', '^']:
        button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                padding: 10px;
                background-color: #FFA07A;
                color: white;
                border: 1px solid #FF8C00;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF7F50;
            }
        """)
    elif text in ["Clear", "delete"] :
        button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                padding: 10px;
                background-color: #FF4500;
                color: white;
                border: 1px solid #FF6347;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF6347;
            }
        """)
    elif text in ['sin', 'cos', 'tan', 'log', 'sqrt', 'exp', 'd/dx', '∫']:
        button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                padding: 10px;
                background-color: #87CEFA;
                color: white;
                border: 1px solid #4682B4;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #00BFFF;
            }
        """)

    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col += 1
    
    if col > 4:  # Change to 4 columns for better layout
        col = 0
        row += 1

# Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)
master_layout.setContentsMargins(10, 10, 10, 10)  # Add padding around the main layout

main_window.setLayout(master_layout)

# Set overall app background color
main_window.setStyleSheet("background-color: #F5F5F5;")

# Show / Run our app
main_window.show()
app.exec_()