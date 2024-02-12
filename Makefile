.PHONY: app

app:
	python -m streamlit run app/main.py --server.port 80
