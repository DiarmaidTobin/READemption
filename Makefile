test:
	python3.3 tests/test_all.py

coverage:
	coverage3 run tests/test_all.py
	coverage3 report

package:
	python3 setup.py sdist

package_to_pypi:
	python3 setup.py sdist upload
	@echo "Go to https://pypi.python.org/pypi/READemption/"

html_doc:
	cd docs && make html && cd ..

upload_doc:
	cd docs/build/html/ && zip -r READemption_docs.zip * && cd ../../.. && mv docs/build/html/READemption_docs.zip .
	@echo "Upload at https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=READemption"

show_html_docs:
	firefox docs/build/html/index.html &

readme_txt:
	pandoc --from=markdown --to=plain README.md -o README.txt

readme_html:
	pandoc --from=markdown --to=html README.md -o README.html

readme_rst:
	pandoc --from=markdown --to=rst README.md -o README.rst

readme_clean:
	rm -f README.tex README.html README.rst
	rm -f README.tex README.html README.txt

pylint:
	pylint bin/reademption reademptionlib/* tests/*

new_release:
	@echo "* Please do this manually:"
	@echo "* ------------------------"
	@echo "* Change bin/reademption"
	@echo "* Change setup.py"
	@echo "* Change docs/source/conf.py"
	@echo "* Change CHANGELOG.txt"
	@echo "* Commit changes e.g. 'git commit -m 'Set version to 0.2.0'"	
	@echo "* Tag the commit e.g. 'git tag -a v0.1.9 -m 'version v0.1.9''"
	@echo "* After pushing generate a new release based on this tag at"
	@echo "  https://github.com/konrad/READemption/releases/new"
