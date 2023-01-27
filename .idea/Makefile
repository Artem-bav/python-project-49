install: # инициализир виртуальн окружен
	poetry install

brain-games: # make ...
	poetry run brain-games

build: # собираем пакет
	poetry build

publish: # проверка оформл пакета и публикац на PyPi
	poetry publish --dry-run
	
package-install: # установим собранный пакет в систему
	python3 -m pip install --user dist/*.whl
	
# <название Makefile>  (START makefile) 
make lint: # проверка содержимого директории brain_games на соответствие правилам написания кода
	poetry run flake8 brain_games
