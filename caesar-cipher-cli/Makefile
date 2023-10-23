install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	cargo fmt --quiet

lint:
	cargo clippy --quiet

test:
	cargo test --quiet

run:
	cargo run 

all: format lint test run