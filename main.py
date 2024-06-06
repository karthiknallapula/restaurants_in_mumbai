import subprocess

# Execute webscraping.py
print("Executing webscraping.py...")
subprocess.run(["python", "webscrapping.py"])

# Execute ocr_processing.py
print("Executing ocr_processing.py...")
subprocess.run(["python", "ocr_processing.py"])

print("Process completed.")
