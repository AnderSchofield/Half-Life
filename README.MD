

---

# Half-Life Module

## Description

The Half-Life Module is a Python code to calculate the half-life of a substance. It implements the `Drug` class that allows a user to manage different drugs and their respective levels in the body considering the decay over time. This code could be useful in various applications including medicine and physics.

## Installation

Make sure you have Python 3.x installed on your system.

1. Clone the repository with `git clone <repository url>`
2. Navigate to the cloned directory with `cd <repository name>`
3. No additional dependencies to install

## Usage

To use the Half-Life Module, import the `Drug` class in your Python code.

```python
from farma.half_life import Drug

# Assume the drug half-life is 5 hours and the absorption time is 1 hour
drug = Drug("path/to/folder", 5, 1)

# Adding a dose of 100
# The function returns a list of drug levels for the next 720 hours
levels = drug.AddDose(100, var)

# You can also get the difference in hours between the current date and the last time a dose was added
hours = drug.CDate()

# If needed, you can reset the files
drug.Erase()
```

## Contribution

This is an open project and contributions are welcome. If you want to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

Remember to replace `"path/to/folder"` with the actual path of the folder where the drug files will be stored, and `var` with the correct variable in the `AddDose` method.

Please review the content to make sure it aligns with your code's functionality as I'm making some assumptions based on the provided code.

I hope this is helpful! If you need more assistance, don't hesitate to ask.
