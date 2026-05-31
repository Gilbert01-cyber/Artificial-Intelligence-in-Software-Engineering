# AI Task: Preemptive Bug Fixing

## Project Overview
This project demonstrates the application of structured AI prompting to conduct an advanced code review on a vulnerable C function designed to append a node to a singly linked list. 

## AI Tool Used
* **AI Engine:** Gemini / ChatGPT
* **Prompting Model:** Role-Based Prompting ("Senior C Developer")

## Identified Flaws
1. **Logical/Correctness Flaw:** The original traversal loop terminated when `current` became `NULL`. Assigning `current = new_node;` only altered a local variable rather than updating the `next` pointer of the actual last node in the list.
2. **Memory Safety Flaw:** The function lacked a `NULL` check verifying if `malloc` successfully allocated memory, risking a **Segmentation Fault** upon dereferencing a failed allocation.

## Repository Contents
* `vulnerable_code.c`: The initial broken code provided in the assignment.
* `fixed_code.c`: The secure, refactored C function incorporating absolute pointer links and memory safety assertions.
