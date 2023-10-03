FROM python:3.10.12-alpine
WORKDIR /stock-price-analyzer
COPY . /stock-price-analyzer
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "run.py"]

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8080/api/health || exit 1