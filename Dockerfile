FROM python:3.11-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8080
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
