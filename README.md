При работе с airflow моя рекомендация использовать оффициальную сборку которую можно найти тут https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
Прочтите пожалуйста информацию которая там представлена 
Здесь найдете пример DAG для запуска контейнера airflow_template\dags\example_dag.py
Чтобы все начало работать так же в compose файле необходимо прокинуть вольюм под docker.socket (уже сделано)
- //var/run/docker.sock:/var/run/docker.sock

Чтобы запустилась сборка достаточно прописать docker compose up или docker compose up -d. Если Вас не забанили в гугле то можете узнать в чем разница.

PS как введете docker compose up\docker compose up -d ничего у Вас не заработает. 
Чтобы заработало еще раз прочтите пожалуйста строчку 2. Делаю это не из за вредности, а чтобы научились читать документацию. 
GLHF
PPS Курс по airflow https://stepik.org/course/99527/promo
