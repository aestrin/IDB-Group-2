FILES :=                \
    application.py      \
    IDB1.html           \
    IDB1.pdf            \
    IDB1.log            \
    requirements.txt    \
    apiary.apib         \
    app/__init__.py     \
    app/db_util.py      \
    app/models.py       \
    app/tests.py        \
    app/views.py


server:
	pip install -r requirements.txt
	python application.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";