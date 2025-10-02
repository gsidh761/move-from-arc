# Move From Arc

## Overview

## Requirements

- Python 3.x
- Arc Browser installed

## Installation

## Usage

Run the `main.py` script from the command line:

```
python3 main.py [-h] [-b] [--version]
```

## How It Works

1. **Read JSON**: Reads the `StorableSidebar.json` file from the Arc Browser's directory *or* the project's directory.
2. **Convert Data**: Converts the JSON data into a hierarchical bookmarks dictionary.
3. **Generate HTML**: Transforms the bookmarks dictionary into an HTML file.
4. **Write HTML**: Saves the HTML file with a timestamp, allowing it to be imported into any web browser.

And do not forget to give the project a star if you like it! :star:

## License

This project is licensed under the MIT License.
