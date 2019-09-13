
test:
	@docker run -v `pwd`:/code python:3  /code/bin/run_unittests.sh

run:
	@docker run -v `pwd`:/code python:3  /code/bin/run_app.sh
	@echo "================== RESULTS ==================="
	cat invited.txt
	@echo "== For additional details please check the log file =="
	

clean:
	rm -fr */__pycache__/


.PHONY: test
