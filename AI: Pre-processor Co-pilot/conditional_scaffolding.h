#ifndef MACRO_SAFETY_H
#define MACRO_SAFETY_H

// Scaffolding for conditional debug mode
#ifdef DEBUG_LOG
    #define LOG_VAL(x) printf("[DEBUG] Value is: %d\n", (x))
#else
    #define LOG_VAL(x)
#endif

#endif