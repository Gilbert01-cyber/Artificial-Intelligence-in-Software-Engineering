# AI: Pre-processor Co-pilot

## Description
This task involved using AI to identify safety risks in C macros, specifically focusing on operator precedence and side effects. I also used AI to generate conditional compilation scaffolding for a debug logging system.

## AI Tool Used
* **Gemini**

## Files
* [initial_macro.c](./initial_macro.c) - The initial unsafe macro featuring a precedence bug.
* [refactored_macro.c](./refactored_macro.c) - The optimized, safe version of the macro.
* [conditional_scaffolding.h](./conditional_scaffolding.h) - AI-generated header guards and debug macro scaffolding.

## Analysis and Reflection
Using AI as a Safety Inspector for the C Preprocessor is highly valuable because macros are handled before the compiler checks types or syntax logic. AI can quickly spot "invisible" errors like missing parentheses in operator precedence or side effects in multiple-argument evaluation that a developer might overlook.
