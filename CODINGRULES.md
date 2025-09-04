# Coding rules

This file is intended to ground cursor / agents to follow a given number of rules.

## For writing tests

When you write tests, use the following best practices:

- use the comments `// Arrange`, `// Act`, `// Assert`
- use bdd style tests when possible
- don't factor the tests too much, unless I'm asking to
- name the system under test `sut`

When writting tests, don't write the implementation. I'll ask for this specifically.

## For writing production code

Whe, you write code, use the following best practices:

- Don't comment, assume the code should be self explainatory
- Don't write long functions
- Minimize the cyclomatic complexity
