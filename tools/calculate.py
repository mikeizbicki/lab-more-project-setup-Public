"""
This file defines the calculate tool, which evaluates mathematical expressions and returns results in JSON format.
"""

import json

def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression string and return the result or error as a JSON-formatted string.

    >>> calculate("2+2")
    '{"result": 4}'

    >>> calculate("10*5")
    '{"result": 50}'

    >>> calculate("2/0")
    '{"error": "division by zero"}'
    """
    try:
        result = eval(expression)
        return json.dumps({"result": result})
    except Exception as e:
        return json.dumps({"error": str(e)})

tool_schema = {
  "type": "function",
  "function": {
    "name": "calculate",
    "description": "Evaluate a mathematical expression and return the result or error as a JSON-formatted string",
    "parameters": {
      "type": "object",
      "properties": {
        "expression": {
          "type": "string",
          "description": "The mathematical expression to evaluate"
        }
      },
      "required": ["expression"]
    }
  }
}