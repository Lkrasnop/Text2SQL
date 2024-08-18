# Text2SQL

[![Text2SQL - CI/CD Pipeline](https://github.com/Lkrasnop/Text2SQL/actions/workflows/main.yml/badge.svg)](https://github.com/Lkrasnop/Text2SQL/actions/workflows/main.yml)

[![Python Application CI](https://github.com/Lkrasnop/Text2SQL/actions/workflows/test_main.yml/badge.svg)](https://github.com/Lkrasnop/Text2SQL/actions/workflows/test_main.yml)

1. Running run.bat file 
2. If the steamlit asking for Email just write 'no-replay@example.com' 
3. where the local host page will raise enter the prompt about the databased. 
4. Push the button Summit 
5. wait for the answer
6. repeat 3-5 until you find your results 

Here is a full README file tailored for your "Text2SQL" project:

---

## Overview

**Text2SQL** is a project aimed at converting natural language text queries into SQL statements. This tool is particularly useful for users who are not familiar with SQL but need to retrieve data from a database using simple, conversational language.

## Features

- **Natural Language Processing (NLP):** Utilizes NLP to interpret and convert plain language into SQL queries.
- **Multi-Platform:** The project is compatible with various platforms including Docker.
- **Automation:** Includes Makefile and Docker integration for ease of use and automation.
- **Testing:** Comprehensive testing with `pytest` to ensure reliability.

## Project Structure

```plaintext
Text2SQL/
├── .github/workflows/  # GitHub workflows for CI/CD
├── __pycache__/        # Python bytecode cache
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── Makefile            # Makefile for automating tasks
├── README.md           # Project documentation
├── README.txt          # Additional documentation
├── app.py              # Main application script
├── dataset.csv         # Sample dataset for testing
├── dockerfile          # Docker configuration file
├── main.py             # Main execution script
├── requirements.txt    # Python dependencies
├── run.bat             # Batch script for running the project
├── run.py              # Script for executing main tasks
├── test.py             # Test script
```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (optional but recommended)
- Make

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Text2SQL.git
   cd Text2SQL
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

To run the project:

```bash
python main.py
```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t text2sql .
   ```

2. Run the Docker container:
   ```bash
   docker run -it --rm text2sql
   ```

### Makefile Commands

The project includes a `Makefile` to streamline common tasks:

- Install dependencies:
  ```bash
  make install
  ```
- Run tests:
  ```bash
  make test
  ```

## Testing

Tests are written using `pytest`. To run the tests:

```bash
pytest
```

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact **Lior Krasnopolski**.

---

This README provides a comprehensive overview of your "Text2SQL" project and should be clear for anyone who wishes to contribute or use it.
