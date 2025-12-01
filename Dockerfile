# 1. Use Python 3.9 (Stable)
FROM python:3.11-slim

# 2. Set folder
WORKDIR /app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy code
COPY . .

# 5. Permission & Run
RUN chmod +x run.sh
CMD ["./run.sh"]