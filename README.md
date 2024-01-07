# detect-homoglyphs

A Python script that detects [confusable characters](https://util.unicode.org/UnicodeJsps/confusables.jsp?a=abcdefghijklmnopqrstuvwxyz&r=None).

## Usage
```bash
python detect_homoglyphs.py FILE
```

## Example
```bash
python detect_homoglyphs.py valid.yaml
echo $?
0
python detect_homoglyphs.py invalid.yaml
Found non-ASCII character: "с". Unicode point 1089 found in "jdbс:mysql://localhost:3306/mydatabase"
echo $?
1
```
