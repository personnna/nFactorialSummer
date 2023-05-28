build:
	@printf "\e[31mBIP BOP... BUILDING!!!\e[0m\n"
	@docker build -t flask-app .

run:
	@printf "\e[32mRUNNING!!!\e[0m\n"
	docker run -it -p 8080:8080 -d --name flask-app flask-app