models.json: clean
	cat models.yaml | yq -o=json > models.json

clean:
	rm models.json &> /dev/null || true
