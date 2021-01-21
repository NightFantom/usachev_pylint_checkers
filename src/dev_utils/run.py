import pylint.lint

if __name__ == "__main__":
    pylint_opts = ["--load-plugins=usachev.checkers", "--disable=all", "--enable=forbidden_print_statement", "tests/resources"]
    pylint.lint.Run(pylint_opts)


