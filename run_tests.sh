#!/usr/bin/env bash
# filepath: run_tests.sh

# 1) Compilează fișierele sursă cu gcc (versiunea din WSL)
gcc Backtracking.c -o backtracking
gcc DP.c -o dp
gcc Greedy.c -o greedy

# 2) Inițializează fișierul CSV
echo "TestFile,Algorithm,TimeS" > results.csv

# 3) Rulează doar pentru testele in7.txt - in16.txt
for i in {1..20}; do
    testfile="tests/in${i}.txt"

    # BACKTRACKING
    /usr/bin/time -f "%e" -o time.txt ./backtracking < "$testfile"
    elapsed=$(cat time.txt)
    echo "in${i},Backtracking,$elapsed" >> results.csv

    # DP
    /usr/bin/time -f "%e" -o time.txt ./dp < "$testfile"
    elapsed=$(cat time.txt)
    echo "in${i},DP,$elapsed" >> results.csv

    # GREEDY
    /usr/bin/time -f "%e" -o time.txt ./greedy < "$testfile"
    elapsed=$(cat time.txt)
    echo "in${i},Greedy,$elapsed" >> results.csv
done

# Șterge fișierul temporar și afișează mesaj de finalizare
rm -f time.txt
echo "Testele s-au rulat. Rezultatele se găsesc în results.csv"