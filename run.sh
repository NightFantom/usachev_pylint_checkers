export PYTHONPATH=$PWD/src
echo $PYTHONPATH
pylint --load-plugins=usachev.checkers --disable=all --enable=forbidden_print_statement tests/resources >> report.txt